# ask a user for name
# Example - Akash Khan
# print count of each words with "for_loop"
# output :
        # A : 1
        # a : 2
        # K : 1
        # k : 1
        # s : 1
        # h : 2

name = "Akash khan" #input("enter your name : ")
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]} : {name.count(name[i])}")
        temp += name[i]