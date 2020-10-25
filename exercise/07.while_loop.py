# exercise one of three
# sum of n natural number
# ask a user for natural number(n)
# print total from 1 to n

n = int(input("enter  a natural number : "))

total, i = 0, 1

while i <= n:
    total += i
    i += 1
print(f"sum of 1 to {n} = {total} ")
