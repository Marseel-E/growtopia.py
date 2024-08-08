__all__ = ('PlayerPool')


from numpy import uint32
from enet import ENetPeer
from .Player import Player



class PlayerPool:
	def __init__(self) -> None:
		self.players: dict[uint32, Player] = {}


	def newPlayer(self, peer: ENetPeer) -> Player:
		p: Player = Player(peer)

		self.players[peer.connectID] = p

		return p
	

	def removePlayer(self, connect_id: uint32) -> None:
		self.players.remove(connect_id)


	def getPlayer(self, connect_id: uint32) -> Player:
		for uid, p in self.players.items():
			if (connect_id != uid):
				continue

			return p
		
		return None


	def getActivePlayers(self) -> int:
		return len(self.players)