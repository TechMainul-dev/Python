# functions practice
print('------return last letter---------')
name = input("input your name : ")


def last_char(name):
    return name[-1]


print(last_char(name))
# ------------------------------------------
print('--------Even or Odd detected------')
num = int(input("Enter your number : "))


def odd_even(num):
    if num % 2 == 0:
        return "even"
    return "odd"


print(odd_even(num))
# ------------------------------------------
print('---------boolean output-----------')


def is_even(num):
    return num % 2 == 0  # True


print(is_even(num))
print('---------greeting---------')


def greeting():
    return "Thank you very much"


print(greeting())
