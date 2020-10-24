# Exercise - Watch COCO
# Ask user's name and age
# if user's name start with ('a' or 'A') and age is above 10 then print "you can watch coco movie"
# Else print 'sorry', you can't watch coco

first_letter, age = 'a', 10

#input type (01)-------------------------------------------->>>>>>
# user_name = input("enter your name : ")
# user_age = int(input("enter your age : "))

#input type (02)-------------------------------------------->>>>>>
user_name, user_age = input("Enter your Name, age with comma separated : ").split(",")

print("Result-------------------->")

#condition type (01)-------------------------------------------->>>>>>
# if first_letter == user_name.lower()[:1] and age <= int(user_age):
#     print("you can watch coco movie")
# else:
#     print("Sorry")

#condition type (02)-------------------------------------------->>>>>>
print("you can watch coco movie") if first_letter == user_name.lower()[:1] and age <= int(user_age) else print("Sorry")
    