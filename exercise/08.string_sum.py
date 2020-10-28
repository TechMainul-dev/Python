# ask user to input a number containing more than one digit
# example - 1256
# calculate 1+2+5+6 and print
# int(x[i]) +


x = input("input a number more than one digit : ")

total, j = 0, 0
  
while j < len(x):
    total += int(x[j])
    j += 1
print(f"{' + '.join(x[i:i + 1] for i in range(0, len(x), 1))} = {total}")