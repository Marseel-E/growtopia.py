__all__ = [
	"TextPacket"
]


from utils import rw


class TextPacket:
	def __init__(self, _type: int, text: list[str]) -> None:
		self.type = _type
		self.text = text


	@staticmethod
	def from_bytes(packet: bytearray) -> "TextPacket":
		if len(packet) < 4:
			raise Exception("Invalid packet recieved.")
		
		_type: int = rw(packet[0:4], 32, "little")
		text: str = packet[4:-1] or ""

		return TextPacket(_type, text)
	

	def parse(self) -> bytearray:
		text: str = self.text.join("\n")
		data = bytearray(4 + len(text) + 1) # +1 for null terminator

		data[0] = rw(self.type, 32, "little")
		data[4] = text

		return data