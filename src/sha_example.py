import hashlib
from SHA256Hash import Sha256
# https://stackoverflow.com/a/40949538



def main():

	string = "abc"
	print(hashlib.sha256(string.encode()).hexdigest())

	# OUTPUT OF REAL HASH IN BINARY
	# 1011101001111000000101101011111110001111000000011100111111101010010000010100000101000000110111100101110110101110001000100010001110110000000000110110000110100011100101100001011101111010100111001011010000010000111111110110000111110010000000000001010110101101

	sha = Sha256()
	a = sha.preprocess(string)
	sha.hash(a)
	
	# CONVERT HEX TO BINARY
	# hx = (bin(int("0x6a09e667", 16))[2:]).zfill(32)
	# print(hx)

	# CONVERT BINARY STRING TO HEX
	#print(hex(int('10111001010011010010011110111001', 2)))


if __name__ == "__main__":
	main()