import random
chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
l=int(input("Enter password length: "))
n=int(input("Enter number of passwords: "))
for i in range(n):
    password=''
    for j in range(l):
        password+=random.choice(chars)
    print(password)