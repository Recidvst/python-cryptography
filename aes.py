
# Crypto library currently not working!! Python version wrong? 64 vs 32?
from Crypto.Cipher import AES

key = "A test cipher key"
plain = "A super secret message"

cipher = AES.new(key)
ciphertext = cipher.encrypt(plain)

print(ciphertext.encode("hex"))