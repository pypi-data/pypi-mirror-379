# Changelog

## [Unreleased]

## [0.4.0] - 2025-07-10

### Added

- Add 'expected latency' parameter to metadata to specify expected latency in
  which the producer will produce data, after which a timeout will occur
- Add 'common' key in channel metadata files which set defaults for all
  channels
- Add custom server errors for use in backends

### Fixed

- Fix issues with partition endpoint by (1) fixing the find/count schemas to
  include publisher metadata and (2) adding relevant publisher metadata to
  fix channel partitioning
- Ensure only unique locations as endpoints to find and count requests are
  sent
- Ensure optional channel properties are not dropped in partitioning
- Fix issue in generating null values from masked arrays in stream endpoint

### Changed

- Allow filtering of scope map in stream requests by start/end times rather
  than by whether the endpoint serves live data
- Update arrakis client version to 0.4.1
- Remove unused appdirs dependency

## [0.3.0] - 2025-04-16

### Added

- Add schema validation to request descriptors allowing server-side validation
  of requests

### Fixed

* Switch time values in mock server block construction from nanoseconds to
  seconds for data transformations

## [0.2.0] - 2025-04-09

### Added

- Add ability to assign a random port for server

### Fixed

- Better endpoint handling for endpoint construction
- Raise import errors when loading backend plugins from entrypoints
- Allow server to stop in-process stream requests prior to shutdown

### Changed

- CLI: handle backends as 'subcommands', i.e. arrakis-server KAFKA, rather than
  via --backend KAFKA. This allows backends to specify their own server command
  line arguments
- Change name of ConfigMetadataBackend to ChannelConfigBackend, simplify
  interface
- Rework ChannelConfigBackend to enforce channel properties, protect against
  overwriting channels
- partition: rework `partition_channels`:
  * Don't update metadata in place
  * Assign publisher ID to channels
  * Ensure all channels are returned in the same order
  * Tweak partition naming scheme (remove domain, rely on publisher ID)
- metadata: handle partitioning within the load method
- metadata: Fix check for cache file when initializing

## [0.1.0] - 2025-03-13

- Initial release

[unreleased]: https://git.ligo.org/ngdd/arrakis-server/-/compare/0.4.0...main
[0.4.0]: https://git.ligo.org/ngdd/arrakis-server/-/tags/0.4.0
[0.3.0]: https://git.ligo.org/ngdd/arrakis-server/-/tags/0.3.0
[0.2.0]: https://git.ligo.org/ngdd/arrakis-server/-/tags/0.2.0
[0.1.0]: https://git.ligo.org/ngdd/arrakis-server/-/tags/0.1.0
