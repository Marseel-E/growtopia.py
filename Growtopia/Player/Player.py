__all__ = ('Player')


from enet import Peer
from .PlayerDialog import PlayerDialog

from Protocol import (
	PlayerFlags,
	TankInfo,
)

from numpy import (
	uint32, 
	uint64
)

from .PlayerItems import PlayerItems

from ENetWrapper import sendPacket


class Player(Peer, PlayerDialog):
	def __init__(self) -> None:
		self.details: TankInfo
		self.player_items: PlayerItems
		
		self.user_id: uint32
		self.flags: uint32
		
		self.raw_name: str
		self.display_name: str

		self.email_address: str
		self.discord_client_id: uint64

		super().__init__()


	def isFlagOn(self, flag: PlayerFlags) -> bool:
		if (self.flags & flag):
			return True
		
		return False

	def setFlag(self, flag: PlayerFlags) -> None:
		self.flags |= flag

	def removeFlag(self, flag: PlayerFlags) -> None:
		self.flags &= ~flag

	def setUserID(self, user_id: uint32) -> None:
		self.user_id = user_id


	def setRawName(self, name: str) -> None:
		self.raw_name = name


	
	def OnConnect(self) -> None:
		packet = SLoginInformationRequestPacket()
		sendPacket(self.Get(), packet)

	def OnDisconnect(self) -> None:
		...