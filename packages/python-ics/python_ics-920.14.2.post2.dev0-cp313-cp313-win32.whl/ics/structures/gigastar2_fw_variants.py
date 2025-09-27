# This file was auto generated; Do not modify, if you value your sanity!
import ctypes
import enum



class gigastar2_fw_variants(enum.IntEnum):
    """A ctypes-compatible IntEnum superclass."""
    @classmethod
    def from_param(cls, obj):
        return int(obj)

    GIGASTAR2_FW_VARIANT_6T1S_1CAN_16LIN  = 0
    GIGASTAR2_FW_VARIANT_8T1S_4CAN_6LIN  = 1
    GIGASTAR2_FW_VARIANT_COUNT = enum.auto()


Gigastar2FwVariants = gigastar2_fw_variants

