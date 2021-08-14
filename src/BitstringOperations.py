class BitStringOperations:
	"""
	Description:

		Provides the Bitstring operations used in the compression state and functions of the SHA algorithm.

	Functions:

		joinBits(string) -> string
		lengthOfMessageBits(string) -> string
		strxor(string) -> string
		strrightshift(string) -> string
		strrightrotate(string) -> string
		strand(string) -> string
		strnot(string) -> string
		stradd(string) -> string

	"""

	# Referenced from https://stackoverflow.com/a/40949538
	@staticmethod
	def joinBits(s=''):
		"""Converts a string of ascii characters into a string of bits."""
		return ''.join(bin(ord(x))[2:].zfill(8) for x in s)

	@staticmethod
	def lengthOfMessageBits(length):
		"""Converts a int into a string of bits."""
		return bin(length)[2:].zfill(64)

	@staticmethod
	def strxor(string1, string2):
		"""Xors two bit strings together."""
		return ''.join('0' if string1[index] == string2[index] else '1' for index in range(len(string1)))

	@staticmethod
	def strrightshift(string, amt):
		"""Shifts string right by given amount."""
		return '0' * amt + string[:-amt]

	@staticmethod
	def strrightrotate(string, amt):
		"""Rotates string right by given amount."""
		return string[-amt:] + string[:-amt]

	@staticmethod
	def strand(string1, string2):
		"""Ands two bit strings together."""
		return ''.join('1' if string1[index] == string2[index] and string1[index] == '1' else '0' for index in range(len(string1)))

	@staticmethod
	def strnot(string):
		"""Returns the Not of a string."""
		return ''.join('1' if string[index] == '0' else '0' for index in range(len(string)))

	@staticmethod
	def stradd(string1, string2):
		"""Adds two bit strings together and mods by 2 ^ 32."""
		add = bin(int(string1, 2) + int(string2, 2))[2:].zfill(32)
		return add[len(add)-32:]