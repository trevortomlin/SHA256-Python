from ShaFunctions import ShaFunctions
from BitstringOperations import BitStringOperations

class WordSchedule:

	"""
	Description:

		Creates the 64 words for the hashing function.

	Functions:

		createMessageSchedule(chunk) -> [strings]

	"""

	@staticmethod
	def createMessageSchedule(chunk):
		"""Takes a chunk of size 512 bits and returns a list of 64 words."""
		words = [chunk[i:i+32] for i in range(0, len(chunk), 32)]

		for i in range(16, 64):

			s0 = ShaFunctions.sigma0(words[i - 15])
			s1 = ShaFunctions.sigma1(words[i - 2])

			word = BitStringOperations.stradd(words[i - 16], s0)
			word = BitStringOperations.stradd(word, words[i - 7])
			word = BitStringOperations.stradd(word, s1)

			words.append(word)

		return words