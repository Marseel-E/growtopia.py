__all__ = ('Server')


from ENetWrapper import ENetServer
from Player import PlayerPool
from World import WorldPool
from time import time
from humanize import naturaltime
from numpy import uint16


class Server(ENetServer):
	def __init__(
		self,
		player_pool: PlayerPool,
		world_pool: WorldPool
	) -> None:
		self.player_pool = player_pool
		self.world_pool = world_pool

		self.clock: float = time()

		super().__init__()


	def init(self, port: uint16, peer_count: int) -> bool:
		return bool(self.ENetServer.init(port, peer_count))

	
	def getUptime(self) -> str:
		return naturaltime(time() - self.clock)


from dataclasses import dataclass


@dataclass
class ServerData:
	url: str
	port: uint16