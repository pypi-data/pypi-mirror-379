"""Classes and methods for location, elevation and azimuth for satellite modems.

Parses NMEA-0183 data into a `GnssLocation` object.
"""

import inspect
import json
import logging
from dataclasses import dataclass
from enum import IntEnum

from .utils import iso_to_ts, ts_to_iso


_log = logging.getLogger(__name__)


class GnssFixType(IntEnum):
    """Enumerated fix type from NMEA-0183 standard."""
    NONE = 1
    FIX_2D = 2
    FIX_3D = 3


class GnssFixQuality(IntEnum):
    """Enumerated fix quality from NMEA-0183 standard."""
    INVALID = 0
    GPS_SPS = 1
    DGPS = 2
    PPS = 3
    RTK = 4
    FLOAT_RTK = 5
    EST_DEAD_RECKONING = 6
    MANUAL = 7
    SIMULATION = 8


@dataclass
class GnssSatelliteInfo(object):
    """Information specific to a GNSS satellite.
    
    Attributes:
        prn: The PRN code (Pseudo-Random Number sequence)
        elevation: The satellite elevation
        azimuth: The satellite azimuth
        snr: The satellite Signal-to-Noise Ratio
    """
    prn: int
    elevation: int
    azimuth: int
    snr: int


def validate_nmea(nmea_sentence: str) -> bool:
    """Validates a given NMEA-0183 sentence with CRC.
    
    Args:
        nmea_sentence (str): NMEA-0183 sentence ending in checksum.
    
    """
    if '*' not in nmea_sentence:
        return False
    data, cs_hex = nmea_sentence.split('*')
    candidate = int(cs_hex, 16)
    crc = 0   # initial
    for i in range(1, len(data)):   # ignore initial $
        crc ^= ord(data[i])
    return candidate == crc


class GnssLocation:
    """A set of location-based information derived from the modem's NMEA data.
    
    Uses 90.0/180.0 and timestamp 0 if latitude/longitude are unknown.

    Attributes:
        latitude (float): decimal degrees
        longitude (float): decimal degrees
        altitude (float): in metres
        speed (float): in km/h
        heading (float): in degrees
        timestamp (int): in seconds since 1970-01-01T00:00:00Z
        satellites (int): in view at time of fix
        fix_type (GnssFixType): 1=None, 2=2D or 3=3D
        fix_quality (GnssFixQuality): Enumerated lookup value
        pdop (float): Probability Dilution of Precision
        hdop (float): Horizontal Dilution of Precision
        vdop (float): Vertical Dilution of Precision
        time_iso (str): ISO 8601 formatted timestamp

    """
    __slots__ = ('latitude', 'longitude', 'altitude', 'speed', 'heading',
                 'timestamp', 'satellites', 'fix_type', 'fix_quality',
                 'pdop', 'hdop', 'vdop',)
    
    def __init__(self, **kwargs):
        """Initializes a Location with default latitude/longitude 90/180."""
        self.latitude = float(kwargs.get('latitude', 90.0))
        self.longitude = float(kwargs.get('longitude', 180.0))
        self.altitude = float(kwargs.get('altitude', 0.0))   # metres
        self.speed = float(kwargs.get('speed', 0.0))  # knots
        self.heading = float(kwargs.get('heading', 0.0))   # degrees
        self.timestamp = int(kwargs.get('timestamp', 0))   # seconds (unix)
        self.satellites = int(kwargs.get('satellites', 0))
        self.fix_type = GnssFixType(int(kwargs.get('fix_type', 1)))
        self.fix_quality = GnssFixQuality(int(kwargs.get('fix_quality', 0)))
        self.pdop = float(kwargs.get('pdop', 99))
        self.hdop = float(kwargs.get('hdop', 99))
        self.vdop = float(kwargs.get('vdop', 99))

    @property
    def time_iso(self) -> str:
        return f'{ts_to_iso(self.timestamp)}'

    def __str__(self) -> str:
        obj = {s: getattr(self, s) for s in self.__slots__
               if not s.startswith('_') and not callable(getattr(self, s))}
        for prop, _ in inspect.getmembers(self.__class__,
                                          lambda o: isinstance(o, property)):
            if not prop.startswith('_'):
                try:
                    val = getattr(self, prop)
                    if not callable(val):
                        obj[prop] = val
                except Exception:
                    pass
        for k, v in obj.items():
            if k in ['latitude', 'longitude']:
                obj[k] = round(v, 5)
            elif isinstance(v, float):
                obj[k] = round(v, 1)
            elif isinstance(v, IntEnum):
                obj[k] = v.name
        return json.dumps(obj, skipkeys=True)
    
    def is_valid(self) -> bool:
        """Check validity."""
        if self.latitude < -90 or self.latitude > 90:
            return False
        if self.longitude < -180 or self.longitude > 180:
            return False
        if self.latitude == 90 and self.longitude == 180 and self.timestamp == 0:
            return False
        if self.fix_type == GnssFixType.NONE:
            return False
        if self.fix_quality == GnssFixQuality.INVALID:
            return False
        return True
    
    def parse_nmea(self, nmea_sentence: str):
        """Update the location with information derived from an NMEA sentence.
        
        Args:
            nmea_sentence (str): The NMEA-0183 sentence to parse.
        """
        if not validate_nmea(nmea_sentence):
            raise ValueError('Invalid NMEA-0183 sentence')
        void_fix = False
        data = nmea_sentence.rsplit('*', 1)[0]
        fields = data.split(',')
        nmea_type = fields[0][-3:]
        
        def _parse_rmc(fields):
            nonlocal void_fix
            cache = {}
            try:
                # Time
                hh, mm, ss = fields[1][0:2], fields[1][2:4], fields[1][4:6]
                cache.update({'fix_hour': hh, 'fix_min': mm, 'fix_sec': ss})
                # Status
                if fields[2] == 'V':
                    void_fix = True
                    return
                # Latitude
                if fields[3]:
                    lat = float(fields[3][0:2]) + float(fields[3][2:]) / 60.0
                    if fields[4] == 'S':
                        lat *= -1
                    self.latitude = round(lat, 6)
                # Longitude
                if fields[5]:
                    lon = float(fields[5][0:3]) + float(fields[5][3:]) / 60.0
                    if fields[6] == 'W':
                        lon *= -1
                    self.longitude = round(lon, 6)
                # Speed in km/h
                if fields[7]:
                    self.speed = round(float(fields[7]) * 1.852, 2)
                # Heading
                if fields[8]:
                    self.heading = float(fields[8])
                # Date → timestamp
                if fields[9]:
                    day, month, yy = int(fields[9][0:2]), int(fields[9][2:4]), int(fields[9][4:])
                    yy += 1900 if yy >= 73 else 2000
                    iso_time = f"{yy}-{month:02}-{day:02}T{hh}:{mm}:{ss}Z"
                    self.timestamp = int(iso_to_ts(iso_time))
            except Exception as e:
                _log.warning("Failed parsing RMC fields: %s", e)

        def _parse_gga(fields):
            try:
                # Latitude
                if fields[2]:
                    lat = float(fields[2][0:2]) + float(fields[2][2:]) / 60.0
                    if fields[3] == 'S':
                        lat *= -1
                    self.latitude = round(lat, 6)
                # Longitude
                if fields[4]:
                    lon = float(fields[4][0:3]) + float(fields[4][3:]) / 60.0
                    if fields[5] == 'W':
                        lon *= -1
                    self.longitude = round(lon, 6)
                # Fix quality
                self.fix_quality = GnssFixQuality(int(fields[6] or 0))
                # Satellites
                if fields[7]:
                    self.satellites = int(fields[7])
                # HDOP
                if fields[8]:
                    self.hdop = round(float(fields[8]), 1)
                # Altitude
                if fields[9]:
                    self.altitude = float(fields[9])
            except Exception as e:
                _log.warning("Failed parsing GGA fields: %s", e)

        def _parse_gsa(fields):
            try:
                # Fix type
                if fields[2]:
                    self.fix_type = GnssFixType(int(fields[2] or 0))
                # PDOP, HDOP, VDOP
                if len(fields) > 15 and fields[15]:
                    self.pdop = round(float(fields[15]), 1)
                if len(fields) > 17 and fields[17]:
                    self.vdop = round(float(fields[17]), 1)
            except Exception as e:
                _log.warning("Failed parsing GSA fields: %s", e)
                    
        _log.debug('Parsing NMEA: %s', nmea_sentence)
        if nmea_type == 'RMC':
            _parse_rmc(fields)
        elif nmea_type == 'GGA':
            _parse_gga(fields)
        elif nmea_type == 'GSA':
            _parse_gsa(fields)
        else:
            _log.debug('Unsupported NMEA sentence type: %s', nmea_type)
    
    @classmethod
    def from_nmea_list(cls, nmea_list: list[str]) -> 'GnssLocation':
        """Create a GnssLocation from a list of NMEA-0183 sentences."""
        if (not isinstance(nmea_list, list) or
            not all(isinstance(s, str) for s in nmea_list)):
            raise ValueError('Invalid list or sentences in list')
        loc = GnssLocation()
        for sentence in nmea_list:
            loc.parse_nmea(sentence)
        return loc
