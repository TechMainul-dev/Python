# replace() method
# find () method

string = "She is beautiful and she is good singer"
# string.replace(" ","_")
# print(string.replace(" ","_"))
# print(string.replace("is","was"))
replace = string.replace("is","was", 2)
print(f"\n_____When 'is' replace with 'was' :______\n{replace}")


# string.find("is")
# print(string.find("is"))
# print(string.find("is", 1))

is_pos1 = string.find("is") # is pos1 ---> number
# is_pos2 = string.find("is",is_pos1) #wrong search

is_pos2 = string.find("is",is_pos1+1)
print(f"2nd 'is' position : {is_pos2}")