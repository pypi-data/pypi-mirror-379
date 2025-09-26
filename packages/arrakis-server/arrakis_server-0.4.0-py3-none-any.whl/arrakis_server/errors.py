# Copyright (c) 2025, California Institute of Technology and contributors
#
# You should have received a copy of the licensing terms for this
# software included in the file "LICENSE" located in the top-level
# directory of this package. If you did not, you can view a copy at
# https://git.ligo.org/ngdd/arrakis-server/-/raw/main/LICENSE

from collections.abc import Sequence

from pyarrow import flight


class TimeRangeUnavailableError(flight.FlightUnavailableError):
    def __init__(self, start: int, end: int):
        msg = f"time range requested ({start} - {end}) not available on this server"
        super().__init__(msg)


class ChannelUnavailableError(flight.FlightUnavailableError):
    def __init__(self, channels: Sequence[str]):
        msg = f"channels requested ({channels}) not available on this server"
        super().__init__(msg)


class RequestUnavailableError(flight.FlightUnavailableError):
    pass


class RequestCancelledError(flight.FlightCancelledError):
    pass


class RequestTimedOutError(flight.FlightTimedOutError):
    pass
