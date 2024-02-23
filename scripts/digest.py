import hashlib

word = "SLASH"

# SHA-256
sha256_hashed_word = hashlib.sha256(word.encode()).hexdigest()

# MD5
md5_hashed_word = hashlib.md5(word.encode()).hexdigest()

# SHA-1
sha1_hashed_word = hashlib.sha1(word.encode()).hexdigest()

print("Original word:", word)
print("SHA-256 Hashed word:", sha256_hashed_word)
print("MD5 Hashed word:", md5_hashed_word)
print("SHA-1 Hashed word:", sha1_hashed_word)
