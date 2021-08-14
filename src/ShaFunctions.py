from BitstringOperations import BitStringOperations

class ShaFunctions:
	"""
	Description:

		Provides the functions used in the compression state of the SHA algorithm.

	Functions:

		sigma0(string) -> string
		sigma1(string) -> string
		SIGMA0(string) -> string
		SIGMA1(string) -> string
		choice(string, string, string) -> string
		majority(string, string, string) -> string

	"""

	@staticmethod
	def sigma0(E):
		"""Takes in a string and outputs a string with operations applied."""

		E1 = BitStringOperations.strrightrotate(E, 7)
		E2 = BitStringOperations.strrightrotate(E, 18)
		E3 = BitStringOperations.strrightshift(E, 3)

		result = BitStringOperations.strxor(E1, E2)
		result = BitStringOperations.strxor(result, E3)

		return result

	@staticmethod
	def sigma1(A):
		"""Takes in a string and outputs a string with operations applied."""

		A1 = BitStringOperations.strrightrotate(A, 17)
		A2 = BitStringOperations.strrightrotate(A, 19)
		A3 = BitStringOperations.strrightshift(A, 10)

		result = BitStringOperations.strxor(A1, A2)
		result = BitStringOperations.strxor(result, A3)

		return result

	@staticmethod
	def SIGMA0(E):
		"""Takes in a string and outputs a string with operations applied."""

		E1 = BitStringOperations.strrightrotate(E, 2)
		E2 = BitStringOperations.strrightrotate(E, 13)
		E3 = BitStringOperations.strrightrotate(E, 22)
		result = BitStringOperations.strxor(E1, E2)
		result = BitStringOperations.strxor(result, E3)

		return result

	@staticmethod
	def SIGMA1(A):
		"""Takes in a string and outputs a string with operations applied."""
		
		A1 = BitStringOperations.strrightrotate(A, 6)
		A2 = BitStringOperations.strrightrotate(A, 11)
		A3 = BitStringOperations.strrightrotate(A, 25)
		result = BitStringOperations.strxor(A1, A2)
		result = BitStringOperations.strxor(result, A3)

		return result

	@staticmethod
	def choice(E, F, G):
		"""Takes in three strings and uses the first string to choose whether or not to take the bit of the second or third string."""

		EF = BitStringOperations.strand(E, F)
		notE = BitStringOperations.strnot(E)
		notEG = BitStringOperations.strand(notE, G)

		result = BitStringOperations.strxor(EF, notEG)

		return result

	@staticmethod
	def majority(A, B, C):
		"""Takes in three strings and takes which bits have the most occurances."""

		AB = BitStringOperations.strand(A, B)
		AC = BitStringOperations.strand(A, C)
		BC = BitStringOperations.strand(B, C)

		result = BitStringOperations.strxor(AB, AC)
		result = BitStringOperations.strxor(result, BC)

		return result