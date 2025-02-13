"""This logging module is designed for pytest logging and log capturing. It includes:

Custom log formatters (colorized logs, date formatting, multi-line handling).
Integration with pytest hooks (e.g., pytest_runtest_setup, pytest_sessionfinish).
Options for logging to files, CLI, and live logging.
"""


import logging
from collections.abc import Mapping
from datetime import timezone, timedelta, datetime
from logging import LogRecord

default_log_format="%(levelname)-8s %(name)s:%(filename)s:%(lineno)d %(message)s"
default_log_date_format= "%H:%M:%S"

class datatime_formatter(logging.Formatter):

    def formatTime(self, record: LogRecord, datefmt: str | None = None) -> str:
        if datefmt and "%f" in datefmt: #checks if the data format is provided and it contains micro seconds(%f)

            #step1: convert log record timestamp
            ct=self.converter(record.created)  #ct--- convert time to human redable time
                                #record.created → A floating-point UNIX timestamp (epoch time) indicating when the log was created.
                                #self.converter(record.created) → Converts this timestamp to a structured time (struct_time),
                                #time.struct_time(tm_year=2025, tm_mon=2, tm_mday=12, tm_hour=16, tm_min=24, tm_sec=58, tm_wday=2, tm_yday=43, tm_isdst=0)

            #step2: extract time zone information
            tz=timezone(timedelta(ct.tm_gmtoff),ct.tm_zone)
            # Construct `datetime.datetime` object from `struct_time`
            # and msecs informat    ion from `record`
            # Using int() instead of round() to avoid it exceeding 1_000_000 and causing a ValueError (#11861).
            dt = datetime(*ct[0:6], microsecond=int(record.msecs * 1000), tzinfo=tz)
            return dt.strftime(datefmt)
            # Use `logging.Formatter` for non-microsecond formats
        return super().formatTime(record, datefmt)


class log_capture_handler(logging.StreamHandler):
    """custom """