import logging
from os.path import dirname, abspath, join

from .constants import *
from .exceptions import *
from .daterange import *
from .earliest_datetime import *
from .get_CMR_granule_ID import *
from .HLS_CMR_query import *
from .HLS_granule_ID import *
from .HLS2_landsat_granule import *
from .HLS2_sentinel_granule import *
from .HLS2_granule import *
from .HLS2_landsat_granule import *
from .HLS2_sentinel_granule import *
from .HLS2_connection import *
from .latest_datetime import *
from .timer import *
from .timeseries import *
from .login import *

with open(join(abspath(dirname(__file__)), "version.txt")) as f:
    version = f.read()

__version__ = version
__author__ = "Gregory H. Halverson, Evan Davis"

logger = logging.getLogger(__name__)

try:
    harmonized_landsat_sentinel = HLS2Connection()
except Exception as e:
    logging.warning(f"Failed to initialize HLS2EarthAccessConnection: {e}")
    harmonized_landsat_sentinel = None
