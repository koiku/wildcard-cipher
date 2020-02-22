from key import *

print("Enter the encoded string")
string = input("> ")

primary_str = string.split(KEY)
result = ''.join(primary_str)

print("\nSource string: {}".format(result.replace(SPACE, " ")))