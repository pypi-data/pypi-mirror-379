"""Preprocessing Functions.

This module contains standalone functions for basic EEG signal processing
operations including filtering, resampling, referencing, and channel operations.

Functions
---------
filter_data : Apply digital filtering (highpass, lowpass, notch)
resample_data : Change sampling frequency
rereference_data : Apply referencing schemes
drop_channels : Remove channels from data
crop_data : Crop data to specific time range
trim_edges : Remove data from beginning and end
assign_channel_types : Set channel types (EEG, EOG, etc.)
"""

from .basic_ops import assign_channel_types, crop_data, drop_channels, trim_edges

# Import implemented functions
from .filtering import filter_data
from .referencing import rereference_data
from .resampling import resample_data
from .wavelet_thresholding import wavelet_threshold

__all__ = [
    "filter_data",
    "resample_data",
    "rereference_data",
    "drop_channels",
    "crop_data",
    "trim_edges",
    "assign_channel_types",
    "wavelet_threshold",
]
