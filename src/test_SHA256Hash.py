import unittest
from SHA256Hash import Sha256
import hashlib

# Sha256 Test Vectors From https://www.di-mgt.com.au/sha_testvectors.html

class TestSha256Hash(unittest.TestCase):

	def test_hash(self):

		sha = Sha256()

		string = ""
		sha.hash(string)
		testhash = sha.hexDigest()
		realhash = hashlib.sha256(string.encode()).hexdigest()
		self.assertEqual(testhash, realhash)

		string = "abc"
		sha.hash(string)
		testhash = sha.hexDigest()
		realhash = hashlib.sha256(string.encode()).hexdigest()
		self.assertEqual(testhash, realhash)

		string = "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq"
		sha.hash(string)
		testhash = sha.hexDigest()
		realhash = hashlib.sha256(string.encode()).hexdigest()
		self.assertEqual(testhash, realhash)

		string = "abcdefghbcdefghicdefghijdefghijkefghijklfghijklmghijklmnhijklmnoijklmnopjklmnopqklmnopqrlmnopqrsmnopqrstnopqrstu"
		sha.hash(string)
		testhash = sha.hexDigest()
		realhash = hashlib.sha256(string.encode()).hexdigest()
		self.assertEqual(testhash, realhash)

		string = 'a' * 1_000_000
		sha.hash(string)
		testhash = sha.hexDigest()
		realhash = hashlib.sha256(string.encode()).hexdigest()
		self.assertEqual(testhash, realhash)