#!/usr/bin/env python
"""
InfosecMachines API

This module provides a Python interface to interact with the Infosec Machines API,
allowing users to search for and retrieve detailed information about machines
available on the platform.

Author:
    dreamer

Version:
    0.0.1

Main classes:
    - Client: Synchronous client for making API requests.
    - ClientAsync: Asynchronous client for making API requests using `asyncio`.

Usage examples:
----

    # Using the synchronous client
    >>> import infosecmachines as info
    >>> client = info.Client()
    >>> client.initial_request()
    >>> results = client.search_machine(machine="Multimaster")
    >>> if not results:
    >>>     exit()
    >>> print(results['os'])
    >>> for key, value in results.items():
    >>>     print(key, value)

    # Using the asynchronous client
    >>> import asyncio
    >>> import infosecmachines as info
    >>> async def main():
    >>>     async with info.ClientAsync() as client:
    >>>         results = await client.search_machine("Multimaster")
    >>>         print(results)
    >>> asyncio.run(main())
"""

from .s4vimachines import Client as Client 
from .s4vimachines import ClientAsync as ClientAsync
from . import exceptions

__version__ = "0.0.1"

__all__ = [
        '__version__',
        'ClientAsync',
        'Client',
        'exceptions',
        ]
