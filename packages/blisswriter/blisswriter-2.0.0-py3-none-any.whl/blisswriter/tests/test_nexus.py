import os
import sys
import time
import psutil
import subprocess
from contextlib import contextmanager

import pytest
import numpy
import h5py.h5t
from silx.io import dictdump
from silx.io.utils import h5py_read_dataset, h5py_read_attribute

from blisswriter.io import nexus


@contextmanager
def nxroot(path, name):
    filename = os.path.join(str(path), name + ".h5")
    rootattrs = {
        "creator": "test",
        "creator_version": "1.0.0",
        "custom_root_attr": "custom_root_attr",
    }
    with nexus.nxRoot(filename, mode="a", rootattrs=rootattrs) as f:
        yield f


def test_nexus_root(tmpdir):
    with nxroot(tmpdir, "test_nexus_root") as h5group:
        validateNxRoot(h5group)


def test_nexus_entry(tmpdir):
    with nxroot(tmpdir, "test_nexus_entry") as h5group:
        entry = nexus.nxEntry(h5group, "entry0001")
        nexus.updated(entry, final=True)
        with pytest.raises(RuntimeError):
            nexus.nxEntry(entry, "entry0002")
        validateNxEntry(entry)


def test_nexus_entry_order(tmpdir):
    with nxroot(tmpdir, "test_nexus_entry") as h5group:
        for i in range(100):
            nexus.nxEntry(h5group, str(i))
            nexus.updateAttribute(h5group, "default", str(i))
        lst = [int(i) for i in h5group.keys()]
        assert lst == list(range(100))
        if nexus.ISSUE_1641_FIXED:
            assert h5group.attrs["default"] == "99"
        else:
            with pytest.raises(AssertionError):
                assert h5group.attrs["default"] == "99"


def test_nexus_process(tmpdir):
    with nxroot(tmpdir, "test_nexus_process") as h5group:
        entry = nexus.nxEntry(h5group, "entry0001")
        configdict = {"a": 1, "b": 2}
        for i, type in enumerate(["json", "ini", None]):
            process = nexus.nxProcess(
                entry, "process{:04d}".format(i), configdict=configdict, type=type
            )
            with pytest.raises(RuntimeError):
                nexus.nxProcess(h5group, "process0002", configdict=configdict)
            validateNxProcess(process)


def test_nexus_data(tmpdir):
    with nxroot(tmpdir, "test_nexus_data") as root:
        entry = nexus.nxEntry(root, "entry0001")
        process = nexus.nxProcess(entry, "process0001")
        data = nexus.nxData(process["results"], "data")
        s = (4, 3, 2)
        datadict = {
            "Fe K": numpy.arange(numpy.prod(s), dtype=float).reshape(s),
            "Ca K": numpy.arange(numpy.prod(s)).reshape(s) + 1,
            "S K": numpy.zeros(s),
        }
        axes = [
            ("y", numpy.arange(s[0]), {"units": "um"}),
            ("x", numpy.arange(s[1]), {}),
            ("z", {"shape": (s[2],), "dtype": int}, None),
        ]
        signals = [
            ("Fe K", datadict["Fe K"], {"interpretation": "image"}),
            ("Ca K", {"data": datadict["Ca K"]}, {}),
            ("S K", {"shape": s, "dtype": int}, None),
        ]
        nexus.nxDataAddAxes(data, axes)
        nexus.nxDataAddSignals(data, signals)

        validateNxData(data, axes, signals)
        signals = nexus.nxDataGetSignals(data)
        assert signals == ["Fe K", "Ca K", "S K"]

        nexus.markDefault(data["Ca K"])
        default = data.file[nexus.getDefault(data.file, signal=False)]
        default = nexus.dereference(default, current=root)
        assert default == nexus.getUri(data)
        default = data.file[nexus.getDefault(data.file, signal=True)]
        default = nexus.dereference(default, current=root)
        assert default == nexus.getUri(data["Ca K"])

        data = entry[nexus.DEFAULT_PLOT_NAME]
        signals = nexus.nxDataGetSignals(data)
        assert signals == ["Ca K", "Fe K", "S K"]
        assert data["y"].attrs["units"] == "um"
        assert data["Fe K"].attrs["interpretation"] == "image"
        for name in signals:
            assert data[name].shape == s
        for n, name in zip(s, list(next(iter(zip(*axes))))):
            assert data[name].shape == (n,)

        # Test dataset concatenation
        def vdatanamegen():
            c = 0
            while True:
                yield "vdata{}".format(c)
                c += 1

        vdataname = vdatanamegen()
        for virtual in False, True:
            value = {
                "axis": 0,
                "newaxis": True,
                "virtual": virtual,
                "data": [nexus.getUri(data[name]) for name in datadict],
            }
            _tmp = next(vdataname)
            vdata = nexus.nxCreateDataSet(process, _tmp, value, None)
            if virtual:
                assert nexus.vdsIsValid(vdata)
            for i, name in enumerate(datadict):
                numpy.testing.assert_array_equal(datadict[name], vdata[i])
            value["axis"] = 1
            vdata1 = nexus.nxCreateDataSet(process, next(vdataname), value, None)
            if virtual:
                assert nexus.vdsIsValid(vdata1)
            for i, name in enumerate(datadict):
                numpy.testing.assert_array_equal(datadict[name], vdata1[:, i])
            value["axis"] = 0
            value["newaxis"] = False
            vdata = nexus.nxCreateDataSet(process, next(vdataname), value, None)
            if virtual:
                assert nexus.vdsIsValid(vdata)
            for i, name in enumerate(datadict):
                numpy.testing.assert_array_equal(
                    datadict[name], vdata[i * s[0] : (i + 1) * s[0]]
                )
            value["axis"] = 1
            vdata = nexus.nxCreateDataSet(process, next(vdataname), value, None)
            if virtual:
                assert nexus.vdsIsValid(vdata)
            for i, name in enumerate(datadict):
                numpy.testing.assert_array_equal(
                    datadict[name], vdata[:, i * s[1] : (i + 1) * s[1]]
                )
            value["data"].append(nexus.getUri(data["y"]))
            with pytest.raises(RuntimeError):
                nexus.nxCreateDataSet(process, next(vdataname), value, None)


def test_nexus_StringAttribute(tmpdir):
    check_string_types(tmpdir, attribute=True, raiseExtended=True)


def test_nexus_StringDataset(tmpdir):
    check_string_types(tmpdir, attribute=False, raiseExtended=True)


def test_nexus_ExtStringAttribute(tmpdir):
    check_string_types(tmpdir, attribute=True, raiseExtended=False)


def test_nexus_ExtStringDataset(tmpdir):
    check_string_types(tmpdir, attribute=False, raiseExtended=False)


def test_nexus_uri(tmpdir):
    path = str(tmpdir)

    uri = "test1.h5::/a::/b"
    a, b = nexus.splitUri(uri)
    assert a == "test1.h5"
    assert b == "/a::/b"

    uri = nexus.normUri("./test1.h5::/a/../b")
    assert uri == "test1.h5::/b"

    uri = "test1.h5::/a/b"
    uriref = "test1.h5::/a"
    a, b = nexus.relUri(uri, uriref)
    assert a == "."
    assert b == "b"

    uri = os.path.join(path, "test1.h5::/a/b")
    uriref = os.path.join(path, "test1.h5::/a")
    a, b = nexus.relUri(uri, uriref)
    assert a == "."
    assert b == "b"

    uri = "test1.h5::/a/b"
    uriref = "test2.h5::/a"
    a, b = nexus.relUri(uri, uriref)
    assert a == "test1.h5"
    assert b == "/a/b"

    uri = os.path.join(path, "test1.h5::/a/b")
    uriref = os.path.join(path, "test2.h5::/a")
    a, b = nexus.relUri(uri, uriref)
    assert a == os.path.join(".", "test1.h5")
    assert b == "/a/b"

    uri = os.path.join(path, "..", "test1.h5::/a/b")
    uriref = os.path.join(path, "test2.h5::/a")
    a, b = nexus.relUri(uri, uriref)
    assert a == os.path.join("..", "test1.h5")
    assert b == "/a/b"


@pytest.mark.parametrize("abspath", [False, True])
def test_nexus_links(tmpdir, abspath):
    def namegen():
        i = 1
        while True:
            yield "link" + str(i)
            i += 1

    linkname = namegen()
    with nxroot(tmpdir, os.path.join("a", "b", "test1")) as f1:
        f1.create_group("a/b/c")
        g = f1["/a/b"]
        assert_same_target(g, g)
        # internal link up
        name = next(linkname)
        nexus.createLink(g, name, f1["a"], abspath=abspath)
        assert_same_target(f1["a"], g[name])
        link = g.get(name, getlink=True)
        assert link.path == "/a"
        assert isinstance(link, h5py.SoftLink)
        # internal link same level
        name = next(linkname)
        nexus.createLink(g, name, f1["a/b"], abspath=abspath)
        assert_same_target(f1["a/b"], g[name])
        link = g.get(name, getlink=True)
        assert link.path == "."
        assert isinstance(link, h5py.SoftLink)
        # internal link down
        name = next(linkname)
        nexus.createLink(g, name, f1["a/b/c"], abspath=abspath)
        assert_same_target(f1["a/b/c"], g[name])
        link = g.get(name, getlink=True)
        assert link.path == "c"
        assert isinstance(link, h5py.SoftLink)
        # external link down
        with nxroot(tmpdir, os.path.join("a", "test2")) as f2:
            name = next(linkname)
            nexus.createLink(f2, name, f1["a"], abspath=abspath)
            link = f2.get(name, getlink=True)
            assert_same_target(f1["a"], f2[name])
            assert link.path == "/a"
            if abspath:
                assert link.filename == f1.filename
            else:
                assert link.filename == os.path.join("b", "test1.h5")
            assert isinstance(link, h5py.ExternalLink)
        # internal link same level
        with nxroot(tmpdir, os.path.join("a", "b", "test2")) as f2:
            name = next(linkname)
            nexus.createLink(f2, name, f1["a"], abspath=abspath)
            link = f2.get(name, getlink=True)
            # assert_same_target(f1["a"], f2[name])
            assert link.path == "/a"
            if abspath:
                assert link.filename == f1.filename
            else:
                assert link.filename == os.path.join(".", "test1.h5")
            assert isinstance(link, h5py.ExternalLink)
        # external link up
        with nxroot(tmpdir, os.path.join("a", "b", "c", "test2")) as f2:
            name = next(linkname)
            nexus.createLink(f2, name, f1["a"], abspath=abspath)
            assert_same_target(f1["a"], f2[name])
            link = f2.get(name, getlink=True)
            assert link.path, "/a"
            if abspath:
                assert link.filename == f1.filename
            else:
                assert link.filename == os.path.join("..", "test1.h5")
            assert isinstance(link, h5py.ExternalLink)


def assert_same_target(node1, node2):
    target1 = nexus.dereference(node1)
    target2 = nexus.dereference(node2)
    assert nexus.normUri(target1) == nexus.normUri(target2)


def test_nexus_reshape_datasets(tmpdir):
    shape = 12, 5
    vshape = 3, 4, 5
    order = "C"

    def flatten(arr):
        return arr.flatten(order=order)

    kwargs = {
        "axis": 0,
        "virtual": True,
        "newaxis": False,
        "shape": vshape,
        "order": order,
        "fillvalue": 0,
    }
    fdatamem = numpy.arange(numpy.prod(shape))
    datamem = fdatamem.reshape(shape, order=order)

    def validate_dset(dset):
        numpy.testing.assert_array_equal(
            fdatamem, flatten(dset[()]), err_msg=nexus.getUri(dset)
        )

    filenames = (
        os.path.join("basedir1", "test1"),
        os.path.join("basedir1", "test2"),
        os.path.join("basedir1", "subdir", "test3"),
    )

    with nxroot(tmpdir, filenames[0]) as root1:
        with nxroot(tmpdir, filenames[1]) as root2:
            with nxroot(tmpdir, filenames[2]) as root3:
                for root in root1, root2, root3:
                    g = root.create_group("a")
                    g.create_group("b")
                    g["data"] = datamem
                    # Internal links
                    kwargs["data"] = [nexus.getUri(root["/a/data"])]
                    dset = nexus.nxCreateDataSet(root, "vdata", kwargs, None)
                    validate_dset(dset)
                    dset = nexus.nxCreateDataSet(root["/a"], "vdata", kwargs, None)
                    validate_dset(dset)
                    dset = nexus.nxCreateDataSet(root["/a/b"], "vdata", kwargs, None)
                    validate_dset(dset)

    # root1 -> root2, root3
    with nxroot(tmpdir, filenames[0]) as root1:
        kwargs["data"] = [nexus.getUri(root1["/a/data"])]

    for filename in filenames[1:]:
        with nxroot(tmpdir, filename) as root:
            dset = nexus.nxCreateDataSet(root, "vdatae", kwargs, None)
            validate_dset(dset)
        with nxroot(tmpdir, filename) as root:
            dset = nexus.nxCreateDataSet(root["/a"], "vdatae", kwargs, None)
            validate_dset(dset)
        with nxroot(tmpdir, filename) as root:
            dset = nexus.nxCreateDataSet(root["/a/b"], "vdatae", kwargs, None)
            validate_dset(dset)

    # root2 -> root1
    with nxroot(tmpdir, filenames[1]) as root2:
        kwargs["data"] = [nexus.getUri(root2["/a/data"])]
    with nxroot(tmpdir, filenames[0]) as root1:
        dset = nexus.nxCreateDataSet(root1, "vdatae", kwargs, None)
        validate_dset(dset)
    with nxroot(tmpdir, filenames[0]) as root1:
        dset = nexus.nxCreateDataSet(root1["/a"], "vdatae", kwargs, None)
        validate_dset(dset)
    with nxroot(tmpdir, filenames[0]) as root1:
        dset = nexus.nxCreateDataSet(root1["/a/b"], "vdatae", kwargs, None)
        validate_dset(dset)

    paths = ("/vdata", "/vdatae", "/a/vdata", "/a/vdatae", "/a/b/vdata", "/a/b/vdatae")
    for filename in filenames:
        with nxroot(tmpdir, filename) as root:
            data = root["/a/data"]
            assert shape == data.shape
            validate_dset(data)
            for path in paths:
                vdata = root[path]
                assert vshape == vdata.shape
                validate_dset(vdata)

    dirname = str(tmpdir)
    os.rename(os.path.join(dirname, "basedir1"), os.path.join(dirname, "basedir2"))
    os.rename(
        os.path.join(dirname, "basedir2", "test2.h5"),
        os.path.join(dirname, "basedir2", "test2_.h5"),
    )
    os.rename(
        os.path.join(dirname, "basedir2", "subdir", "test3.h5"),
        os.path.join(dirname, "basedir2", "subdir", "test3_.h5"),
    )
    filenames = (
        os.path.join("basedir2", "test1"),
        os.path.join("basedir2", "test2_"),
        os.path.join("basedir2", "subdir", "test3_"),
    )
    lostlinks = [
        ("/vdatae", "/a/vdatae", "/a/b/vdatae"),
        tuple(),
        ("/vdatae", "/a/vdatae", "/a/b/vdatae"),
    ]
    for filename, lost in zip(filenames, lostlinks):
        with nxroot(tmpdir, filename) as root:
            data = root["/a/data"]
            assert shape == data.shape
            validate_dset(data)
            for path in paths:
                vdata = root[path]
                assert vshape == vdata.shape
                if path in lost:
                    with pytest.raises(AssertionError):
                        validate_dset(vdata)
                else:
                    validate_dset(vdata)


def validateNxRoot(h5group):
    attrs = {
        "NX_class",
        "creator",
        "creator_version",
        "HDF5_Version",
        "file_name",
        "file_time",
        # "file_update_time",
        "h5py_version",
        "custom_root_attr",
    }
    assert set(h5group.attrs.keys()) == attrs
    assert h5group.attrs["NX_class"] == "NXroot"
    assert h5group.name == "/"


def validateNxEntry(h5group):
    attrs = ["NX_class"]
    assert set(h5group.attrs.keys()) == set(attrs)
    files = ["start_time", "end_time"]
    assert set(h5group.keys()) == set(files)
    assert h5group.attrs["NX_class"] == "NXentry"
    assert h5group.parent.name == "/"


def validateNxProcess(h5group):
    attrs = ["NX_class"]
    assert set(h5group.attrs.keys()) == set(attrs)
    files = ["program", "configuration", "date", "results"]
    assert set(h5group.keys()) == set(files)
    assert h5group.attrs["NX_class"] == "NXprocess"
    assert h5group.parent.attrs["NX_class"] == "NXentry"
    validateNxNote(h5group["configuration"])
    validateNxCollection(h5group["results"])


def validateNxNote(h5group):
    attrs = ["NX_class"]
    assert set(h5group.attrs.keys()) == set(attrs)
    files = ["date", "data", "type"]
    assert set(h5group.keys()) == set(files)
    assert h5group.attrs["NX_class"] == "NXnote"


def validateNxCollection(h5group):
    attrs = ["NX_class"]
    assert set(h5group.attrs.keys()) == set(attrs)
    assert h5group.attrs["NX_class"] == "NXcollection"


def validateNxData(h5group, axes, signals):
    attrs = ["NX_class", "axes", "signal", "auxiliary_signals"]
    assert set(h5group.attrs.keys()) == set(attrs)
    files = list(next(iter(zip(*axes)))) + list(next(iter(zip(*signals))))
    assert set(h5group.keys()) == set(files)
    assert h5group.attrs["NX_class"] == "NXdata"


def check_string_types(tmpdir, attribute=True, raiseExtended=True):
    # Test following string literals
    sAsciiBytes = b"abc"
    sAsciiUnicode = "abc"
    sLatinBytes = b"\xe423"
    sUTF8Unicode = "\u0101bc"
    sUTF8Bytes = b"\xc4\x81bc"
    sUTF8AsciiUnicode = "abc"
    sUTF8AsciiBytes = b"abc"
    # Expected conversion after HDF5 write/read
    strmap = {}
    strmap["ascii(scalar)"] = sAsciiBytes, sAsciiUnicode
    strmap["ext(scalar)"] = sLatinBytes, sLatinBytes
    strmap["unicode(scalar)"] = sUTF8Unicode, sUTF8Unicode
    strmap["unicode2(scalar)"] = sUTF8AsciiUnicode, sUTF8AsciiUnicode
    strmap["ascii(list)"] = [sAsciiBytes, sAsciiBytes], [sAsciiUnicode, sAsciiUnicode]
    strmap["ext(list)"] = [sLatinBytes, sLatinBytes], [sLatinBytes, sLatinBytes]
    strmap["unicode(list)"] = [sUTF8Unicode, sUTF8Unicode], [sUTF8Unicode, sUTF8Unicode]
    strmap["unicode2(list)"] = (
        [sUTF8AsciiUnicode, sUTF8AsciiUnicode],
        [sUTF8AsciiUnicode, sUTF8AsciiUnicode],
    )
    strmap["mixed(list)"] = (
        [sUTF8Unicode, sUTF8AsciiUnicode, sAsciiBytes, sLatinBytes],
        [sUTF8Bytes, sUTF8AsciiBytes, sAsciiBytes, sLatinBytes],
    )
    strmap["ascii(0d-array)"] = numpy.array(sAsciiBytes), sAsciiUnicode
    strmap["ext(0d-array)"] = numpy.array(sLatinBytes), sLatinBytes
    strmap["unicode(0d-array)"] = numpy.array(sUTF8Unicode), sUTF8Unicode
    strmap["unicode2(0d-array)"] = numpy.array(sUTF8AsciiUnicode), sUTF8AsciiUnicode
    strmap["ascii(1d-array)"] = (
        numpy.array([sAsciiBytes, sAsciiBytes]),
        [sAsciiUnicode, sAsciiUnicode],
    )
    strmap["ext(1d-array)"] = (
        numpy.array([sLatinBytes, sLatinBytes]),
        [sLatinBytes, sLatinBytes],
    )
    strmap["unicode(1d-array)"] = (
        numpy.array([sUTF8Unicode, sUTF8Unicode]),
        [sUTF8Unicode, sUTF8Unicode],
    )
    strmap["unicode2(1d-array)"] = (
        numpy.array([sUTF8AsciiUnicode, sUTF8AsciiUnicode]),
        [sUTF8AsciiUnicode, sUTF8AsciiUnicode],
    )
    strmap["mixed(1d-array)"] = (
        numpy.array([sUTF8Unicode, sUTF8AsciiUnicode, sAsciiBytes]),
        [sUTF8Unicode, sUTF8AsciiUnicode, sAsciiUnicode],
    )
    strmap["mixed2(1d-array)"] = (
        numpy.array([sUTF8AsciiUnicode, sAsciiBytes]),
        [sUTF8AsciiUnicode, sAsciiUnicode],
    )

    with nxroot(tmpdir, "test_nexus_String{:d}".format(attribute)) as h5group:
        h5group = h5group.create_group("test")
        if attribute:
            out = h5group.attrs
        else:
            out = h5group
        for name, (value, expectedValue) in strmap.items():
            decodingError = "ext" in name or name == "mixed(list)"
            if raiseExtended and decodingError:
                with pytest.raises(UnicodeDecodeError):
                    ovalue = nexus.asNxChar(value, raiseExtended=raiseExtended)
                continue
            else:
                ovalue = nexus.asNxChar(value, raiseExtended=raiseExtended)
            # Write/read
            out[name] = ovalue
            if attribute:
                value = h5py_read_attribute(out, name)
            else:
                value = h5py_read_dataset(out[name])
            # Expected type and value?
            if "list" in name or "1d-array" in name:
                assert isinstance(value, numpy.ndarray)
                value = value.tolist()
                assert list(map(type, value)) == list(map(type, expectedValue)), name
                firstValue = value[0]
            else:
                firstValue = value
            msg = "{} {} instead of {}".format(name, type(value), type(expectedValue))
            assert type(value) is type(expectedValue), msg
            assert value == expectedValue, msg
            # Expected character set?
            if not attribute:
                charSet = out[name].id.get_type().get_cset()
                if isinstance(firstValue, bytes):
                    # This is the tricky part, CSET_ASCII is supposed to be
                    # only 0-127 while we actually allow 0-255
                    expectedCharSet = h5py.h5t.CSET_ASCII
                else:
                    expectedCharSet = h5py.h5t.CSET_UTF8
                msg = "{} type {} instead of {}".format(name, charSet, expectedCharSet)
                assert charSet == expectedCharSet, msg


def test_nexus_exists(tmpdir):
    with nxroot(tmpdir, "test_nexus_entry") as root:
        uri = nexus.getUri(root)
    assert nexus.exists(uri)

    with nxroot(tmpdir, "test_nexus_entry") as root:
        uri = nexus.joinUri(nexus.getUri(root), "entry")
    assert not nexus.exists(uri)

    with nxroot(tmpdir, "test_nexus_entry") as root:
        nexus.nxEntry(root, "entry")
    assert nexus.exists(uri)

    with nxroot(tmpdir, "test_nexus_entry") as root:
        with pytest.raises(nexus.NexusInstanceExists):
            nexus.nxEntry(root, "entry", raise_on_exists=True)

    with nxroot(tmpdir, "test_nexus_entry") as root:
        parent = root["entry"]
        uri = nexus.joinUri(nexus.getUri(parent), "collection")
    assert not nexus.exists(uri)

    with nxroot(tmpdir, "test_nexus_entry") as root:
        parent = root["entry"]
        nexus.nxCollection(parent, "collection")
    assert nexus.exists(uri)

    with nxroot(tmpdir, "test_nexus_entry") as root:
        parent = root["entry"]
        with pytest.raises(nexus.NexusInstanceExists):
            nexus.nxCollection(parent, "collection", raise_on_exists=True)
        # with pytest.raises(RuntimeError):
        nexus.nxCollection(root, "collection")

    with nxroot(tmpdir, "test_nexus_entry") as root:
        parent = root["entry"]
        uri = nexus.joinUri(nexus.getUri(parent), "process")
    assert not nexus.exists(uri)

    with nxroot(tmpdir, "test_nexus_entry") as root:
        parent = root["entry"]
        nexus.nxProcess(parent, "process")
    assert nexus.exists(uri)

    with nxroot(tmpdir, "test_nexus_entry") as root:
        parent = root["entry"]
        with pytest.raises(nexus.NexusInstanceExists):
            nexus.nxProcess(parent, "process", raise_on_exists=True)

    with nxroot(tmpdir, "test_nexus_entry") as root:
        parent = root["entry"]
        uri = nexus.joinUri(nexus.getUri(parent), "subentry")
    assert not nexus.exists(uri)

    with nxroot(tmpdir, "test_nexus_entry") as root:
        parent = root["entry"]
        nexus.nxSubEntry(parent, "subentry")
    assert nexus.exists(uri)

    with nxroot(tmpdir, "test_nexus_entry") as root:
        parent = root["entry"]
        with pytest.raises(nexus.NexusInstanceExists):
            nexus.nxSubEntry(parent, "subentry", raise_on_exists=True)

    with nxroot(tmpdir, "test_nexus_entry") as root:
        parent = root["entry"]
        uri = nexus.joinUri(nexus.getUri(parent), "plot")
    assert not nexus.exists(uri)

    with nxroot(tmpdir, "test_nexus_entry") as root:
        parent = root["entry"]
        nexus.nxData(parent, "plot")
    assert nexus.exists(uri)

    with nxroot(tmpdir, "test_nexus_entry") as root:
        parent = root["entry"]
        with pytest.raises(nexus.NexusInstanceExists):
            nexus.nxData(parent, "plot", raise_on_exists=True)

    with nxroot(tmpdir, "test_nexus_entry") as root:
        parent = root["entry"]
        uri = nexus.joinUri(nexus.getUri(parent), "instrument")
    assert not nexus.exists(uri)

    with nxroot(tmpdir, "test_nexus_entry") as root:
        parent = root["entry"]
        nexus.nxInstrument(parent, "instrument")
    assert nexus.exists(uri)

    with nxroot(tmpdir, "test_nexus_entry") as root:
        parent = root["entry"]
        with pytest.raises(nexus.NexusInstanceExists):
            nexus.nxInstrument(parent, "instrument", raise_on_exists=True)

    with nxroot(tmpdir, "test_nexus_entry") as root:
        parent = root["entry/instrument"]
        uri = nexus.joinUri(nexus.getUri(parent), "detector")
    assert not nexus.exists(uri)

    with nxroot(tmpdir, "test_nexus_entry") as root:
        parent = root["entry/instrument"]
        nexus.nxDetector(parent, "detector")
    assert nexus.exists(uri)

    with nxroot(tmpdir, "test_nexus_entry") as root:
        parent = root["entry/instrument"]
        with pytest.raises(nexus.NexusInstanceExists):
            nexus.nxDetector(parent, "detector", raise_on_exists=True)

    with nxroot(tmpdir, "test_nexus_entry") as root:
        parent = root["entry/instrument"]
        uri = nexus.joinUri(nexus.getUri(parent), "positioner")
    assert not nexus.exists(uri)

    with nxroot(tmpdir, "test_nexus_entry") as root:
        parent = root["entry/instrument"]
        nexus.nxPositioner(parent, "positioner")
    assert nexus.exists(uri)

    with nxroot(tmpdir, "test_nexus_entry") as root:
        parent = root["entry/instrument"]
        with pytest.raises(nexus.NexusInstanceExists):
            nexus.nxPositioner(parent, "positioner", raise_on_exists=True)


def test_nexus_locked_exception(tmpdir):
    filename = str(tmpdir / "data.h5")
    lockscript = str(tmpdir / "lockscript.py")
    smffile = str(tmpdir / "locked.smf")

    content = f"""
import threading
from blisswriter.io import nexus

with nexus.File(r'{filename}', mode='a', locking=True) as f:
    f['a'] = 10
    f.flush()
    with open(r'{smffile}', 'w'):
        pass
    print('Locked and waiting to be killed')
    threading.Event().wait()
"""

    with open(lockscript, "w") as f:
        f.write(content)

    with subprocess.Popen([sys.executable, lockscript]) as proc:
        try:
            # Wait until file is expected to be locked
            for _ in range(30):
                time.sleep(0.1)
                if os.path.exists(smffile):
                    break
            else:
                raise TimeoutError("subprocess did not lock the file")

            # We should not be able to lock the file
            try:
                with nexus.File(filename, mode="r", locking=True):
                    pass
                raise RuntimeError("Locked exception not raises")
            except Exception as e:
                assert nexus.isLockedError(e), str(e)

            # Check that the locking error message mentions
            # the process that locked the file
            err_msg = nexus.lockedErrorMessage(filename)
            print(err_msg)
            parent_proc = psutil.Process(proc.pid)
            if str(parent_proc) not in err_msg:
                if not any(
                    (
                        str(child_proc) in err_msg
                        for child_proc in parent_proc.children(recursive=True)
                    )
                ):
                    if sys.platform == "win32":
                        return pytest.xfail(
                            "sometimes cannot find the locking process on windows"
                        )
                    assert f"pid={proc.pid}" in err_msg

            # We should be able to open the file without locking
            try:
                with nexus.File(filename) as f:
                    assert f["a"][()] == 10
            except Exception:
                if sys.platform == "win32":
                    return pytest.skip(
                        "disabling file locking does not work on windows"
                    )
                raise
        finally:
            proc.kill()


def test_nexus_locked_self(tmpdir):
    filename = str(tmpdir / "test.h5")
    with nexus.File(filename, mode="a", locking=True) as f1:
        f1["a"] = 10
        f1.flush()
        # We should be able to open the file with locking
        with nexus.File(filename, mode="r", locking=True) as f2:
            assert f2["a"][()] == 10


def test_dicttonx_structured_array(tmpdir):
    filename = str(tmpdir / "test.h5")
    data = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
    with nexus.File(filename, mode="w") as f:
        tree = {"empty": [], "data": data}
        nexus.dicttonx(tree, f)
    content = dictdump.nxtodict(filename)
    structures = content["data"]
    structures = [dict(zip(structures.dtype.names, x)) for x in structures]
    assert structures == data
