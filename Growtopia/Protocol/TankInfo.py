__all__ = ('TankInfo')


from numpy import (
	int32,
	uint32,
)

from .enums import (
	PlatformID,
	ClientFlags,
)

from Utils import TextParser


class TankInfo:
	def __init__(
		self,
		requested_name: str = "",
		tank_id_name: str = "",
		tank_id_pass: str = "",
		relative_id: str = "",
		google_id: str = "",
		security_id: str = "",
		a_id: str = "",
		v_id: str = "",
		country_code: str = "",
		machine_address: str = "",
		game_version: float = 0.0,
		platform_id: int32 = PlatformID.UNKNOWN,
		meta: str = "",
		flags: uint32 = 0
	) -> None:
		self.requested_name = requested_name
		self.tank_id_name = tank_id_name
		self.tank_id_pass = tank_id_pass
		self.relative_id = relative_id
		self.google_id = google_id
		self.security_id = security_id
		self.a_id = a_id
		self.v_id = v_id
		self.country_code = country_code
		self.machine_address = machine_address
		self.game_version = game_version
		self.platform_id = platform_id
		self.meta = meta
		self.flags = flags


	def isFlagOn(self, flag: ClientFlags) -> bool:
		return (self.flags & flag)

	def setFlag(self, flag: ClientFlags) -> None:
		self.flags |= flag

	def removeFlag(self, flag: ClientFlags) -> None:
		self.flags &= ~flag

	
	def setRequestedName(self, data: str) -> bool:
		if (
			len(data) > 16
			| len(data) < 1
		):
			return False
		
		self.requested_name = data

		return True
	
	def setTankIDName(self, data: str) -> bool:
		if (
			len(data) > 24
			| len(data) < 1
		):
			return False

		self.tank_id_name = data

		return True
	
	def setTankIDPass(self, data: str) -> bool:
		if (
			len(data) > 24
			| len(data) < 1
		):
			return False
		
		self.tank_id_pass = data

		return True

	def setRelativeID(self, data: str) -> bool:
		if (
			len(data) > 32
			| len(data) < 1
		):
			return False
		
		self.relative_id = data

		return True
	
	def setCountryCode(self, data: str) -> bool:
		if (
			len(data) > 3
			| len(data) < 1
		):
			return False
		
		self.country_code = data

		return True

	
	def serialize(self, parser: TextParser) -> bool:
		if not (
			self.setRequestedName(parser.et("requestedName", 1))
			| self.setCountryCode(parser.Get("country", 1))
			| self.setRelativeID(parser.Get("rid", 1))
		):
			return False
		
		self.game_version = float(parser.Get("game_version", 1))

		platform_id = parser.Get("platformID", 1)
		if len(platform_id < 1):
			return False
		self.platform_id = uint32(platform_id[0])
		
		if self.platform_id < 0:
			return False
		
		return True