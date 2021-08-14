from BitstringOperations import BitStringOperations

class Preprocessor:

	"""
	Description:

		Splits a string into a list of strings with a size of 512 bits.

	Functions:

		preproces(string) -> [strings]

	"""

	@staticmethod
	def preprocess(string):
		"""Splits the string into 512 bit sections by adding padding if length is not a multiple of 512 and adds the length of the message in bits to the end."""

		string = BitStringOperations.joinBits(string)
		loM = BitStringOperations.lengthOfMessageBits(len(string))

		string +="1"

		while ((len(string) + 64) % 512 != 0):
			string += "0"

		string += loM

		chunks = [string[i:i+512] for i in range(0, len(string), 512)]

		return chunks