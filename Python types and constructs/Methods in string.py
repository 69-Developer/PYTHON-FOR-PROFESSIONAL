# capitalize - Capital the first word of string

globalstring = "this is a global STRING"

print(globalstring.capitalize())

# lower - return entire string in lower case

print(globalstring.lower())

# upper - return entire string in upper case

print(globalstring.upper())

# Startswith - return does the string starting with given argument [argument is case sensative]

print(globalstring.startswith("this"))

# endswith - return does the string ending with given argument [argument is case sensative]

print(globalstring.endswith("STRING"))

# Replace the given arguments but do not change the string

print(globalstring.replace("STRING","CHARACTER"))

# split the string into element and form a list

print(globalstring.split())

x = "THIS"

print(x.split())

# Join function

array = ["a","b","c"]

print(array)

print(''.join(array))
print('+'.join(array))