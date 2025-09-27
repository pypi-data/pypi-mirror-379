# This file was auto generated; Do not modify, if you value your sanity!
import ctypes
import enum



class phy_id(enum.IntEnum):
    """A ctypes-compatible IntEnum superclass."""
    @classmethod
    def from_param(cls, obj):
        return int(obj)

    PHY_88Q211x_Z1  = 0
    PHY_88Q211x_A0  = 1
    PHY_88Q211x_A1  = 2
    PHY_88Q211x_A2  = 3
    PHY_88Q222xM_A0  = 4
    PHY_88Q222xM_B0  = 5
    PHY_88Q222xM_B1  = 6
    PHY_88Q222xM_B2  = 7
    PHY_UNKNOWN  = 255


PhyId = phy_id

