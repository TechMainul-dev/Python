# functions practice
print('--------------------------------')


def last_char(name):
    return name[-1]


print(last_char("Akash"))
print('--------------------------------')


def odd_even(num):
    if num % 2 == 0:
        return "even"
    return "odd"


print(odd_even(11))
print('--------------------------------')


def is_even(num):
    if num % 2 == 0:
        return True
    return False


print(is_even(10))
