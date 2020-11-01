# ask user a number like 1256
# calculate sum of digits ---? 1 + 2 + 5 + 6
# logic

total = 0
num = ("1342") # input("enter a number : ")
for i in range(0, len(num)):
    total += int(num[i])
print(total)