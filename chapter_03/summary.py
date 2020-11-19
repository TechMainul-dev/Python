print('\n______if statement______\n')
name = "khan"
if name == "Akash" or name == "akash":
    print("You are Akash")
elif name == "khan" or name == "Khan":
    print("Your are khan")
else:
    print("You are not Akash or Khan")
# ====================================
print('\n______While loop______\n')
i = 1
while i <= 10:
    print(f"{i} {name}")
    i += 1
# ====================================
print('\n______for loop______\n')
for i in range(1, 11, 2):
    print(i)
# ====================================
print('\n______break keyword______\n')
for i in range(1, 11):
    if i == 5:
        break
    print(i)
