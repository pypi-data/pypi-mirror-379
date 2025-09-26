from ctypes import c_uint

nInterfaceNum   = c_uint(0)
nTriggerMode    = c_uint(0)
TRIGGER_MODE_ON = c_uint(1)
TRIGGER_MODE_OFF = c_uint(0)

MONO8 = 0x01080001
MONO10 = 0x01100003
MONO12 = 0x01100005


TRIGGER_SOURCE_LINE0 = c_uint(0)                     # ch:Line0 | en:Line0
TRIGGER_SOURCE_LINE1 = c_uint(1)                     # ch:Line1 | en:Line1
TRIGGER_SOURCE_LINE2 = c_uint(2)                     # ch:Line2 | en:Line2
TRIGGER_SOURCE_LINE3 = c_uint(3)                     # ch:Line3 | en:Line3
TRIGGER_SOURCE_COUNTER0 = c_uint(4)                  # ch:Conuter0 | en:Conuter0
TRIGGER_SOURCE_SOFTWARE = c_uint(7)                  # ch:软触发 | en:Software
TRIGGER_SOURCE_FrequencyConverter = c_uint(8)        # ch:变频器 | en:Frequency Converter