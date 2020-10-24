# take two comma separated inputs from user
# 1. user's name
# 2. a single character

# Output - 2 print lines
# 1. user's name length
# 2. count the character that user inputted (case insensitive count)

name, char = input("Enter your Name, Character with comma separated : ").split(",") 

print(f"Name length with left/right space: {len(name)}") 
print(f"Character count when case sensitive: {name.count(char.strip())}") # case sensitive

print()
# name.lower().count(char.lower())
# print(name.strip() + dots)
print(f"Name length without space: {len(name.strip())}") 
print(f"Character count when case insensitive: {name.lower().count(char.strip().lower())}") # removed (input) left & right spaces