# ask a user for name
# Example - Akash Khan
# print count of each words
# output :
        # A : 1
        # a : 2
        # K : 1
        # k : 1
        # s : 1
        # h : 2

name = ("Akash khan")
temp_var = ""
i = 0
# x = name[0] 
# y = name.count(name[0])

while i < len(name):
    if name[i] not in temp_var: 
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1

