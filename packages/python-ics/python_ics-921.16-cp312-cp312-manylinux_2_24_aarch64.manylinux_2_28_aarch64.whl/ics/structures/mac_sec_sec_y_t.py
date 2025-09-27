# This file was auto generated; Do not modify, if you value your sanity!
import ctypes
import enum



class Nameless8267(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ('index', ctypes.c_uint8),
        ('controlled_port_enabled', ctypes.c_uint8),
        ('validate_frames', ctypes.c_uint8),
        ('strip_sectag_icv', ctypes.c_uint8),
        ('cipher', ctypes.c_uint8),
        ('confidential_offset', ctypes.c_uint8),
        ('icv_includes_da_sa', ctypes.c_uint8),
        ('replay_protect', ctypes.c_uint8),
        ('replay_window', ctypes.c_uint32),
        ('protect_frames', ctypes.c_uint8),
        ('sectag_offset', ctypes.c_uint8),
        ('sectag_tci', ctypes.c_uint8),
        ('mtu', ctypes.c_uint16),
        ('rsvd', ctypes.c_uint8 * 6),
        ('enable', ctypes.c_uint8),
    ]



class mac_sec_sec_y_t(ctypes.Union):
    _pack_ = 1
    _anonymous_  = ('Nameless8267',)
    _fields_ = [
        ('Nameless8267', Nameless8267),
        ('byte', ctypes.c_uint8 * 24),
    ]


_MACSecSecY = mac_sec_sec_y_t
MACSecSecY_t = mac_sec_sec_y_t

