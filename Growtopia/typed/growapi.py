__all__ = [
	"GrowAPI"
]


from ..Client import Client


class GrowAPI:
	def __init__(self, client: Client) -> None:
		self.client: Client = client

	
	def onConnect(net_id: int) -> None:
		...

	def onDisconnect(net_id: int) -> None:
		...

	def onRaw(net_id: int, data: bytearray) -> None:
		...