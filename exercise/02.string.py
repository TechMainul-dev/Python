#Exercise_02
# Ask user to input 3 numbers and you have to print average of three numbers using string formatting.

# x, y, z = int(input("input '3' number like separated x, y, z : ").split(","))

x = int(input("x = "))
y = int(input("x = "))
z = int(input("x = "))
print()

print(f"when, \nx = {x}, y = {y}, z = {z}")
print(f"so,\nx + y + z = {x} + {y} + {z}")
total = x + y + z
print(f"total = {total}")
average = total //3
print(f"average = {average}")


#total = x + y + z
#print(str(total))


# name, age = input("enter your name,age : ").split(",")