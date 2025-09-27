#!/usr/bin/env python
from typing import NoReturn, TypedDict, List, Dict, Any
import webbrowser as web 
import screeninfo
from typeguard import typechecked
from yt_dlp import YoutubeDL

class Writeup:
    
    def __init__(self, url: str, name: str) -> None:
        self._url = url
        self._name = name 
    
    def open(self, new: int = 0, 
             autoraise: bool = True) -> bool:
        
        result = web.open(url=self._url, new=new, autoraise=autoraise)

        return result
    
    @typechecked
    def download(self, monitor: int = 0,
                 use_monitor_quality: bool = True,
                 quality: tuple[int, int] | None = None,
                 dest: str | None = None):
        
        pass

    @property
    def url(self) -> str:
        return self._url
    
    @url.setter 
    def url(self) -> NoReturn:

        raise ValueError("Error fatal, no puedes cambiar la url destino!")

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self) -> NoReturn:

        raise ValueError("Error fatal, no puedes cambiar la url destino!")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(url={self._url!r}, name={self._name!r})"


class S4viResponse(TypedDict):

    # ['newData', 'totalMachines'] 
    newData: List
    totalMachines: Dict

class totalMachines(TypedDict):

    htb: str | int  
    vuln: str | int 
    swigger: str | int 
    challenge: str | int 

class MachineResult(TypedDict):

    platform: str 
    name: str 
    os: str 
    state: str
    techniques: str 
    certification: str 
    ip: str 
    video: str 
