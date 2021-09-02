# name, age = "Akash", 27
# print("Your Name is : " + name + " \n your age is : " + str(age))
# ___________________________________________________________________

# name, age = input("enter your name & age: ").split(",")
# print(name)
# print(age)
# ___________________________________________________________________

# print("Hello {}, your age is {}".format(name, age)) this is for python 3.0
# print(f"Hello {name}, your age is {age}") #this is for python 3.0
# ___________________________________________________________________

# num1, num2, num3 = 2, 3, 4
# total = num1 + num2 + num3
# print(f"total is : {total}")
# print(f"Average number is :{total/3}")
# ___________________________________________________________________

# num1, num2, num3 = 1,2,3
# # num1, num2, num3 = input("Enter three number separated by comma :").split(",")

# print(f"Total number is :{(int(num1) + int(num2) + int(num3))} \n& Average number is : {(int(num1) + int(num2) + int(num3)) / 3}")
# ___________________________________________________________________

# name = "Akash Khan"
# print(name[-7])
# print(name[7])

# --------String slicing
# print(name[2:8])
# print(name[2:])
# print(name[:8])

# --------step argument
#print("Akash khan"[0:8])
# print("Akash khan"[0:8:2])  # --third letter skip steps
# print("Akash khan"[3::-1])  # --backword

# ---Exercise
# name = input("Enter your name :")
# print(f"reverse of your name is :{name[::-1]}")
# _____________________________________________________________

# # --String method part-1

# # len function
# print(len(name))
# print(len("Akash khan"))

# # lower method
# print(name.lower())

# # Upper method
# print(name.upper())

# # title method
# print(name.title())

# # Count method
# print(name.count("a"))
# ----------------------------------------------------------------
# name, char = "Akash khAn", "A"
# # name, char = input("Enter comma separeted Name & Character :").split(",")


# print(f"Lenth of your name :{len(name.lower())}")
# print(f"Character count :{name.lower().count(char.strip().lower())}")

#--Replace & find method
