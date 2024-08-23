__all__ = [
	"Caching",
	"HttpsServerOptions",
	"UseNewPacket",
	"EnetServerOptions",
	"ClientOptions",
	"ClientType"
]


from typing import TypedDict

from .growapi import GrowAPI
from .peer import NativePeerMethod


class Caching(TypedDict):
	players: dict[int, int]


class HttpsServerOptions(TypedDict):
	ip: str
	enetPort: int
	httpPort: int
	httpsPort: int
	enable: bool
	type2: bool


class UseNewPacket(TypedDict):
	asClient: bool

class EnetServerOptions(TypedDict):
	ip: str
	port: int
	maxPeers: int
	useNewPacket: UseNewPacket


class ClientOptions(TypedDict):
	# Third Party Plugins
	plugins: list[GrowAPI]

	# Bult-in https web server
	https: HttpsServerOptions
	enet: EnetServerOptions


class ClientType(TypedDict):
	ip: str
	port: int
	def setEmit(emit) -> None: ...
	def create(maxPeers: int, isClient: bool) -> None: ...
	def service() -> None: ...
	def deInit() -> None: ...
	def send(peerID: int, count: int, packets: list[bytearray]) -> None: ...
	def disconnect(peerID: int) -> None: ...
	def disconnectLater(peerID: int) -> None: ...
	def disconnectNow(peerID: int) -> None: ...
	def toggleNewPacket() -> None: ...
	def connect(ipAddress: str, port: int, peerID: int) -> bool: ...
	def getPeer(peerID: int) -> NativePeerMethod: ...