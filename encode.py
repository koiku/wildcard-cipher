from key import *
print("Enter string to encode")
string = input("> ")

result = ''

for char in string:
	if char == " ":
		result += SPACE
		continue
	result += char + KEY

print("\nEncoded string: {}".format(result))