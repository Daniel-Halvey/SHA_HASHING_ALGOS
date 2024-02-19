# Exploring Hashing Algorithms (Educational only, not secure)

# Use placeholder names and generic statements
str = "A fictional person created their first program in a programming language"

# SHA-256 (Secure for some non-critical uses)
result = hashlib.sha256(str.encode()).hexdigest()
print(f"SHA-256 hash: {result}")

# SHA-384 (More secure than SHA-256)
result = hashlib.sha384(str.encode()).hexdigest()
print(f"SHA-384 hash: {result}")

# Briefly explain why SHA-1 is unsuitable for security
print("\nSHA-1 is not recommended for security purposes due to known vulnerabilities.\n")

# Explain the meaning of the generated hashes and their limitations
print("These hashes are unique fingerprints of the input string, but remember:")
print("- They are not reversible, meaning you cannot get the original string from the hash.")
print("- Changing even a single character in the string will result in a completely different hash.")

print("\nUse strong hashing algorithms like bcrypt or Argon2 for sensitive data!")
