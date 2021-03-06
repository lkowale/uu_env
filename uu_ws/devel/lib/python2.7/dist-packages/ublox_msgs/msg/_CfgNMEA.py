# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ublox_msgs/CfgNMEA.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class CfgNMEA(genpy.Message):
  _md5sum = "9d53bb6c49d53481b2a181d8ed0bed23"
  _type = "ublox_msgs/CfgNMEA"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# CFG-NMEA (0x06 0x17)
# NMEA protocol configuration V1
#
# Set/Get the NMEA protocol configuration. See section NMEA Protocol 
# Configuration for a detailed description of the configuration effects on 
# NMEA output
#

uint8 CLASS_ID = 6
uint8 MESSAGE_ID = 23 

uint8 filter                  # filter flags
uint8 FILTER_POS = 1          # Enable position output for failed or 
                              # invalid fixes
uint8 FILTER_MSK_POS = 2      # Enable position output for invalid fixes
uint8 FILTER_TIME = 4         # Enable time output for invalid times
uint8 FILTER_DATE = 8         # Enable date output for invalid dates
uint8 FILTER_GPS_ONLY = 16    # Restrict output to GPS satellites only
uint8 FILTER_TRACK = 32       # Enable COG output even if COG is frozen

uint8 nmeaVersion             # NMEA version
uint8 NMEA_VERSION_4_1 = 65     # Version 4.1
uint8 NMEA_VERSION_4_0 = 64     # Version 4.0
uint8 NMEA_VERSION_2_3 = 35     # Version 2.3
uint8 NMEA_VERSION_2_1 = 33     # Version 2.1

uint8 numSV                   # Maximum Number of SVs to report per TalkerId: 
                              # unlimited (0) or 8, 12, 16
uint8 NUM_SV_UNLIMITED = 0 

uint8 flags                   # flags
uint8 FLAGS_COMPAT = 1          # enable compatibility mode.
                                # This might be needed for certain applications  
                                # when customer's NMEA parser expects a fixed 
                                # number of  digits in position coordinates
uint8 FLAGS_CONSIDER = 2        # enable considering mode
uint8 FLAGS_LIMIT82 = 4         # enable strict limit to 82 characters maximum
uint8 FLAGS_HIGH_PREC = 8       # enable high precision mode
                                # This flag cannot be set in conjunction with  
                                # either Compatibility Mode or Limit82 Mode.
                                # (not supported in protocol versions < 20.01)

uint32 gnssToFilter           # Filters out satellites based on their GNSS.  
                              # If a bitfield is enabled, the corresponding 
                              # satellites will be not output.
uint32 GNSS_TO_FILTER_GPS = 1       # Disable reporting of GPS satellites
uint32 GNSS_TO_FILTER_SBAS = 2      # Disable reporting of SBAS satellites
uint32 GNSS_TO_FILTER_QZSS = 16     # Disable reporting of QZSS satellites
uint32 GNSS_TO_FILTER_GLONASS = 32  # Disable reporting of GLONASS satellites
uint32 GNSS_TO_FILTER_BEIDOU = 64   # Disable reporting of BeiDou satellites

uint8 svNumbering             # Configures the display of satellites that do not  
                              # have an NMEA-defined value. Note: this does not
                              # apply to satellites with an unknown ID.
uint8 SV_NUMBERING_STRICT = 0     # Strict - Satellites are not output
uint8 SV_NUMBERING_EXTENDED = 1   # Extended - Use proprietary numbering

uint8 mainTalkerId            # By default the main Talker ID (i.e. the Talker 
                              # ID used  for all messages other than GSV) is 
                              # determined by the  GNSS assignment of the 
                              # receiver's channels (see CfgGNSS). 
                              # This field enables the main Talker ID to be 
                              # overridden
uint8 MAIN_TALKER_ID_NOT_OVERRIDDEN = 0   # Main Talker ID is not overridden
uint8 MAIN_TALKER_ID_GP = 1               # Set main Talker ID to 'GP'
uint8 MAIN_TALKER_ID_GL = 2               # Set main Talker ID to 'GL'
uint8 MAIN_TALKER_ID_GN = 3               # Set main Talker ID to 'GN'
uint8 MAIN_TALKER_ID_GA = 4               # Set main Talker ID to 'GA'
uint8 MAIN_TALKER_ID_GB = 5               # Set main Talker ID to 'GB'

uint8 gsvTalkerId             # By default the Talker ID for GSV messages is  
                              # GNSS specific (as defined by NMEA). This field 
                              # enables the GSV Talker ID to be overridden.
uint8 GSV_TALKER_ID_GNSS_SPECIFIC = 0   # Use GNSS specific Talker ID 
                                        # (as defined by NMEA)
uint8 GSV_TALKER_ID_MAIN = 1            # Use the main Talker ID

uint8 version                 # Message version (set to 1 for this version)
uint8 VERSION = 1

uint8[2] bdsTalkerId          # Sets the two characters that should be used 
                              # for the BeiDou Talker ID. If these are set to 
                              # zero, the default BeiDou TalkerId will be used

uint8[6] reserved1            # Reserved"""
  # Pseudo-constants
  CLASS_ID = 6
  MESSAGE_ID = 23
  FILTER_POS = 1
  FILTER_MSK_POS = 2
  FILTER_TIME = 4
  FILTER_DATE = 8
  FILTER_GPS_ONLY = 16
  FILTER_TRACK = 32
  NMEA_VERSION_4_1 = 65
  NMEA_VERSION_4_0 = 64
  NMEA_VERSION_2_3 = 35
  NMEA_VERSION_2_1 = 33
  NUM_SV_UNLIMITED = 0
  FLAGS_COMPAT = 1
  FLAGS_CONSIDER = 2
  FLAGS_LIMIT82 = 4
  FLAGS_HIGH_PREC = 8
  GNSS_TO_FILTER_GPS = 1
  GNSS_TO_FILTER_SBAS = 2
  GNSS_TO_FILTER_QZSS = 16
  GNSS_TO_FILTER_GLONASS = 32
  GNSS_TO_FILTER_BEIDOU = 64
  SV_NUMBERING_STRICT = 0
  SV_NUMBERING_EXTENDED = 1
  MAIN_TALKER_ID_NOT_OVERRIDDEN = 0
  MAIN_TALKER_ID_GP = 1
  MAIN_TALKER_ID_GL = 2
  MAIN_TALKER_ID_GN = 3
  MAIN_TALKER_ID_GA = 4
  MAIN_TALKER_ID_GB = 5
  GSV_TALKER_ID_GNSS_SPECIFIC = 0
  GSV_TALKER_ID_MAIN = 1
  VERSION = 1

  __slots__ = ['filter','nmeaVersion','numSV','flags','gnssToFilter','svNumbering','mainTalkerId','gsvTalkerId','version','bdsTalkerId','reserved1']
  _slot_types = ['uint8','uint8','uint8','uint8','uint32','uint8','uint8','uint8','uint8','uint8[2]','uint8[6]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       filter,nmeaVersion,numSV,flags,gnssToFilter,svNumbering,mainTalkerId,gsvTalkerId,version,bdsTalkerId,reserved1

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CfgNMEA, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.filter is None:
        self.filter = 0
      if self.nmeaVersion is None:
        self.nmeaVersion = 0
      if self.numSV is None:
        self.numSV = 0
      if self.flags is None:
        self.flags = 0
      if self.gnssToFilter is None:
        self.gnssToFilter = 0
      if self.svNumbering is None:
        self.svNumbering = 0
      if self.mainTalkerId is None:
        self.mainTalkerId = 0
      if self.gsvTalkerId is None:
        self.gsvTalkerId = 0
      if self.version is None:
        self.version = 0
      if self.bdsTalkerId is None:
        self.bdsTalkerId = b'\0'*2
      if self.reserved1 is None:
        self.reserved1 = b'\0'*6
    else:
      self.filter = 0
      self.nmeaVersion = 0
      self.numSV = 0
      self.flags = 0
      self.gnssToFilter = 0
      self.svNumbering = 0
      self.mainTalkerId = 0
      self.gsvTalkerId = 0
      self.version = 0
      self.bdsTalkerId = b'\0'*2
      self.reserved1 = b'\0'*6

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_4BI4B().pack(_x.filter, _x.nmeaVersion, _x.numSV, _x.flags, _x.gnssToFilter, _x.svNumbering, _x.mainTalkerId, _x.gsvTalkerId, _x.version))
      _x = self.bdsTalkerId
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_2B().pack(*_x))
      else:
        buff.write(_get_struct_2s().pack(_x))
      _x = self.reserved1
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_6B().pack(*_x))
      else:
        buff.write(_get_struct_6s().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.filter, _x.nmeaVersion, _x.numSV, _x.flags, _x.gnssToFilter, _x.svNumbering, _x.mainTalkerId, _x.gsvTalkerId, _x.version,) = _get_struct_4BI4B().unpack(str[start:end])
      start = end
      end += 2
      self.bdsTalkerId = str[start:end]
      start = end
      end += 6
      self.reserved1 = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_4BI4B().pack(_x.filter, _x.nmeaVersion, _x.numSV, _x.flags, _x.gnssToFilter, _x.svNumbering, _x.mainTalkerId, _x.gsvTalkerId, _x.version))
      _x = self.bdsTalkerId
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_2B().pack(*_x))
      else:
        buff.write(_get_struct_2s().pack(_x))
      _x = self.reserved1
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_6B().pack(*_x))
      else:
        buff.write(_get_struct_6s().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.filter, _x.nmeaVersion, _x.numSV, _x.flags, _x.gnssToFilter, _x.svNumbering, _x.mainTalkerId, _x.gsvTalkerId, _x.version,) = _get_struct_4BI4B().unpack(str[start:end])
      start = end
      end += 2
      self.bdsTalkerId = str[start:end]
      start = end
      end += 6
      self.reserved1 = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2B = None
def _get_struct_2B():
    global _struct_2B
    if _struct_2B is None:
        _struct_2B = struct.Struct("<2B")
    return _struct_2B
_struct_2s = None
def _get_struct_2s():
    global _struct_2s
    if _struct_2s is None:
        _struct_2s = struct.Struct("<2s")
    return _struct_2s
_struct_4BI4B = None
def _get_struct_4BI4B():
    global _struct_4BI4B
    if _struct_4BI4B is None:
        _struct_4BI4B = struct.Struct("<4BI4B")
    return _struct_4BI4B
_struct_6B = None
def _get_struct_6B():
    global _struct_6B
    if _struct_6B is None:
        _struct_6B = struct.Struct("<6B")
    return _struct_6B
_struct_6s = None
def _get_struct_6s():
    global _struct_6s
    if _struct_6s is None:
        _struct_6s = struct.Struct("<6s")
    return _struct_6s
