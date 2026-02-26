"""Allow ``python -m mega-header-astroml.ingestion`` to start the streaming client."""
import asyncio

from mega-header-astroml.ingestion.stream import _configure_logging, _main

_configure_logging()
asyncio.run(_main())
