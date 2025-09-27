# This file was auto generated; Do not modify, if you value your sanity!
import ctypes
import enum



class Nameless11965(ctypes.Structure):
    _pack_ = 2
    _fields_ = [
        ('tap1ToVspy', ctypes.c_uint8, 1),
        ('tap2ToVspy', ctypes.c_uint8, 1),
        ('tap3ToVspy', ctypes.c_uint8, 1),
        ('tap4ToVspy', ctypes.c_uint8, 1),
        ('tap5ToVspy', ctypes.c_uint8, 1),
        ('tap6ToVspy', ctypes.c_uint8, 1),
        ('tap7ToVspy', ctypes.c_uint8, 1),
        ('tap8ToVspy', ctypes.c_uint8, 1),
    ]



class Nameless23998(ctypes.Union):
    _pack_ = 2
    _anonymous_  = ('Nameless11965',)
    _fields_ = [
        ('tapPairOpt', ctypes.c_uint8),
        ('Nameless11965', Nameless11965),
    ]



class flags(ctypes.Structure):
    _pack_ = 2
    _fields_ = [
        ('bTapEnSwitch', ctypes.c_uint32, 1),
        ('bTapEnPtp', ctypes.c_uint32, 1),
        ('bEnReportLinkQuality', ctypes.c_uint32, 1),
        ('bEnTapTxReceipts', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 28),
    ]



class Nameless14996(ctypes.Union):
    _pack_ = 2
    _fields_ = [
        ('flags', flags),
        ('uFlags', ctypes.c_uint32),
    ]



class op_eth_general_settings(ctypes.Structure):
    _pack_ = 2
    _anonymous_  = ('Nameless23998', 'Nameless14996')
    _fields_ = [
        ('ucInterfaceType', ctypes.c_uint8),
        ('Nameless23998', Nameless23998),
        ('reserved0', ctypes.c_uint8 * 2),
        ('tapPair0', ctypes.c_uint16),
        ('tapPair1', ctypes.c_uint16),
        ('tapPair2', ctypes.c_uint16),
        ('tapPair3', ctypes.c_uint16),
        ('tapPair4', ctypes.c_uint16),
        ('tapPair5', ctypes.c_uint16),
        ('Nameless14996', Nameless14996),
    ]


OP_ETH_GENERAL_SETTINGS_t = op_eth_general_settings
OP_ETH_GENERAL_SETTINGS = op_eth_general_settings

