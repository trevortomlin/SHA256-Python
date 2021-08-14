import math

class ConstantGenerator:

	"""
	Description:

		Generates the constants used for the hash.

	Functions:

		genConstants(string) -> [strings]

	"""

	@staticmethod 
	def genConstants(constant="h"):
		"""Takes a string denoting which constant to generate and returns a list of appropriate size"""

		first64primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
				     101,103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
				     199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311]

		# constant = h or k

		if constant == "h":

			root = 1/2
			numPrimes = 8

		elif constant == "k":

			root = 1/3
			numPrimes = 64

		else:
			 raise Exception("Constant Variable is not valid.")

		constants = []

		for prime in first64primes[:numPrimes]:

			rtprime = prime ** root

			binstring = ""

			fractional = (rtprime - math.floor(rtprime))

			for x in range(8):

				product = fractional * 16
				carry = math.floor(product)
				fractional = product - math.floor(product)
				binstring += bin(carry)[2:].zfill(4)

			constants.append(binstring)

		return constants