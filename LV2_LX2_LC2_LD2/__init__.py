# Embedded file name: c:\Jenkins\live\output\win_32_static\Release\python-bundle\MIDI Remote Scripts\LV2_LX2_LC2_LD2\__init__.py
import Live
from LV2_LX2_LC2_LD2 import LV2_LX2_LC2_LD2
from FaderfoxScript import FaderfoxScript

def create_instance(c_instance):
    return LV2_LX2_LC2_LD2(c_instance)