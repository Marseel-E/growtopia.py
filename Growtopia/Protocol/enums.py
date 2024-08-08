__all__ = (
	'PlatformID',
	'ClientFlags',
	'PlayerFlags'
)


from enum import IntEnum


class PlatformID(IntEnum):
	UNKNOWN = -1
	WINDOWS = 0
	IOS = 0
	OSX = 0
	LINUX = 0
	ANDROID = 0
	WINDOWS_MOBILE = 0
	WEBOS = 0
	BBX = 0
	FLASH = 0
	HTML5 = 0
	MAXVAL = 0


class ClientFlags(IntEnum):
	LOGGED_ON = (1 << 0)
	IS_IN = (1 << 1)
	UPDATING_ITEMS = (1 << 2)
	UPDATING_TRIBUTE = (1 << 3)
	IS_FACING_LEFT = (1 << 4)


class PlayerFlags(IntEnum):
	IS_INVISIBLE = (1 << 0)
	IS_MOD = (1 << 1)
	IS_SUPER_MOD = (1 << 2)