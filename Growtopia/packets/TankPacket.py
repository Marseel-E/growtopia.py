__all__ = [
	"TankPacket"
]


from typed import Tank

from utils import rw

from struct import unpack



TANK_HEADER_SIZE: int = 60


class TankPacket:
	def __init__(self, data: Tank) -> None:
		self.data = Tank(data)


	@staticmethod
	def from_data(data: Tank) -> "TankPacket":
		return TankPacket(data)


	@staticmethod
	def from_bytes(b: bytearray) -> "TankPacket":
		data = Tank(
			rw(b[0:4], 32, "little"), # packetType
			rw(b[4:5], 8), # type
			rw(b[5:6], 8), # punchID
			rw(b[6:7], 8), # buildRange
			rw(b[7:8], 8), # punchRange
			rw(b[8:12], 32, "little"), # netID
			rw(b[12:16], 32, "little"), # targetNetID
			rw(b[16:24], 32, "little"), # state
			rw(b[24:28], 32, "little"), # info
			unpack("<f", b[28:32]), # xPos
			unpack("<f", b[32:36]), # yPos
			unpack("<f", b[36:40]), # xSpeed
			unpack("<f", b[40:48]), # ySpeed
			rw(b[48:50], 32, "little"), # xPunch
			rw(b[50:56], 32, "little") # yPunch
		)

		dataLength: int = rw(b[56:], 32, "little")

		if dataLength > 0:
			data.data = lambda _: data[60:60 + dataLength]

		return TankPacket(data)
	

	def parse(self) -> bytearray:
		if not self.data:
			return
		
		b = bytearray(TANK_HEADER_SIZE)

		b[0] = rw(0x4, 32, "little") # packetType
		b[4] = rw(self.data.type or 0, 8)
		b[5] = rw(self.data.punchID or 0, 8)
		b[6] = rw(self.data.buildRange or 0, 8)
		b[7] = rw(self.data.punchRange or 0, 8)
		b[8] = rw(self.data.netID or 0, 32, "little")
		b[12] = rw(self.data.targetNetID or 0, 32, "little")
		b[16] = rw(self.data.state or 0x8, 32, "little")
		b[24] = rw(self.data.info or 0, 32, "little")
		b[28] = unpack("<f", self.data.xPos or 0)
		b[32] = unpack(self.data.yPos or 0)
		b[36] = unpack(self.data.xSpeed or 0)
		b[40] = unpack(self.data.ySpeed or 0)
		b[48] = rw(self.data.xPunch or 0, 32, "little")
		b[52] = rw(self.data.yPunch or 0, 32, "little")

		if type(self.data.data == function):
			extra = self.data.data()

			if not type(extra) == bytearray:
				return
			
			rw(b[len(extra):56], 32, "little")
			b.extend(extra)

		return b