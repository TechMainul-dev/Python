# ask user to input a number containing more than one digit
# example - 1256
# calculate 1+2+5+6 and print

x = input("input a number more than one digit : ")

# int(x[i]) +

total, i, j = 0, 0, 0
# y = (f"{x[0]} + {x[1]} + {x[2]} + {x[3]}")

y = x[0:1] + "+" + x[1:2]

while j < len(x):
    y = x

while i < len(x):
    total += int(x[i])
    i += 1
print(f"{y} = {total}")