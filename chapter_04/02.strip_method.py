name = "    Akash Khan   "
dots = ".............."
# lstrip()-method
print(name + dots)
print(name.lstrip() + dots) # remove only left space
print(name.rstrip() + dots) # remove only right space
print(name.strip() + dots) # remove left & right space
print(name.replace(" ","") + dots) # replace all space 