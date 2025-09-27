# Copyright (c) 2022, California Institute of Technology and contributors
#
# You should have received a copy of the licensing terms for this
# software included in the file "LICENSE" located in the top-level
# directory of this package. If you did not, you can view a copy at
# https://git.ligo.org/ngdd/arrakis-server/-/raw/main/LICENSE

import logging
import threading
from collections.abc import Iterable, Iterator
from functools import wraps
from urllib.parse import urlparse

import numpy
import pyarrow
from arrakis import SeriesBlock
from arrakis.flight import RequestType, RequestValidator, create_command, parse_command
from pyarrow import flight

from . import arrow, constants, schemas, traits
from .channel import Channel
from .scope import ScopeMap

logger = logging.getLogger("arrakis")


def exception_catcher(func):
    """decorator to catch uncaught exceptions in FlightServer

    The exception is logged and a FlightInternalError is raised for
    the client.

    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except flight.FlightError:
            raise
        except Exception:
            logger.exception(
                "internal server error: %s, %s, %s",
                func,
                args,
                kwargs,
            )
            # FIXME: provide better admin contact into
            raise flight.FlightInternalError(
                "internal server error, please contact server admin"
            )

    return wrapper


def parse_url(url: str | tuple[str, int] | None):
    """Parse a URL into a valid location for the FlightServer

    Returns a tuple of (hostname, port).

    """
    if url is None:
        return None
    if url in ["-", "0"]:
        return None
    if isinstance(url, tuple):
        url = "//%s:%s" % url
    parsed = urlparse(url, scheme="grpc")
    if parsed.hostname is None:
        parsed = urlparse("//" + url, scheme="grpc")
    return parsed.hostname, parsed.port


class ArrakisFlightServer(flight.FlightServerBase):
    """Arrow Flight server implementation to server timeseries.

    Parameters
    ----------
    url : str, optional
        The URL at which to serve Flight requests.  Either URI
        (e.g. grpc://localhost:port) or (host, port) tuple.  If None
        then server will be started on localport with a
        system-provided random port.  Default is to bind to all
        available interfaces on port 31206.
    backend: ServerBackend, optional
        An instantiated backend providing data to serve.
    scope_map: ScopeMap, optional
        Scope map for available flight endpoints.

    """

    def __init__(
        self,
        url: str | tuple[str, int] | None = constants.DEFAULT_LOCATION,
        backend: traits.ServerBackend | traits.PublishServerBackend | None = None,
        scope_map: ScopeMap | None = None,
        **kwargs,
    ):
        self._location = parse_url(url)
        self._is_stopped = threading.Event()
        self._validator = RequestValidator()

        if not backend and not scope_map:
            raise ValueError("nothing to serve, must specify scope map and/or backend")

        self._backend = backend
        logger.info("backend: %s", self._backend)

        self._scope_map = scope_map or ScopeMap()
        self._scope_map.sync_local_map(self._backend, constants.FLIGHT_REUSE_URL)
        logger.info("scope map: %s", self._scope_map)

        super().__init__(self._location, **kwargs)
        if self._location is None:
            self._location = ("127.0.0.1", self.port)
        else:
            self._location = (self._location[0], self.port)
        logger.info("URL: %s", self.url)

    @property
    def url(self):
        return "grpc://%s:%s" % self._location

    @exception_catcher
    def list_flights(
        self, context: flight.ServerCallContext, criteria: bytes
    ) -> Iterator[flight.FlightInfo]:
        """List flights available on this service.

        Parameters
        ----------
        context : ServerCallContext
            Common contextual information.
        criteria : bytes
            Filter criteria provided by the client.

        Yields
        ------
        FlightInfo

        """
        logger.debug("serving list_flights for %s", context.peer())
        for channel in self._channels:
            yield self.make_flight_info(
                create_command(
                    RequestType.Stream,
                    channels=[channel.name],
                    validator=self._validator,
                )
            )

    @exception_catcher
    def get_flight_info(
        self, context: flight.ServerCallContext, descriptor: flight.FlightDescriptor
    ) -> flight.FlightInfo:
        """Get information about a flight.

        Parameters
        ----------
        context : ServerCallContext
            Common contextual information.
        descriptor : FlightDescriptor
            The descriptor for the flight provided by the client.

        Returns
        -------
        FlightInfo

        """
        logger.debug("serving get_flight_info for %s", context.peer())
        return self.make_flight_info(descriptor.command)

    @exception_catcher
    def do_exchange(
        self,
        context: flight.ServerCallContext,
        descriptor: flight.FlightDescriptor,
        reader: flight.MetadataRecordBatchReader,
        writer: flight.MetadataRecordBatchWriter,
    ) -> flight.FlightDataStream:
        """Write data to a flight.

        Parameters
        ----------
        context : ServerCallContext
            Common contextual information.
        ticket : Ticket
            The ticket for the flight.

        Returns
        -------
        FlightDataStream
            A stream of data to send back to the client.

        """
        if not self._backend:
            raise flight.FlightServerError(
                "DoExchange requests unavailable from this server"
            )
        logger.debug("serving DoExchange request for %s", context.peer())
        return self.process_exchange_request(descriptor, reader, writer)

    def process_exchange_request(
        self,
        descriptor: flight.FlightDescriptor,
        reader: flight.MetadataRecordBatchReader,
        writer: flight.MetadataRecordBatchWriter,
    ) -> flight.FlightDataStream:
        """Write data to a flight.

        Parameters
        ----------
        context : ServerCallContext
            Common contextual information.
        ticket : Ticket
            The ticket for the flight.

        Returns
        -------
        FlightDataStream
            A stream of data to send back to the client.

        """
        assert self._backend
        request, kwargs = parse_command(descriptor.command, validator=self._validator)
        logger.debug("serving DoExchange %s request", request.name)
        match request:
            case RequestType.Partition:
                if not traits.can_publish(self._backend):
                    raise flight.FlightError(
                        "partition not supported for server backend"
                    )
                return self._partition(reader, writer, **kwargs)
            case _:
                raise flight.FlightError("request type not valid")

    @exception_catcher
    def do_get(
        self, context: flight.ServerCallContext, ticket: flight.Ticket
    ) -> flight.FlightDataStream:
        """Write data to a flight.

        Parameters
        ----------
        context : ServerCallContext
            Common contextual information.
        ticket : Ticket
            The ticket for the flight.

        Returns
        -------
        FlightDataStream
            A stream of data to send back to the client.

        """
        if not self._backend:
            raise flight.FlightServerError(
                "DoGet requests unavailable from this server"
            )
        logger.debug("serving DoGet request for %s", context.peer())
        return self.process_get_request(context, ticket)

    def process_get_request(
        self, context: flight.ServerCallContext | None, ticket: flight.Ticket
    ) -> flight.FlightDataStream:
        """Write data to a flight.

        Parameters
        ----------
        context : ServerCallContext
            Common contextual information.
        ticket : Ticket
            The ticket for the flight.

        Returns
        -------
        FlightDataStream
            A stream of data to send back to the client.

        """
        assert self._backend
        request, kwargs = parse_command(ticket.ticket, validator=self._validator)
        logger.debug("serving DoGet %s request", request.name)
        match request:
            case RequestType.Stream:
                return self._stream(context, **kwargs)
            case RequestType.Describe:
                return self._describe(**kwargs)
            case RequestType.Find:
                return self._find(**kwargs)
            case RequestType.Count:
                return self._count(**kwargs)
            case RequestType.Publish:
                if not traits.can_publish(self._backend):
                    raise flight.FlightError("publish not supported for this backend")
                return self._publish(**kwargs)
            case _:
                raise flight.FlightServerError("request type not valid")

    @exception_catcher
    def list_actions(
        self, context: flight.ServerCallContext
    ) -> Iterable[tuple[str, str]]:
        """List custom actions available on this server.

        Parameters
        ----------
        context : ServerCallContext
            Common contextual information.

        Returns
        -------
        Iterable of 2-tuples in the form (command, description).

        """
        if traits.can_publish(self._backend):
            logger.debug("serving list_actions for %s", context.peer())
            return [("publish", "Request to publish data.")]
        else:
            return []

    @exception_catcher
    def do_action(
        self, context: flight.ServerCallContext, action: flight.Action
    ) -> Iterator[bytes]:
        """Execute a custom action.

        Parameters
        ----------
        context : ServerCallContext
            Common contextual information.
        action : Action
            The action to execute.

        Yields
        ------
        bytes

        """
        logger.debug("serving %s action for %s", action.type, context.peer())
        match action.type:
            case _:
                raise flight.FlightError("action not valid")

    def _construct_endpoints(self, cmd: bytes) -> list[flight.FlightEndpoint]:
        endpoints = []
        request, kwargs = parse_command(cmd, validator=self._validator)

        # publish requests can only be served directly to local endpoints,
        # and we have validated that this server can accept publish requests
        if request in {RequestType.Publish, RequestType.Partition}:
            return [flight.FlightEndpoint(cmd, [constants.FLIGHT_REUSE_URL])]

        # filter source map by time retention
        if request is RequestType.Stream:
            scope_map = self._scope_map.filter_by_range(
                start=kwargs["start"],
                end=kwargs["end"],
            )
        else:
            scope_map = self._scope_map

        # map channels to endpoints
        if request in {RequestType.Stream, RequestType.Describe}:
            endpoints_for_channels = scope_map.endpoints_for_channels(
                kwargs["channels"]
            )
            for channels, locations in endpoints_for_channels:
                kwargs["channels"] = channels
                ticket = create_command(request, validator=self._validator, **kwargs)
                endpoints.append(flight.FlightEndpoint(ticket, locations))

        elif request in {RequestType.Find, RequestType.Count}:
            ticket = create_command(request, validator=self._validator, **kwargs)
            # ultimately we want to look at the request and use that to pair
            # down the endpoints we return.
            # for now just make sure to only send unique locations back
            location_set = set()
            for domain in scope_map.domains:
                locations = scope_map.endpoints_for_domain(domain)
                for entry in locations:
                    location_set.add(entry)
            for entry in location_set:
                endpoints.append(flight.FlightEndpoint(ticket, [entry]))

        else:
            raise flight.FlightError(f"Unknown request: {request}")

        if not endpoints:
            raise flight.FlightError("Could not find channels on any known endpoints.")

        return endpoints

    def make_flight_info(self, cmd: bytes) -> flight.FlightInfo:
        """Create Arrow Flight stream descriptions from commands.

        Parameters
        ----------
        cmd : bytes
            The opaque command to parse.

        Returns
        -------
        flight.FlightInfo
            The Arrow Flight stream description describing the command.

        """
        endpoints = self._construct_endpoints(cmd)
        descriptor = flight.FlightDescriptor.for_path(cmd)

        request, args = parse_command(cmd, validator=self._validator)

        match request:
            case RequestType.Stream:
                if self._backend:
                    channels = self._backend.describe(channels=args["channels"])
                else:
                    # create dummy channel metadata for each channel as the client
                    # does not use this when making a request. by doing this,
                    # information servers do not need to store all metadata for the
                    # channels for a domain it could potentially serve, but instead
                    # can delegate to the endpoints it does know about
                    channels = [
                        Channel(name, data_type=numpy.dtype("int32"), sample_rate=32)
                        for name in args["channels"]
                    ]
                schema = schemas.stream(channels)
            case RequestType.Describe:
                schema = schemas.describe()
            case RequestType.Find:
                schema = schemas.find()
            case RequestType.Count:
                schema = schemas.count()
            case RequestType.Publish:
                if not traits.can_publish(self._backend):
                    raise flight.FlightError("publish not supported for server backend")
                schema = schemas.publish()
            case RequestType.Partition:
                if not traits.can_publish(self._backend):
                    raise flight.FlightError(
                        "partition not supported for server backend"
                    )
                schema = schemas.partition()
            case _:
                raise flight.FlightError("command not understood")

        return flight.FlightInfo(schema, descriptor, endpoints, -1, -1)

    def shutdown(self) -> None:
        """Shut down the server."""
        self._is_stopped.set()
        return super().shutdown()

    def wait_until_shutdown(self) -> None:
        """Wait until the server receives a shutdown request."""
        self._is_stopped.wait()

    def _find(
        self,
        *,
        pattern: str,
        data_type: list[str],
        min_rate: int,
        max_rate: int,
        publisher: list[str],
    ) -> flight.FlightDataStream:
        """Serve Flight data for the 'find' route."""
        assert isinstance(self._backend, traits.ServerBackend)
        metadata = self._backend.find(
            pattern=pattern,
            data_type=data_type,
            min_rate=min_rate,
            max_rate=max_rate,
            publisher=publisher,
        )
        return arrow.create_metadata_stream(metadata)

    def _count(
        self,
        *,
        pattern: str,
        data_type: list[str],
        min_rate: int,
        max_rate: int,
        publisher: list[str],
    ) -> flight.FlightDataStream:
        """Serve Flight data for the 'count' route."""
        assert isinstance(self._backend, traits.ServerBackend)
        count = self._backend.count(
            pattern=pattern,
            data_type=data_type,
            min_rate=min_rate,
            max_rate=max_rate,
            publisher=publisher,
        )
        schema = schemas.count()
        batch = pyarrow.RecordBatch.from_arrays(
            [
                pyarrow.array(
                    [count],
                    type=schema.field("count").type,
                ),
            ],
            schema=schema,
        )
        return flight.RecordBatchStream(
            pyarrow.RecordBatchReader.from_batches(schema, [batch])
        )

    def _describe(self, *, channels: Iterable[str]) -> flight.FlightDataStream:
        """Serve Flight data for the 'describe' route."""
        assert isinstance(self._backend, traits.ServerBackend)
        metadata = self._backend.describe(channels=channels)
        return arrow.create_metadata_stream(metadata)

    def _stream(
        self,
        context: flight.ServerCallContext | None,
        *,
        channels: Iterable[str],
        start: int,
        end: int,
    ) -> flight.FlightDataStream:
        """Serve Flight data for the 'stream' route."""
        assert isinstance(self._backend, traits.ServerBackend)

        metadata = self._backend.describe(channels=channels)
        schema = schemas.stream(metadata)
        blocks = self._backend.stream(channels=channels, start=start, end=end)
        return flight.GeneratorStream(
            schema,
            self._generate_stream(context, schema, blocks),
        )

    def _publish(self, *, publisher_id: str) -> flight.FlightDataStream:
        """Serve Flight data for the 'publish' route."""
        assert traits.can_publish(self._backend)
        schema = schemas.publish()
        info = self._backend.publish(publisher_id=publisher_id)
        batch = pyarrow.RecordBatch.from_arrays(
            [
                pyarrow.array(
                    [info],
                    type=schema.field("properties").type,
                ),
            ],
            schema=schema,
        )
        return flight.RecordBatchStream(
            pyarrow.RecordBatchReader.from_batches(schema, [batch])
        )

    def _partition(self, reader, writer, *, publisher_id: str) -> None:
        """Exchange Flight data for the 'partition' route."""
        assert traits.can_publish(self._backend)
        schema = schemas.partition()

        # read metadata from client
        channels = []
        for batch in arrow.read_all_chunks(reader):
            for meta in batch.to_pylist():
                data_type = numpy.dtype(meta["data_type"])
                channel = Channel(
                    meta["channel"],
                    sample_rate=meta["sample_rate"],
                    data_type=data_type,
                    publisher=publisher_id,
                )
                channels.append(channel)

        # partition channels
        channels = list(
            self._backend.partition(channels=channels, publisher_id=publisher_id)
        )

        # prepare the batch with mappings
        batches = arrow.create_partition_batches(channels)

        # send partitions back to the client
        writer.begin(schema)
        for batch in batches:
            writer.write_batch(batch)
        writer.close()

    def _generate_stream(
        self,
        context: flight.ServerCallContext | None,
        schema: pyarrow.Schema,
        blocks: Iterator[SeriesBlock],
    ) -> Iterator[pyarrow.RecordBatch]:
        """Generate a record batch stream which can be stopped."""
        for block in blocks:
            if self._is_stopped.is_set() or (context and context.is_cancelled()):
                return
            yield block.to_column_batch(schema)
