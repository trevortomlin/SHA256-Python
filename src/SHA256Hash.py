import math
from Preprocessor import Preprocessor
from WordSchedule import WordSchedule
from ConstantGenerator import ConstantGenerator
from ShaFunctions import ShaFunctions
from BitstringOperations import BitStringOperations

class Sha256:

	"""
	Description:

		Hashes a string using SHA256

	Functions:

		hash(string)
		binDigest() -> string
		hexDigest() -> string

	"""

	hashed = ""

	def hash(self, string):
		"""Takes a string and hashes it use SHA256."""

		self.hashed = ""

		chunks = Preprocessor.preprocess(string)

		hlist = ConstantGenerator.genConstants("h")
		klist = ConstantGenerator.genConstants("k")

		for chunk in chunks:

			words = WordSchedule.createMessageSchedule(chunk)

			a = hlist[0]
			b = hlist[1]
			c = hlist[2]
			d = hlist[3]
			e = hlist[4]
			f = hlist[5]
			g = hlist[6]
			h = hlist[7] 

			for i in range(64):
				S1 = ShaFunctions.SIGMA1(e)
				ch = ShaFunctions.choice(e, f, g)

				temp1 = BitStringOperations.stradd(h, S1)
				temp1 = BitStringOperations.stradd(temp1, ch)
				temp1 = BitStringOperations.stradd(temp1, klist[i])
				temp1 = BitStringOperations.stradd(temp1, words[i])
				S0 = ShaFunctions.SIGMA0(a)
				maj = ShaFunctions.majority(a, b, c)
				temp2 = BitStringOperations.stradd(S0, maj)

				h = g
				g = f
				f = e
				e = BitStringOperations.stradd(d, temp1)
				d = c
				c = b
				b = a
				a = BitStringOperations.stradd(temp1, temp2)

			hlist[0] = BitStringOperations.stradd(hlist[0], a)
			hlist[1] = BitStringOperations.stradd(hlist[1], b)
			hlist[2] = BitStringOperations.stradd(hlist[2], c)
			hlist[3] = BitStringOperations.stradd(hlist[3], d)
			hlist[4] = BitStringOperations.stradd(hlist[4], e) 
			hlist[5] = BitStringOperations.stradd(hlist[5], f)
			hlist[6] = BitStringOperations.stradd(hlist[6], g)
			hlist[7] = BitStringOperations.stradd(hlist[7], h)


		for x in hlist:
			self.hashed += x

	def binDigest(self):
		"""Returns the binary data of the hash."""
		return(self.hashed.zfill())

	def hexDigest(self):
		"""Returns the hex data of the hash."""
		return(hex(int(self.hashed, 2))[2:].zfill(64))