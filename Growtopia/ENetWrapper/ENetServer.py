__all__ = ('ENetServer')


from numpy import uint16

from enet import (
	ENetHost,
	ENetEvent,
	ENetAddress,
	ENET_HOST_ANY,
	enet_host_create,
	enet_crc32,
	enet_host_compress_with_range_coder
)


class ENetServer:
	def __init__(
		self,
		port: int,
		max_peers: int = 256
	) -> None:
		self.port = port
		self.max_peers = max_peers

		self.server: ENetHost
		self.event: ENetEvent
		self.unique_id: str

	
	def init(self, port: uint16, max_peers: int):
		if self.server:
			return False
		
		address: ENetAddress = ENetAddress(
			host=ENET_HOST_ANY,
			port=port
		)

		self.server = enet_host_create(
			address,
			max_peers,
			2, 0, 0
		)

		if not self.server:
			return False
		
		self.server.checksum = enet_crc32

		enet_host_compress_with_range_coder(self.server)

		return True

	
	def getHost(self) -> ENetHost:
		return self.server

	
	def getEvent(self) -> ENetEvent:
		return self.event