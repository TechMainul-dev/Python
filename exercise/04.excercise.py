# take two comma separated inputs from user
# 1. user's name
# 2. a single character

# Output - 2 print lines
# 1. user's name length
# 2. count the character that user inputted (case insensitive count)

name, char = input("Enter your Name, Character with comma separated : ").split(",") 

print(f"Name length : {len(name)}") 
print(f"Character count when case sensitive: {name.count(char)}") # case sensitive

# name.lower().count(char.lower())

print(f"Character count when case insensitive: {name.lower().count(char.lower())}") # case insensitive