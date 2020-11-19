# break and continue keyword

# 1 to 10 print
print("Break keyword\n")

for i in range(1, 11):
    if i == 5:
        break
    print(i)
print("________________\n")
print("Continue keyword :")

for i in range(1, 11):
    if i == 9:
        continue
    print(i)
