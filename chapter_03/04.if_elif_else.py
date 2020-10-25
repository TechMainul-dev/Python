# if elif else statement 

# show ticket pricing 
# age: 
# 1 to 3  (free)
# 4 to 10 (150 tk)
# 11 to 60 (250 tk)
# above 60 (200 tk)

age = int(input("enter your age : "))

if age <= 0:
    print("age input error")
elif 1 <= age <= 3:
    print("ticket price : free")
elif 4 <= age <= 10:
    print("ticket price : 150 taka")
elif 11 <= age <= 60:
    print("ticket price : 250 taka")
else:
    print("ticket price : 200 taka")