import random

caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
c=int(input("ingrse el numero de caracteres que va a tener la contraseña:"))
password=""
for i in range(c):
    password+=random.choice(caracteres)
print("su contraseña sera:",password)




 