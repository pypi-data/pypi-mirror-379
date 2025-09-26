from datetime import date
import logging

from dateutil.rrule import rrule, DAILY

from rasters import RasterGeometry

import colored_logging as cl

from harmonized_landsat_sentinel import HLS2Connection

from harmonized_landsat_sentinel import (
    HLSTileNotAvailable,
    HLSSentinelNotAvailable,
    HLSLandsatNotAvailable,
    HLSDownloadFailed,
    HLSNotAvailable,
)

from ECOv003_exit_codes import *

from .daterange import get_date
from .VNP43NRT import VNP43NRT

logger = logging.getLogger(__name__)

def retrieve_STARS_sources(
    tile: str,
    geometry: RasterGeometry,
    HLS_start_date: date,
    HLS_end_date: date,
    VIIRS_start_date: date,
    VIIRS_end_date: date,
    HLS_connection: HLS2Connection,
    VIIRS_connection: VNP43NRT):
    """
    Retrieves necessary Harmonized Landsat Sentinel (HLS) and VIIRS source data.

    This function downloads HLS Sentinel and Landsat data, and prefetches VIIRS VNP09GA
    data for the specified tile and date ranges. It includes error handling for
    download failures and data unavailability.

    Args:
        tile (str): The HLS tile ID.
        geometry (RasterGeometry): The spatial geometry of the area of interest.
        HLS_start_date (date): The start date for HLS data retrieval.
        HLS_end_date (date): The end date for HLS data retrieval.
        VIIRS_start_date (date): The start date for VIIRS data retrieval.
        VIIRS_end_date (date): The end date for VIIRS data retrieval.
        HLS_connection (HLS2Connection): An initialized HLS data connection object.
        VIIRS_connection (VNP43NRT): An initialized VIIRS data connection object
                                      (can be VNP43NRT, VNP43IA4, or VNP43MA3).

    Raises:
        DownloadFailed: If an HLS download fails.
        AuxiliaryLatency: If HLS data for a given tile/date is not available (latency issue).
    """
    logger.info(
        f"Retrieving HLS sources for tile {cl.place(tile)} from {cl.time(HLS_start_date)} to {cl.time(HLS_end_date)}"
    )
    # Iterate through each day in the HLS date range to retrieve Sentinel and Landsat data
    for processing_date in [
        get_date(dt) for dt in rrule(DAILY, dtstart=HLS_start_date, until=HLS_end_date)
    ]:
        try:
            logger.info(
                f"Retrieving HLS Sentinel at tile {cl.place(tile)} on date {cl.time(processing_date)}"
            )
            # Attempt to download HLS Sentinel data
            HLS_connection.sentinel(tile=tile, date_UTC=processing_date)
            logger.info(
                f"Retrieving HLS Landsat at tile {cl.place(tile)} on date {cl.time(processing_date)}"
            )
            # Attempt to download HLS Landsat data
            HLS_connection.landsat(tile=tile, date_UTC=processing_date)
        except HLSDownloadFailed as e:
            logger.exception(e)
            raise AuxiliaryDownloadFailed(e)
        except (
            HLSTileNotAvailable,
            HLSSentinelNotAvailable,
            HLSLandsatNotAvailable,
        ) as e:
            # Log warnings for data not being available, but continue processing
            logger.warning(e)
        except Exception as e:
            # Catch other unexpected exceptions during HLS retrieval
            logger.warning("Exception raised while retrieving HLS tiles")
            logger.exception(e)
            continue  # Continue to the next date even if one HLS retrieval fails

    logger.info(
        f"Retrieving VIIRS sources for tile {cl.place(tile)} from {cl.time(VIIRS_start_date)} to {cl.time(VIIRS_end_date)}"
    )
    # Prefetch VNP09GA data for the specified VIIRS date range and geometry
    VIIRS_connection.prefetch_VNP09GA(
        start_date=VIIRS_start_date,
        end_date=VIIRS_end_date,
        geometry=geometry,
    )
