def greater(a, b):
    if a > b:
        return a
    else:
        return b


a = int(input("Enter Your 1st number : "))
b = int(input("Enter Your 2nd number : "))
print(f"{greater(a, b)} are greater")
