from .enums import *
from .parser import *

def rw(a, c, b = "big") -> int:
	return int.from_bytes(a, b, c)