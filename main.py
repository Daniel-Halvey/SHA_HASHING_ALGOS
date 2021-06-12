import hashlib
#input the strings you need encrypted where you see "str ="
print("          Daniel Halvey is working with Hashing Algorithms on 6/12/2021 11:47 am")


str = "Let's_encrypt_Daniel"

# using encode() and sha256
result = hashlib.sha256(str.encode())

# hexadecimal output
print("The hexadecimal value of SHA256 is : ")
print(result.hexdigest())

print("\r")


str = "Daniel can code"

# using encode() and sha384
result = hashlib.sha384(str.encode())

# hexadecimal output
print("The hexadecimal value of SHA384 is : ")
print(result.hexdigest())

print("\r")


str = "Learning to encrypt is easy"


# using encode() and sha224
result = hashlib.sha224(str.encode())

# hexadecimal output
print("The hexadecimal value of SHA224 is : ")
print(result.hexdigest())

print("\r")


str = "Daniel created his first program in JavaScript at USFSP With his favorite computer scientist"
# using encode() and sha512()
result = hashlib.sha512(str.encode())

# hexadecimal output
print("The hexadecimal value of SHA512 is : ")
print(result.hexdigest())

print("\r")

# Final Hash SHA1
str = "Final Hash in this Program SHA1"

# using encode() and sha1
result = hashlib.sha1(str.encode())

# hexadecimal output
print("The hexadecimal value  of SHA1 is : ")
print(result.hexdigest())
print("\r")
print("\r")
print("******")
print("*****")
print("****")
print("***")
print("*")
print("**")
print("***")
print("****")
print("*****")
#Daniel Halvey






print("This is a wonderful program for understanding different was to hash strings")