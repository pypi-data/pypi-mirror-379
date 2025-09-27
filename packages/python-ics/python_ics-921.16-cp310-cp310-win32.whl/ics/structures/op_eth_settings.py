# This file was auto generated; Do not modify, if you value your sanity!
import ctypes
import enum



class Nameless8987(ctypes.Structure):
    _pack_ = 2
    _fields_ = [
        ('mac_addr1', ctypes.c_uint8 * 6),
        ('mac_addr2', ctypes.c_uint8 * 6),
        ('mac_spoofing_en', ctypes.c_uint16, 1),
        ('mac_spoofing_isDstOrSrc', ctypes.c_uint16, 1),
        ('link_spd', ctypes.c_uint16, 2),
        ('q2112_phy_mode', ctypes.c_uint16, 1),
        ('macsec_en', ctypes.c_uint16, 1),
        ('compliance_mode_en', ctypes.c_uint16, 1),
        ('cut_thru_tap', ctypes.c_uint16, 1),
        ('snf_tap', ctypes.c_uint16, 1),
        ('disable_tap_to_host', ctypes.c_uint16, 1),
        ('show_tap_tx_receipt', ctypes.c_uint16, 1),
        ('reserved', ctypes.c_uint16, 5),
    ]



class Nameless11656(ctypes.Union):
    _pack_ = 2
    _anonymous_  = ('Nameless8987',)
    _fields_ = [
        ('Nameless8987', Nameless8987),
        ('reserved0', ctypes.c_uint8 * 14),
    ]



class op_eth_settings(ctypes.Structure):
    _pack_ = 2
    _anonymous_  = ('Nameless11656',)
    _fields_ = [
        ('ucConfigMode', ctypes.c_uint8),
        ('preemption_en', ctypes.c_uint8),
        ('Nameless11656', Nameless11656),
    ]


OP_ETH_SETTINGS_t = op_eth_settings
OP_ETH_SETTINGS = op_eth_settings

