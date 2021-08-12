import math



class Sha256:

	first64primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
				 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
				 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311]

	def preprocess(self, string):
		string = self.joinBits(string)
		loM = self.lengthOfMessageBits(len(string))

		string +="1"

		while ((len(string) + 64) % 512 != 0):
			string += "0"

		string += loM

		chunks = [string[i:i+512] for i in range(0, len(string), 512)]

		return chunks

	def joinBits(self, s=''):
		return ''.join(bin(ord(x))[2:].zfill(8) for x in s)

	def lengthOfMessageBits(self, length):
		return bin(length)[2:].zfill(64)

	def strxor(self, string1, string2):
		return ''.join('0' if string1[index] == string2[index] else '1' for index in range(len(string1)))

	def strrightshift(self, string, amt):
		return '0' * amt + string[:-amt]

	def strrightrotate(self, string, amt):
		return string[-amt:] + string[:-amt]

	def strand(self, string1, string2):
		return ''.join('1' if string1[index] == string2[index] and string1[index] == '1' else '0' for index in range(len(string1)))

	def strnot(self, string):
		return ''.join('1' if string[index] == '0' else '0' for index in range(len(string)))

	def stradd(self, string1, string2):
		add = bin(int(string1, 2) + int(string2, 2))[2:].zfill(32)
		return add[len(add)-32:]

	def sigma0(self, E):

		E1 = self.strrightrotate(E, 7)
		E2 = self.strrightrotate(E, 18)
		E3 = self.strrightshift(E, 3)

		result = self.strxor(E1, E2)
		result = self.strxor(result, E3)

		return result

	def sigma1(self, A):

		A1 = self.strrightrotate(A, 17)
		A2 = self.strrightrotate(A, 19)
		A3 = self.strrightshift(A, 10)

		result = self.strxor(A1, A2)
		result = self.strxor(result, A3)

		return result


	def SIGMA0(self, E):

		E1 = self.strrightrotate(E, 2)
		E2 = self.strrightrotate(E, 13)
		E3 = self.strrightrotate(E, 22)
		result = self.strxor(E1, E2)
		result = self.strxor(result, E3)

		return result

	def SIGMA1(self, A):
		
		A1 = self.strrightrotate(A, 6)
		A2 = self.strrightrotate(A, 11)
		A3 = self.strrightrotate(A, 25)
		result = self.strxor(A1, A2)
		result = self.strxor(result, A3)

		return result

	def choice(self, E, F, G):

		EF = self.strand(E, F)
		notE = self.strnot(E)
		notEG = self.strand(notE, G)

		result = self.strxor(EF, notEG)

		return result


	def majority(self, A, B, C):

		AB = self.strand(A, B)
		AC = self.strand(A, C)
		BC = self.strand(B, C)

		result = self.strxor(AB, AC)
		result = self.strxor(result, BC)

		return result

	def genConstants(self, constant="h"):
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

		for prime in self.first64primes[:numPrimes]:

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

	def createMessageSchedule(self, chunk):
		words = [chunk[i:i+32] for i in range(0, len(chunk), 32)]

		for i in range(16, 64):

			s0 = self.sigma0(words[i - 15])
			s1 = self.sigma1(words[i - 2])

			word = self.stradd(words[i - 16], s0)
			word = self.stradd(word, words[i - 7])
			word = self.stradd(word, s1)

			words.append(word)

		return words


	def hash(self, chunks):

		hlist = self.genConstants("h")
		klist = self.genConstants("k")

		for chunk in chunks:

			words = self.createMessageSchedule(chunk)

			a = hlist[0]
			b = hlist[1]
			c = hlist[2]
			d = hlist[3]
			e = hlist[4]
			f = hlist[5]
			g = hlist[6]
			h = hlist[7] 

			for i in range(64):
				S1 = self.SIGMA1(e)
				ch = self.choice(e, f, g)

				temp1 = self.stradd(h, S1)
				temp1 = self.stradd(temp1, ch)
				temp1 = self.stradd(temp1, klist[i])
				temp1 = self.stradd(temp1, words[i])
				S0 = self.SIGMA0(a)
				maj = self.majority(a, b, c)
				temp2 = self.stradd(S0, maj)

				h = g
				g = f
				f = e
				e = self.stradd(d, temp1)
				d = c
				c = b
				b = a
				a = self.stradd(temp1, temp2)

			hlist[0] = self.stradd(hlist[0], a)
			hlist[1] = self.stradd(hlist[1], b)
			hlist[2] = self.stradd(hlist[2], c)
			hlist[3] = self.stradd(hlist[3], d)
			hlist[4] = self.stradd(hlist[4], e) 
			hlist[5] = self.stradd(hlist[5], f)
			hlist[6] = self.stradd(hlist[6], g)
			hlist[7] = self.stradd(hlist[7], h)

		hashed = ""
		for x in hlist:
			hashed += (hex(int(x, 2))[2:])

		print(hashed)
