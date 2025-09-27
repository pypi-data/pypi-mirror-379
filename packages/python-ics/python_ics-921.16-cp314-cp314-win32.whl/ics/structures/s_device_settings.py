# This file was auto generated; Do not modify, if you value your sanity!
import ctypes
import enum

from ics.structures.e_device_settings_type import *
from ics.structures.s_cyan_settings import *
from ics.structures.s_fire3_flexray_settings import *
from ics.structures.s_fire3_settings import *
from ics.structures.s_fire_settings import *
from ics.structures.s_fire_vnet_settings import *
from ics.structures.s_flex_vnetz_settings import *
from ics.structures.s_neo_ecu12_settings import *
from ics.structures.s_neo_vi_connect_settings import *
from ics.structures.s_pendant_settings import *
from ics.structures.s_red2_settings import *
from ics.structures.s_red_settings import *
from ics.structures.s_vivid_can_settings import *
from ics.structures.scan_hub_settings import *
from ics.structures.secu_settings import *
from ics.structures.sobd2_lc_settings import *
from ics.structures.srad_comet3_settings import *
from ics.structures.srad_comet_settings import *
from ics.structures.srad_epsilon_settings import *
from ics.structures.srad_galaxy2_settings import *
from ics.structures.srad_galaxy_settings import *
from ics.structures.srad_gigastar2_settings import *
from ics.structures.srad_gigastar_settings import *
from ics.structures.srad_jupiter_settings import *
from ics.structures.srad_moon2_settings import *
from ics.structures.srad_moon3_settings import *
from ics.structures.srad_moon_t1_s_settings import *
from ics.structures.srad_star2_settings import *
from ics.structures.srada2_b_settings import *
from ics.structures.sradbms_settings import *
from ics.structures.svcan3_settings import *
from ics.structures.svcan412_settings import *
from ics.structures.svcan4_ind_settings import *
from ics.structures.svcan4_settings import *


class Settings(ctypes.Union):
    _pack_ = 2
    _fields_ = [
        ('red', SRedSettings),
        ('fire', SFireSettings),
        ('firevnet', SFireVnetSettings),
        ('cyan', SCyanSettings),
        ('vcan3', SVCAN3Settings),
        ('vcan4', SVCAN4Settings),
        ('ecu', SECUSettings),
        ('pendant', SPendantSettings),
        ('radgalaxy', SRADGalaxySettings),
        ('radstar2', SRADStar2Settings),
        ('vcan412', SVCAN412Settings),
        ('vcan4_12', SVCAN412Settings),
        ('radmoon2', SRADMoon2Settings),
        ('canhub', SCANHubSettings),
        ('neoecu12', SNeoECU12Settings),
        ('flexvnetz', SFlexVnetzSettings),
        ('vividcan', SVividCANSettings),
        ('vcan4_ind', SVCAN4IndSettings),
        ('obd2lc', SOBD2LCSettings),
        ('radgigastar', SRADGigastarSettings),
        ('radGalaxy2', SRADGalaxy2Settings),
        ('jupiter', SRADJupiterSettings),
        ('fire3', SFire3Settings),
        ('red2', SRed2Settings),
        ('rad_a2b', SRADA2BSettings),
        ('epsilon', SRADEpsilonSettings),
        ('rad_bms', SRADBMSSettings),
        ('radmoon3', SRADMoon3Settings),
        ('fire3Flexray', SFire3FlexraySettings),
        ('radcomet', SRADCometSettings),
        ('radcomet3', SRADComet3Settings),
        ('radgigastar2', SRADGigastar2Settings),
        ('radmoont1s', SRADMoonT1SSettings),
        ('neovi_connect', SNeoVIConnectSettings),
    ]



class s_device_settings(ctypes.Structure):
    _pack_ = 2
    _fields_ = [
        ('DeviceSettingType', ctypes.c_int32),
        ('Settings', Settings),
    ]


_SDeviceSettings = s_device_settings
SDeviceSettings = s_device_settings

