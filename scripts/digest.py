import hashlib

word = "SLASH"

sha256 = hashlib.sha256(word.encode()).hexdigest()
md5 = hashlib.md5(word.encode()).hexdigest()
sha1 = hashlib.sha1(word.encode()).hexdigest()

print("SHA-256:", sha256)
print("MD5:", md5)
print("SHA-1:", sha1)
