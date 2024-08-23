__all__ = [
	"Client"
]


from EventEmitter import EventEmitter
from typed import (
	Caching,
	ClientOptions,
	ClientType
)
from utils import parseText
from .Peer import Peer



class Client:
	def __init__(self) -> None:
		...