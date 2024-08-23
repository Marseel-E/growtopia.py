__all__ = [
	"Tank",
	"Sendable"
]


from typing import TypedDict

from packets import (
	TankPacket,
	TextPacket,
	Variant
)


class Tank(TypedDict):
	packetType: int
	type: int
	punchID: int
	buildRange: int
	punchRange: int
	netID: int
	targetNetID: int
	state: int
	info: int
	xPos: float
	yPos: float
	xSpeed: float
	ySpeed: float
	xPunch: int
	yPunch: int
	def data() -> bytearray: ...


class Sendable(TypedDict):
	...