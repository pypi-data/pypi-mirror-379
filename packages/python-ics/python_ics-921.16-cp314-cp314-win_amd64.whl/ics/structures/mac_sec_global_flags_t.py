# This file was auto generated; Do not modify, if you value your sanity!
import ctypes
import enum



class Nameless34924(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ('en', ctypes.c_uint32, 1),
        ('nvm', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]



class mac_sec_global_flags_t(ctypes.Union):
    _pack_ = 1
    _anonymous_  = ('Nameless34924',)
    _fields_ = [
        ('Nameless34924', Nameless34924),
        ('flags_32b', ctypes.c_uint32),
    ]


_MACSecGlobalFlags = mac_sec_global_flags_t
MACSecGlobalFlags_t = mac_sec_global_flags_t

