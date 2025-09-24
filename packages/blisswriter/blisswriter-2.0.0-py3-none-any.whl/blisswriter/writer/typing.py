from __future__ import annotations

from typing import Union
from collections.abc import Sequence

import numpy

NumericDataType = Sequence[numpy.ndarray]
"""numpy array or a list of numpy arrays (ragged data like diode samples)
"""

LimaStatusType = Sequence[dict]

ScanReferenceType = Sequence[dict]

ChannelDataType = Union[NumericDataType, LimaStatusType, ScanReferenceType]
