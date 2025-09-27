#!/usr/bin/env python
import requests
from typing import Dict, Generator, List, Literal, NoReturn
from .classes import S4viResponse, totalMachines, MachineResult, Writeup
from .exceptions import InitialRequestAsyncException, InitialRequestException
from typeguard import typechecked
import random
import aiohttp

class Client():
    """
    Synchronous client for interacting with the ``infosecmachines.io`` API.

    This client manages API requests using ``requests.Session`` and provides
    convenience methods for retrieving information about available machines or
    searching for specific ones by name.

    The client can be used either as a context manager or instantiated directly.
    When used as a context manager, the underlying HTTP session is automatically
    created and closed. When instantiated directly, the session remains open
    until ``close()`` is called or the object is garbage collected.

    Methods
    -------
    initial_request() -> None
        Performs the initial API request and populates the internal state.
    search_machine(name: str) -> list[dict[str, Any]]
        Search for a machine by name and return a list of matching results.
    get_all_machines() -> list[dict[str, Any]]
        Retrieve a list of all available machines.

    Examples
    --------
    Using as a context manager:

    >>> from infosecmachines import Client
    >>> def main() -> None:
    ...     with Client() as client:
    ...         results = client.search_machine("Tentacle")
    ...     print(results[0]["name"])
    ...
    >>> if __name__ == "__main__":
    ...     main()

    Using without a context manager:

    >>> from infosecmachines import Client
    >>> def main() -> None:
    ...     client = Client()
    ...     client.initial_request()
    ...     machines = client.search_machine("Tentacle")
    ...     print(machines[0]["techniques"])
    ...
    >>> if __name__ == "__main__":
    ...     main()

    Notes
    -----
    - The return values are dictionaries with fixed keys such as
      ``name``, ``os``, ``state``, ``techniques``, among others.
    - A static type checker (e.g., mypy or basedpyright) can infer the
      structure of the returned dictionaries.
    """

    def __init__(self,
                 timeout: int | None = None,
                 headers: dict | None = None,
                 cookies: dict | None = None,
                 **kwargs,
                 ) -> None:

        """
        Initialize a new ``Client`` instance.

        Creates a new client with an internal ``requests.Session`` object and
        optional configuration such as timeout, headers, and cookies. Any additional
        keyword arguments are passed directly to the underlying ``Session``.

        Parameters
        ----------
        timeout : int | None, optional
            Default timeout (in seconds) to apply to requests. If ``None``, no
            default timeout is applied.
        headers : dict | None, optional
            Default headers to include with all requests made by this client.
        cookies : dict | None, optional
            Cookies to include with all requests made by this client.
        **kwargs : object
            Additional keyword arguments to configure the underlying
            ``requests.Session``.

        Notes
        -----
        - The client maintains a persistent HTTP session for connection reuse.
        - To ensure resources are released, either use the client as a context
          manager or call ``close()`` explicitly.
        """

        self._timeout = timeout 
        self._headers = headers 
        self._cookies = cookies 
        self._kwargs = kwargs
        self._session = requests.Session()

    def __enter__(self):
        self.initial_request()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.close()

        return False 

    def initial_request(self):

        """
        Perform the initial API request.

        Executes a single HTTP ``GET`` request using the internal
        ``requests.Session``. The response is stored in internal variables
        to allow searching and counting of machines resolved by S4vitar.

        Attributes
        ----------
        html : dict
            The raw API response in JSON format.
        totalMachines : dict[str, int]
            A dictionary mapping each platform name to the number of machines
            resolved by S4vitar on that platform.
        new_data : list[dict[str, str]]
            A list of dictionaries containing machine metadata. Each dictionary
            has the following fixed keys:

            - ``platform`` (str)
            - ``name`` (str)
            - ``os`` (str)
            - ``state`` (str)
            - ``techniques`` (str)
            - ``certification`` (str)
            - ``ip`` (str)
            - ``video`` (str)

        Notes
        -----
        - Static type checkers (e.g., mypy, basedpyright) can infer the structure
          of the dictionaries stored in ``new_data``.
        - Direct manipulation of these attributes is not recommended unless you
          understand their structure.
        """

        resp = self._session.get(url='https://infosecmachines.io/api/machines', 
                                 timeout=self._timeout, 
                                 headers=self._headers, 
                                 cookies=self._cookies,
                                 **self._kwargs)
        
        self.data: S4viResponse = resp.json()
        
        self.total: totalMachines = self.data['totalMachines']
        self.new_data: List[Dict] = self.data['newData']

    def initial_check(self) -> NoReturn | None:
        if not hasattr(self, "new_data"):
            raise InitialRequestException(f"Haz iniciado la petición inicial para empezar?")

        return None

    def close(self):
        self._session.close()

        return None
    
    @typechecked
    def search_machine(self, machine: str) -> tuple[MachineResult, ...]:
        """
        Search for a machine by name.

        Looks up a machine inside ``self.new_data`` by its name and returns
        the corresponding result(s) if found.

        Args:
            machine (str): The name of the machine to search for.

        Returns:
            tuple[MachineResult, ...] | None: A tuple of matching machine results
            if the machine is found, or ``None`` otherwise.

        Examples:
            >>> from infosecmachines import Client
            >>> client = Client()
            >>> client.initial_request()
            >>> results = client.search_machine(machine="Tentacle")
            >>> if results:
            ...     print(results[0]["name"])
            ... else:
            ...     print("No match found")
        """        

        self.initial_check()
        
        results = (src for src in self.new_data if src['name'].lower().strip() == machine.lower().strip())

        results: tuple[MachineResult, ...] = tuple(results)

        return results
    
    @typechecked
    def search_ip(self, adress: str) -> tuple[MachineResult]:
        """
        Search for a machine by its IP address.

        Looks up a machine in ``self.new_data`` by matching its IP address
        and returns the corresponding machine data if found.

        Args:
            address (str): The IP address of the machine to search for.

        Returns:
            MachineResult | None: A dictionary with fixed keys that a type
            checker (e.g., mypy, basedpyright) can recognize, or ``None`` if
            no machine matches the given IP address.

        Examples:
            >>> from infosecmachines import Client
            >>> client = Client()
            >>> client.initial_request()
            >>> result = client.search_ip(address="10.10.10.179")
            >>> if result:
            ...     print(result["techniques"])
        """        
        self.initial_check()
        src: MachineResult
        
        matches: tuple[MachineResult, ...] = tuple(src for src in self.new_data if src['ip'] == adress)
        
        return matches 

    @typechecked
    def search_os(self,
                  os: Literal['Windows', 'Linux'], 
                  return_type: Literal['Generator', 'Normal'] = 'Generator',
                  ) -> Generator[str, None, None] | tuple[str, ...]:

        """
        Search for machines by operating system.

        Filters machines stored in ``self.new_data`` by their operating system.
        By default, results are returned as a generator, but the output can be
        forced into a tuple by setting ``return_type="Normal"``.

        Args:
            os (Literal["Windows", "Linux"]): The operating system to search for.
            return_type (Literal["Generator", "Normal"], optional): 
                Controls the return type. Defaults to ``"Generator"``.
                - ``"Generator"`` → yields results lazily (default).
                - ``"Normal"`` → returns all results as a tuple.

        Returns:
            Generator[str, None, None] | tuple[str, ...]: 
            A sequence of machine names matching the given operating system.

        Examples:
            >>> from infosecmachines import Client
            >>> client = Client()
            >>> client.initial_request()
            >>> results = client.search_os(os="Windows", return_type="Normal")
            >>> if results:
            ...     print(results[0])
        """
        self.initial_check()
        
        gen = (src['name'] for src in self.new_data if src.get('os') == os)
       
        return gen if return_type == 'Generator' else tuple(gen)
    
    @typechecked
    def search_difficulty(
        self,
        difficulty: Literal["Easy", "Medium", "Hard", "Insane"],
        return_type: Literal["Generator", "Normal"] = "Generator"
    ) -> Generator[str, None, None] | tuple[str, ...]:
        """
        Search for machines by difficulty level.

        Filters machines stored in ``self.new_data`` by their difficulty rating.
        By default, results are returned as a generator, but the output can be
        forced into a tuple by setting ``return_type="Normal"``.

        Args:
            difficulty (Literal["Easy", "Medium", "Hard", "Insane"]): 
                The difficulty level to search for.
            return_type (Literal["Generator", "Normal"], optional): 
                Controls the return type. Defaults to ``"Generator"``.
                - ``"Generator"`` → yields results lazily (default).
                - ``"Normal"`` → returns all results as a tuple.

        Returns:
            Generator[str, None, None] | tuple[str, ...]: 
            A sequence of machine names matching the given difficulty.

        Examples:
            >>> from infosecmachines import Client
            >>> client = Client()
            >>> client.initial_request()
            >>> results = client.search_difficulty(difficulty="Insane", return_type="Normal")
            >>> if results:
            ...     print(results[0])
        """

        self.initial_check()

        gen = (src['name'] for src in self.new_data if src.get('state') == difficulty)

        return gen if return_type == 'Generator' else tuple(gen)

    @typechecked
    def search_platform(
        self,
        platform: Literal["HackTheBox", "VulnHub", "PortSwigger"],
        return_type: Literal["Generator", "Normal"] = "Generator"
    ) -> Generator[str, None, None] | tuple[str, ...]:
        """
        Search for machines by platform.

        Filters machines stored in ``self.new_data`` by their platform.
        By default, results are returned as a generator, but the output can be
        forced into a tuple by setting ``return_type="Normal"``.

        Args:
            platform (Literal["HackTheBox", "VulnHub", "PortSwigger"]): 
                The platform to search for.
            return_type (Literal["Generator", "Normal"], optional): 
                Controls the return type. Defaults to ``"Generator"``.
                - ``"Generator"`` → yields results lazily (default).
                - ``"Normal"`` → returns all results as a tuple.

        Returns:
            Generator[str, None, None] | tuple[str, ...]: 
            A sequence of machine names matching the given platform.

        Examples:
            >>> from infosecmachines import Client
            >>> client = Client()
            >>> client.initial_request()
            >>> results = client.search_platform(platform="HackTheBox", return_type="Normal")
            >>> if results:
            ...     print(results[0])
        """

        self.initial_check()

        gen = (src['name'] for src in self.new_data if src.get('platform') == platform)

        return gen if return_type == 'Generator' else tuple(gen)
    
    @typechecked
    def search_writeup(self, machine: str) -> Writeup | tuple[Writeup, ...] | None:
        """
        Retrieve the writeup metadata for a machine.

        Looks up the writeup for the given machine name and returns a
        `MachineWriteup` object when found. The lookup may be performed
        case-insensitively if ``case_insensitive`` is ``True``.

        Args:
            machine (str): The name of the machine to retrieve the writeup for.
            case_insensitive (bool, optional): If True, the search will ignore case.
                Defaults to ``True``.

        Returns:
            MachineWriteup | None:
                A ``MachineWriteup`` instance containing metadata and convenience
                methods for the writeup (see below), or ``None`` if no writeup was found.

        MachineWriteup structure
        -----------------------
        The returned object provides the following public attributes/methods:

        - ``name`` (str): The machine name.
        - ``url`` (str): The URL to the writeup.
        - ``download() -> Path``: Download the writeup to disk and return the saved path.
        - ``open() -> None``: Open the writeup in the default web browser.

        Examples:
            Using as a context manager:

            >>> from infosecmachines import Client
            >>> with Client() as client:
            ...     client.initial_request()
            ...     writeup = client.search_writeup("Multimaster")
            ...     if writeup:
            ...         print(writeup.name, writeup.url)
            ...         writeup.download()
            ...         writeup.open()

            Without context manager:

            >>> client = Client()
            >>> client.initial_request()
            >>> writeup = client.search_writeup("Multimaster")
            >>> if writeup:
            ...     print(writeup.name)
        """

        self.initial_check()
        
        result = self.search_machine(machine=machine) 

        if not result:
            return None 

        if len(result) > 1:

            objects: tuple[Writeup, ...]
            
            objects = tuple(
                    Writeup(name=r['name'], url=r['video'])
                    for r in result
                    )

            return objects

        writeup = Writeup(result[0]['video'], result[0]['name'])

        return writeup
    
    @typechecked
    def search_techniques(
        self,
        techniques: tuple[str, ...],
        return_type: Literal["Generator", "Normal"] = "Generator",
    ) -> Generator[str, None, None] | tuple[str, ...] | None:
        """
        Search machines by associated techniques or skills.

        Args:
            techniques (tuple[str, ...]): A tuple of skills/techniques to filter machines by.
                Each element must be a string representing a technique name.
            return_type (Literal["Generator", "Normal"], optional): Determines the return type.
                Defaults to ``"Generator"`` because this function is intended to iterate over
                multiple results.

        Returns:
            Generator[str, None, None] | tuple[str, ...] | None:
                - A generator of machine names if ``return_type`` is ``"Generator"``.
                - A tuple of machine names if ``return_type`` is ``"Normal"``.
                - ``None`` if no results are found.

        Examples:
            >>> from infosecmachines import Client
            >>> client = Client()
            >>> client.initial_request()
            >>> results = client.search_techniques(
            ...     techniques=("SQL Injection", "XSS"),
            ...     return_type="Normal"
            ... )
            >>> if not results:
            ...     exit()
            >>> print(results)
        """        
        self.initial_check()

        gen = (
                src['name'] for src in self.new_data
                if all(technique.lower() in src['techniques'].lower() for technique in techniques)
                ) 

        return tuple(gen) if return_type == 'Normal' else gen
    
    @typechecked
    def search_certificates(
        self,
        certificates: tuple[str, ...],
        return_type: Literal["Generator", "Normal"] = "Generator",
    ) -> Generator[str, None, None] | tuple[str, ...] | None:
        """
        Search machines by associated certificates.

        Args:
            certificates (tuple[str, ...]): A tuple of certificates to filter machines by.
                Each element must be a string (e.g., "OSCP", "OSWE", "OSEP").
            return_type (Literal["Generator", "Normal"], optional): Determines the return type.
                Defaults to ``"Generator"`` because this function is designed to handle
                multiple results efficiently.

        Returns:
            Generator[str, None, None] | tuple[str, ...] | None:
                - A generator of machine names if ``return_type`` is ``"Generator"``.
                - A tuple of machine names if ``return_type`` is ``"Normal"``.
                - ``None`` if no results are found.

        Examples:
            >>> from infosecmachines import Client
            >>> with Client() as client:
            ...     results = client.search_certificates(
            ...         certificates=("OSCP", "OSWE", "OSEP"),
            ...         return_type="Normal"
            ...     )
            ...     print(results)
        """

        self.initial_check()

        gen = (
                src['name'] for src in self.new_data
                if all(cert.lower() in src['certification'].lower() for cert in certificates)
                ) 
        
        return tuple(gen) if return_type == 'Normal' else gen
    
    @typechecked
    def advanced_search(
        self,
        objects: tuple[str, ...],
        return_type: Literal["Generator", "Normal"] = "Generator",
    ):
        """
        Advanced search that inspects across all machine keys.

        This function checks multiple attributes of each machine such as
        certifications, skills, name, operating system, difficulty, platform, etc.

        Args:
            objects (tuple[str, ...]): A tuple of strings to search for. Each element
                will be compared against multiple machine attributes.
            return_type (Literal["Generator", "Normal"], optional): Determines the return type.
                Defaults to ``"Generator"`` because this function is designed to handle
                multiple results efficiently.

        Returns:
            Generator[str, None, None] | tuple[str, ...] | None:
                - A generator of machine names if ``return_type`` is ``"Generator"``.
                - A tuple of machine names if ``return_type`` is ``"Normal"``.
                - ``None`` if no results are found.

        Examples:
            >>> from infosecmachines import Client
            >>> with Client() as client:
            ...     results = client.advanced_search(objects=("OSCP", "Windows", "SQLi"), return_type="Normal")
            ...     print(results)
        """

        self.initial_check()

        gen = (
            m['name'] for m in self.new_data
            if all(
                any(k.lower() in str(m[field]).lower() for field in m.keys() if field not in 'video')
                for k in objects
            )
        )


        return tuple(gen) if return_type == 'Normal' else gen
    
    @typechecked 
    def get_all_machines(self, return_type: Literal['Generator', 'Normal'] = 'Generator'):
        """
        Retrieve all machines available in infosecmachines.

        This function returns the complete set of machines fetched during
        the initial request, including their attributes (platform, name,
        OS, difficulty, techniques, certifications, IP, and writeup links).

        Args:
            return_type (Literal['Generator', 'Normal'], optional): Determines the return type.
                Defaults to ``"Generator"`` because this function is designed to handle
                a potentially large number of results efficiently.

        Returns:
            Generator[str, None, None] | tuple[str, ...] | None:
                - A generator of machine names if ``return_type`` is ``"Generator"``.
                - A tuple of machine names if ``return_type`` is ``"Normal"``.
                - ``None`` if no machines are available.

        Examples:
            >>> from infosecmachines import Client
            >>> with Client() as client:
            ...     machines = client.get_all_machines(return_type="Normal")
            ...     print(machines[10])
        """
        self.initial_check()

        machines = (
                m['name'] for m in self.new_data
                )

        return tuple(machines) if return_type == 'Normal' else machines
    
    @typechecked
    def get_random_machine(
        self,
        recoils: int = 100,
        objects: tuple[str, ...] | None = None
    ) -> str | None:
        """
        Retrieve a random machine.

        This function selects a random machine from the available dataset.  
        If ``objects`` is provided, the selection is filtered using the same
        logic as ``advanced_search``.

        Args:
            recoils (int, optional): Number of iterations for the random search loop.  
                Defaults to ``100``. Increasing this value can improve the chance of
                finding a machine when filters are applied.
            objects (tuple[str, ...] | None, optional): A tuple of strings used as
                filters. Each string is checked across machine attributes 
                (platform, OS, difficulty, techniques, certifications, etc.).  
                Defaults to ``None``, in which case a random machine is selected 
                without filtering.

        Returns:
            str | None:
                - A random machine name if found.
                - ``None`` if no machine matches the filters in ``objects``.

        Examples:
            >>> from infosecmachines import Client
            >>> with Client() as client:
            ...     machine = client.get_random_machine()
            ...     print(machine)  # Random machine from all available

            >>> with Client() as client:
            ...     machine = client.get_random_machine(objects=("OSCP", "Linux"))
            ...     print(machine)  # Random machine matching filters
        """

        self.initial_check()

        machines: tuple[str, ...] = self.get_all_machines('Normal') if not objects else self.advanced_search(objects=objects, return_type='Normal')
        
        if not machines:
            return ""

        machine = ''

        for _ in range(0, recoils + 1):
            machine = tuple(random.sample(machines, 1) )

        return machine[0]
    
    @property
    def machine_counts(self) -> totalMachines:
        """
        Retrieve the number of machines resolved per platform.

        This function returns a dictionary containing the total number of machines
        that S4vitar has resolved, categorized by platform.  
        To obtain the overall total, simply sum the values of the dictionary.

        Returns:
            dict[str, int]: A dictionary where the keys are platform names
            (e.g., ``"htb"``, ``"vuln"``, ``"swigger"``) and the values are the
            corresponding counts of resolved machines.

        Examples:
            >>> from infosecmachines import Client
            >>> with Client() as client:
            ...     print(machine_counts["htb"])  # Number of HackTheBox machines
        """
        self.initial_check()

        return self.total

class ClientAsync():
    """
    Asynchronous client for interacting with the infosecmachines.io API.

    This client uses ``aiohttp`` to perform asynchronous requests and provides 
    methods to fetch all available machines or search for specific ones.

    It is recommended to use this class inside an ``async with`` block, which will 
    automatically handle the initial request and resource cleanup.

    Examples
    --------
    Basic usage with context manager:
        >>> import asyncio
        >>> from infosecmachines import ClientAsync
        >>> async def main() -> None:
        ...     async with ClientAsync() as client:
        ...         results = await client.search_machine("Tentacle")
        ...     print(results[0]['name'])  # Type checker can see 'techniques', 'name', 'os', 'state', etc.
        >>> if __name__ == '__main__':
        ...     asyncio.run(main())

    Usage without context manager:
        >>> import asyncio
        >>> from infosecmachines import ClientAsync
        >>> async def main():
        ...     client = ClientAsync()
        ...     await client.initial_request()
        ...     machines = await client.search_machine("Tentacle")
        ...     print(machines[0]['techniques'])
        >>> if __name__ == '__main__':
        ...     asyncio.run(main())

    Usage with multiple tasks:
        >>> import asyncio, sys
        >>> from infosecmachines import ClientAsync
        >>> async def main() -> None:
        ...     async with ClientAsync() as client:
        ...         results = await asyncio.gather(
        ...             client.search_machine("Tentacle"),
        ...             client.search_machine("Multimaster"),
        ...         )
        ...     if not results:
        ...         sys.exit()
        ...     print(results[0][0]['name'])  # Tentacle, keys are fully visible to type checkers
        >>> if __name__ == '__main__':
        ...     asyncio.run(main())
    """
    
    def __init__(self, **kwargs) -> None:
        """
        Initialize the asynchronous client.

        This constructor accepts arbitrary keyword arguments, which will be 
        passed directly to the underlying ``aiohttp.ClientSession``. This allows 
        customization of session behavior such as timeouts, headers, cookies, 
        and connection options.

        Args:
            **kwargs: Arbitrary keyword arguments forwarded to 
                ``aiohttp.ClientSession``. Common parameters include:
                
                - ``headers`` (dict[str, str]): Default headers for all requests.
                - ``cookies`` (dict[str, str]): Cookies to include with each request.
                - ``timeout`` (aiohttp.ClientTimeout): Custom timeout configuration.
                - ``connector`` (aiohttp.TCPConnector): Low-level connection management.

        Examples:
            >>> from infosecmachines import ClientAsync
            >>> import aiohttp, asyncio
            >>>
            >>> async def main():
            ...     timeout = aiohttp.ClientTimeout(total=30)
            ...     async with ClientAsync(headers={"User-Agent": "infosec-bot"}, timeout=timeout) as client:
            ...         machines = await client.get_all_machines(return_type="Normal")
            ...         print(len(machines))
            >>>
            >>> if __name__ == "__main__":
            ...     asyncio.run(main())
        """

        self._kwargs = kwargs

    async def __aenter__(self):
        
        await self.initial_request()

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):

        return False    

    async def initial_check(self):

        if not hasattr(self, "new_data"):
            raise InitialRequestAsyncException("Necesitas realizar la petición inicial antes de empezar!")

    async def initial_request(self):
        """
        Perform the initial asynchronous request.

        This function makes a single HTTP ``GET`` request using 
        ``aiohttp.ClientSession``. The response is cached into 
        internal attributes for later use across search and query methods.

        Attributes set:
            self.html (dict): The raw JSON response from the API.
            self.totalMachines (dict[str, int]): A dictionary where each key is a 
                platform name and the value is the number of machines resolved 
                by S4vitar on that platform.
            self.new_data (dict[str, list[dict]]): Dictionary holding all machine
                data used for search operations. Each machine entry contains:

                - ``platform`` (str)
                - ``name`` (str)
                - ``os`` (str)
                - ``state`` (str)
                - ``techniques`` (str)
                - ``certification`` (str)
                - ``ip`` (str)
                - ``video`` (str)

        Notes:
            A type checker (e.g., mypy, basedpyright) can statically infer 
            the structure of these keys.  
            Direct manipulation of these attributes is not recommended 
            unless you know what you are doing.

        Examples:
            >>> import asyncio
            >>> from infosecmachines import ClientAsync
            >>> async def main():
            ...     client = ClientAsync()
            ...     await client.initial_request()
            ...     machine = await client.search_machine("Tentacle")
            ...     print(machine)
            >>> if __name__ == "__main__":
            ...     asyncio.run(main())
        """

        async with aiohttp.ClientSession(**self._kwargs) as sess:
            
            async with sess.get(url='https://infosecmachines.io/api/machines') as response:

                self.html: S4viResponse = await response.json()

                self.total: totalMachines = self.html['totalMachines']  

                self.new_data: List[Dict] = self.html['newData'] 
    
    @typechecked
    async def search_machine(self, machine: str) -> tuple[MachineResult] | tuple[MachineResult, ...]:
        '''
        Search machine function, this function returns machine data from the API.  
        
        Args:
            machine (str): Machine name to search. 

        Returns:
            Tuple[MachineResult, ...] | None: Machine information if found, otherwise None.

        Raises:
            InitialRequestAsyncException: If you try to call this function before the client context 
            has been entered (or before manually calling `initial_request()`).

        Examples:
        >>> import asyncio
        >>> from infosecmachines import ClientAsync
        >>> 
        >>> async def main():
        >>>     async with ClientAsync() as client:
        >>>         result = await client.search_machine("Tentacle")
        >>>         print(result)
        >>> 
        >>> asyncio.run(main())
        '''
        await self.initial_check()

        machine_fetch = (src for src in self.new_data if src['name'].lower().strip() == machine.lower().strip())

        machine_fetch: tuple[MachineResult, ...] = tuple(machine_fetch)

        return machine_fetch
    
    @typechecked
    async def _fetch_results(self, field: str, to_search: str, return_type: Literal['Generator', 'Normal'] = 'Generator'):
        
        await self.initial_check()

        gen = (src['name'] for src in self.new_data if src[field] == to_search)

        return tuple(gen) if return_type == 'Normal' else gen 
    
    @typechecked
    async def search_os(self, os: Literal['Windows', 'Linux'], return_type: Literal['Generator', 'Normal'] = 'Generator'):
        '''
        Search machines by operating system.

        Args:
            os (Literal['Windows', 'Linux']): Operating system to search for.
            return_type (Literal['Generator', 'Normal'], optional): 
                Determines the return format. Defaults to "Generator".
                - "Generator": Returns a generator of machine names (tuple of strings).
                - "Normal": Returns a tuple with machine details.

        Returns:
            Generator | tuple[str, ...] | None: Machines that match the given OS, 
            or None if not found.

        Raises:
            InitialRequestAsyncException: If called before performing the initial request.

        Examples
        --------
        >>> import asyncio
        >>> from infosecmachines import ClientAsync
        >>>
        >>> async def main():
        >>>     async with ClientAsync() as client:
        >>>         results = await client.search_os("Linux", return_type="Normal")
        >>>         if results: 
        >>>             print(results[0])
        >>>
        >>> asyncio.run(main())
        '''
        await self.initial_check()

        response = await self._fetch_results(field='os', to_search=os, return_type=return_type)
        
        return response
    
    @typechecked
    async def search_platform(self, platform: Literal['HackTheBox', 'VulnHub', 'PortSwigger'], return_type: Literal['Generator', 'Normal'] = 'Generator'):

        '''
        Search machines by platform.

        Args:
            platform (Literal['HackTheBox', 'VulnHub', 'PortSwigger']): 
                Platform to search for.
            return_type (Literal['Generator', 'Normal'], optional): 
                Determines the return format. Defaults to "Generator".
                - "Generator": Returns a generator of machine names (tuple of strings).
                - "Normal": Returns a tuple with machine details.

        Returns:
            Generator | tuple[str, ...] | None: Machines that match the given 
            platform, or None if not found.

        Raises:
            InitialRequestAsyncException: If called before performing the initial request.

        Examples
        --------
        >>> import asyncio
        >>> from infosecmachines import ClientAsync
        >>>
        >>> async def main():
        >>>     async with ClientAsync() as client:
        >>>         results = await client.search_platform("HackTheBox", return_type="Normal")
        >>>         if results:
        >>>             print(results[0])
        >>>
        >>> asyncio.run(main())
        '''

        await self.initial_check()

        response = await self._fetch_results(field='platform', to_search=platform, return_type=return_type)
        
        return response
    
    @typechecked
    async def search_difficulty(self, difficulty: Literal['Easy', 'Medium', 'Hard', 'Insane'], return_type: Literal['Generator', 'Normal'] = 'Generator'):

        '''
        Search machines by difficulty level.

        Args:
            difficulty (Literal['Easy', 'Medium', 'Hard', 'Insane']):
                Difficulty level to search for.
            return_type (Literal['Generator', 'Normal'], optional): 
                Determines the return format. Defaults to "Generator".
                - "Generator": Returns a generator of machine names (tuple of strings).
                - "Normal": Returns a tuple with machine details.

        Returns:
            Generator | tuple[str, ...] | None: Machines that match the given 
            difficulty, or None if not found.

        Raises:
            InitialRequestAsyncException: If called before performing the initial request.

        Examples
        --------
        >>> import asyncio
        >>> from infosecmachines import ClientAsync
        >>>
        >>> async def main():
        >>>     async with ClientAsync() as client:
        >>>         results = await client.search_difficulty("Insane", return_type="Normal")
        >>>         if results:
        >>>             print(results[0])
        >>>
        >>> asyncio.run(main())
        '''
        await self.initial_check()

        response = await self._fetch_results(field='state', to_search=difficulty, return_type=return_type)
        
        return response
    
    @typechecked
    async def search_ip(self, adress: str) -> tuple[MachineResult, ...] | tuple:
        '''
        Search for a machine by its IP address.

        Args:
            address (str): IP address of the machine to search for.

        Returns:
            Tuple[str, ...] | None: Dictionary containing the machine's data if found,
            otherwise None.

        Raises:
            InitialRequestAsyncException: If called before performing the initial request.

        Examples
        --------
        >>> import asyncio
        >>> from infosecmachines import ClientAsync
        >>>
        >>> async def main():
        >>>     async with ClientAsync() as client:
        >>>         result = await client.search_ip("10.10.10.120")
        >>>         if result:
        >>>             print(result[0]['name'])
        >>>
        >>> asyncio.run(main())
        '''
        await self.initial_check()
    
        matches: tuple[MachineResult, ...] = tuple(src for src in self.new_data if src['ip'] == adress)
        
        return matches 

    async def search_writeup(self, machine: str) -> tuple[Writeup] | tuple[Writeup, ...] | None:
        '''
        Retrieve the writeup for a given machine.

        Args:
            machine (str): Name of the machine to retrieve the writeup for.

        Returns:
            Writeup | None: A writeup object with attributes like `name` and `url`.
            The object provides helper methods such as `.download()` to save the writeup
            locally and `.open()` to open it in a browser.

        Raises:
            InitialRequestAsyncException: If called before performing the initial request.

        Examples
        --------
        >>> import asyncio
        >>> from infosecmachines import ClientAsync
        >>>
        >>> async def main():
        >>>     async with ClientAsync() as client:
        >>>         writeup = await client.get_writeup("Multimaster")
        >>>         if writeup:
        >>>             print(writeup.name, writeup.url)
        >>>             writeup.download()  # Download the writeup
        >>>             writeup.open()      # Open the writeup in a browser
        >>>
        >>> asyncio.run(main())
        '''

        result = await self.search_machine(machine=machine) 

        if not result:
            return None 

        if len(result) > 1:

            objects: tuple[Writeup, ...]
            
            objects = tuple(
                    Writeup(name=r['name'], url=r['video'])
                    for r in result
                    )

            return objects

        writeup = Writeup(result[0]['name'], name=result[0]['video'])

        return writeup
    
    @typechecked
    async def search_certificates(self, certificates: tuple[str, ...], return_type: Literal['Generator', 'Normal'] = 'Generator'):

        '''
        Search for machines by associated certificates.

        Args:
            certificates (tuple[str, ...]): A tuple of certificate names to filter machines by.
                For example: ("OSCP", "OSWE", "OSEP").
            return_type (Literal['Generator', 'Normal'], optional): Determines the return type.
                - "Generator": Returns a generator of machine dictionaries.
                - "Normal": Returns a tuple of machine dictionaries.
                Defaults to "Generator".

        Returns:
            Generator[str, None, None] | tuple[str, ...] | None: Matching machines
            if found, otherwise None.

        Raises:
            InitialRequestAsyncException: If called before performing the initial request.

        Examples
        --------
        >>> import asyncio
        >>> from infosecmachines import ClientAsync
        >>>
        >>> async def main():
        >>>     async with ClientAsync() as client:
        >>>         results = await client.search_certificates(
        >>>             certificates=("OSCP", "OSWE", "OSEP"),
        >>>             return_type="Normal"
        >>>         )
        >>>         if results:
        >>>             print(results[0])
        >>>
        >>> asyncio.run(main())
        '''
        await self.initial_check()

        gen = (
            src['name'] for src in self.new_data
            if all(cert.lower() in src['certification'].lower() for cert in certificates)
            ) 

        return tuple(gen) if return_type == 'Normal' else gen
    
    @typechecked
    async def search_techniques(self, techniques: tuple[str, ...], return_type: Literal['Generator', 'Normal'] = 'Generator'):
        '''
        Search for machines by techniques or skills.

        Args:
            techniques (tuple[str, ...]): A tuple of techniques/skills to filter machines by.
                Each item in the tuple should be a string.  
                For example: ("SQL Injection", "Buffer Overflow").
            return_type (Literal['Generator', 'Normal'], optional): Determines the return type.
                - "Generator": Returns a generator of machine dictionaries.
                - "Normal": Returns a tuple of machine dictionaries.
                Defaults to "Generator".

        Returns:
            Generator[str, None, None] | tuple[str, ...] | None: Matching machines
            if found, otherwise None.

        Raises:
            InitialRequestAsyncException: If called before performing the initial request.

        Examples
        --------
        >>> import asyncio
        >>> from infosecmachines import ClientAsync
        >>>
        >>> async def main():
        >>>     async with ClientAsync() as client:
        >>>         results = await client.search_techniques(
        >>>             techniques=("SQL Injection", "XSS"),
        >>>             return_type="Normal"
        >>>         )
        >>>         if results:
        >>>             print(results[0])
        >>>
        >>> asyncio.run(main())
        '''        
        await self.initial_check()

        gen = (
            src['name'] for src in self.new_data
            if all(cert.lower() in src['techniques'].lower() for cert in techniques)
            ) 

        return tuple(gen) if return_type == 'Normal' else gen
    
    @typechecked
    async def advanced_search(self, objects: tuple[str, ...], return_type: Literal['Generator', 'Normal'] = "Generator"):
        '''
        Perform an advanced search across all available machine attributes.

        This function inspects multiple keys such as platform, techniques, name,
        operating system, difficulty, and certification, returning machines that 
        match any of the provided search terms.

        Args:
            objects (tuple[str, ...]): A tuple of strings to search for across
                all machine attributes. For example: ("Linux", "OSCP", "SQL Injection").
            return_type (Literal['Generator', 'Normal'], optional): Determines the return type.
                - "Generator": Returns a generator of machine.
                - "Normal": Returns a tuple with machines.
                Defaults to "Generator".

        Returns:
            Generator[str, None, None] | tuple[str, ...] | None: Matching machines
            if found, otherwise None.

        Raises:
            InitialRequestAsyncException: If called before performing the initial request.

        Examples
        --------
        >>> import asyncio
        >>> from infosecmachines import ClientAsync
        >>>
        >>> async def main():
        >>>     async with ClientAsync() as client:
        >>>         results = await client.advanced_search(
        >>>             objects=("Linux", "OSCP", "SQL Injection"),
        >>>             return_type="Normal"
        >>>         )
        >>>         if results:
        >>>             print(results[0])
        >>>
        >>> asyncio.run(main())
        '''
        await self.initial_check()

        gen = (
            m['name'] for m in self.new_data
            if all(
                any(k.lower() in str(m[field]).lower() for field in m.keys() if field not in 'video')
                for k in objects
            )
        )

        return tuple(gen) if return_type == 'Normal' else gen

    @typechecked 
    async def get_all_machines(self, return_type: Literal["Generator", "Normal"] = 'Generator') -> Generator[str, None, None] | tuple[str, ...]:
        '''
        Retrieve all available machines from the API.

        Args:
            return_type (Literal['Generator', 'Normal'], optional): Determines the return type.
                - "Generator": Returns a generator of machine dictionaries.
                - "Normal": Returns a tuple of with all machines.
                Defaults to "Generator".

        Returns:
            Generator[str, None, None] | tuple[str, ...]: All available machines.

        Raises:
            InitialRequestAsyncException: If called before performing the initial request.

        Examples
        --------
        >>> import asyncio
        >>> from infosecmachines import ClientAsync
        >>>
        >>> async def main():
        >>>     async with ClientAsync() as client:
        >>>         machines = await client.get_all_machines(return_type="Normal")
        >>>         print(machines[10])
        >>>
        >>> asyncio.run(main())
        '''
        await self.initial_check()

        gen = (
                src['name'] for src in self.new_data
                )


        return tuple(gen) if return_type == 'Normal' else gen

    async def get_random_machine(self, recoils: int = 100, objects: tuple[str, ...] | None = None) -> str:
        '''
        Retrieve a random machine from the API.

        This function selects a random machine, optionally filtering the results 
        using the same criteria as ``advanced_search``.

        Args:
            recoils (int, optional): Number of iterations for the random selection loop.  
                Defaults to 100.
            objects (tuple[str, ...] | None, optional): Optional tuple of search terms 
                (e.g., certificates, techniques, OS) that will be passed to 
                ``advanced_search`` to filter machines before selecting randomly.  
                Defaults to None.

        Returns:
            str | None: The name of a random machine if found, otherwise None.

        Raises:
            InitialRequestAsyncException: If called before performing the initial request.

        Examples
        --------
        >>> import asyncio
        >>> from infosecmachines import ClientAsync
        >>>
        >>> async def main():
        >>>     async with ClientAsync() as client:
        >>>         machine = await client.get_random_machine(recoils=100)
        >>>         print(machine)  # Any random machine
        >>>
        >>>         machine = await client.get_random_machine(
        >>>             objects=("OSCP", "Linux", "SQL Injection")
        >>>         )
        >>>         print(machine)  # Random machine filtered by objects
        >>>
        >>> asyncio.run(main())
        '''        
        await self.initial_check()
        
        machines = await self.get_all_machines('Normal') if not objects else await self.advanced_search(objects=objects, return_type='Normal')
        
        if not machines:
            return ""

        machine = ''

        for _ in range(0, recoils + 1):
            machine = tuple(random.sample(machines, 1) )

        return machine[0]
    
    @property
    async def machine_counts(self) -> totalMachines:
        '''
        Dictionary with the number of machines resolved per platform.
        Requires that `initial_request()` has been called before.

        Raises:
            InitialRequestException: if the initial request was not performed.

        Returns:
            A dictionary with fixed keys (`htb`, `swigger`, `vuln`, `challengue`).
        
        Example:
        >>> async with ClientAsync() as client:
        >>>     await client.initial_request()
        >>>     counts = await client.machine_counts
        >>>     print(counts['htb'])
        '''        
        await self.initial_check()

        return self.total
