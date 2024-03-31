[![License](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.html)
![First Principles Software](https://img.shields.io/badge/Powered_by-First_Principles_Software-blue)
[![Status](https://img.shields.io/badge/Status-Alpha-yellow)](https://github.com/runemalm/py-domain-driven-design)

> **Note:** This library is currently in alpha stage and is under active development. APIs and features may change before the final release.

## py-domain-driven-design

A domain driven design library for Python.

## Roadmap

Below is a list of planned features and enhancements for future releases of the `py-domain-driven-design` library.

- [ ] **Repository Pattern**: Add support for the repository pattern to provide a standard way to access domain objects from a data source.
- [ ] **Aggregates**: Add support for defining and working with aggregates, including aggregate roots and associated objects.
- [ ] **Value Objects**: Implement support for defining value objects to represent immutable domain concepts.
- [ ] **Entities**: Add support for defining entities with distinct identities and lifecycles.
- [ ] **Domain Events**: Implement infrastructure for defining and handling domain events to capture important domain changes.
- [ ] **Integration Events**: Add support for defining and handling integration events for communication between different bounded contexts.
- [ ] **Listeners**: Implement listeners to react to domain and integration events, enabling reactive and decoupled systems.
- [ ] **Documentation**: Expand the documentation to cover new features and provide more comprehensive usage examples and best practices.

We welcome feedback and contributions to help shape the future of this library. If you have ideas or suggestions, please [create an issue](

## Python Compatibility

This library is compatible and tested with the following Python versions:

- Python 3.7
- Python 3.8
- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12

[![Push on master](https://github.com/runemalm/py-domain-driven-design/actions/workflows/master.yml/badge.svg?branch=master)](https://github.com/runemalm/py-domain-driven-design/actions/workflows/master.yml)

## Installation:

```bash
$ pip install py-domain-driven-design
```

## Documentation:

You can find the latest documentation at [readthedocs](https://py-domain-driven-design.readthedocs.io/en/latest/) (coming soon).

## License

`py-domain-driven-design` is released under the GPL 3 license. See [LICENSE](LICENSE) for more details.

## Source Code

You can find the source code for `py-domain-driven-design` on [GitHub](https://github.com/runemalm/py-domain-driven-design).

## Release Notes

### [1.0.0-alpha.1](https://github.com/runemalm/py-domain-driven-design/releases/tag/v1.0.0-alpha.1) (2024-04-xx)

- Initial alpha release.
- Added implementation for the repository pattern, providing a base for data access in a domain-driven design context.
- Basic Documentation: An initial set of documentation is provided, focusing on the repository pattern.
- License: Released under the GPL 3 license.
