__all__ = [
	"parseText"
]


from typing import Union


def parseText(chunk: bytearray) -> dict[str, Union[str, int]]:
	data: dict[str, Union[str, int]] = {}
	
	chunk[len(chunk) - 1] = 0

	a: str = str(chunk[4:])
	lines: list[str] = a.split("\n")

	for line in lines:
		if line.startswith("|"):
			line = line[1:]

		info: list[str] = line.split("|")

		key: str = info[0]
		value: str = info[1]

		if key and value:
			if value.endswith("\x00"):
				value = value[0:-1]
			
			data[key] = value

	return data
