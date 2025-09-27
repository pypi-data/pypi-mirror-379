#!/usr/bin/env python

class InitialRequestException(Exception):
    """
    Exception raised when an initial request has not been performed.

    This exception is intended to be raised if a method that requires
    an initial request is called before the `initial_request()` method
    has been executed on the client.

    Example:
        >>> from infosecmachines import Client 
        >>> from infosecmachines.exceptions import InitialRequestException
        >>> client = Client()
        >>> try:
        >>>     client.search_machine("Multimaster")
        >>> except InitialRequestException:
        >>>     print("You must call `initial_request()` first.")
    """
    pass

class InitialRequestAsyncException(Exception):
    """
    Exception raised when an initial asynchronous request has not been performed.

    This exception is intended to be raised if an asynchronous method that requires
    an initial request is called before the `initial_request()` coroutine has been
    awaited on the async client.

    Example:
        >>> import asyncio
        >>> from infosecmachines import ClientAsync 
        >>> from infosecmachines.exceptions import InitialRequestAsyncException
        >>> async def main():
        >>>     client = ClientAsync()
        >>>     try:
        >>>         await client.search_machine("Multimaster")
        >>>     except InitialRequestAsyncException:
        >>>         print("You must await `initial_request()` first.")
        >>> asyncio.run(main())
    """
    pass
