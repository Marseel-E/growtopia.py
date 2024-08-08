__all__ = ('TextParser')


class TextParser:
	def __init__(
		self,
		data: str = "",
	) -> None:
		self.data: list[str] = self.parse(data)


	def stringTokenize(self, data: str, delimiter: str = "|") -> list[str]:
		tokens: list[str] = []
		pre_i: int = 0
		i: int = 0

		while (
			i < len(data)
			& pre_i < len(data)
		):
			i = data.find(delimiter, pre_i)
			if i == -1:
				i = len(data)

			token: str = data[pre_i:i - pre_i]
			if not (token == ""):
				tokens.append(token)

			pre_i = i + len(delimiter)

		return tokens

	
	def parse(self, data: str) -> None:
		self.data = self.stringTokenize(data, "\n")

		# MEH
		for d in self.data:
			if d == "\r":
				self.data.remove(d)


	def get(self, key: str, index: int = 1, token: str = "|", key_index: int = 0) -> str:
		if self.data == []:
			return ""
		
		for d in self.data:
			if d == "":
				continue

			tokenize: list[str] = self.stringTokenize(d, token)

			if tokenize[key_index] != key:
				continue

			if (
				index < 0
				| index >= len(tokenize)
			):
				return ""
			
			return tokenize[key_index + index]
		
		return ""


	def add(self, key: str, value: str, token: str = "|") -> None:
		self.data.append(key + token + value)

	
	def set(self, key: str, value: str, token: str = "|") -> None:
		if self.data == []:
			return
		
		for d in self.data:
			tokenize: list[str] = self.stringTokenize(d, token)

			if tokenize[0] != key:
				continue

			d = str(tokenize[0])
			d += token
			d += value

			break


	def contain(self, key: str) -> bool:
		return (self.get(key) != "")
	

	def isEmpty(self) -> bool:
		return (self.data == [])

	def getSize(self) -> int:
		return len(self.data)

	def getAsString(self) -> str:
		return '\n'.join(self.data)