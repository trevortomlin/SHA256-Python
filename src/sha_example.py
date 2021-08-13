import hashlib
from SHA256Hash import Sha256
# https://stackoverflow.com/a/40949538



def main():

	string = ""
	print(hashlib.sha256(string.encode()).hexdigest())

	sha = Sha256()
	
	sha.hash(string)
	#print(sha.binDigest())
	print(sha.hexDigest())


if __name__ == "__main__":
	main()