from random import *
import string

print("Upper case ",string.ascii_uppercase)
print("Digit ", string.digits)

def gen_password(pwd_length):

    pwd = ""

    for i in range(pwd_length):
        if random() > 0.4:
            pwd += choice(string.ascii_letters)
        else:
            pwd += choice(string.digits)
    return pwd
    
print("password length 5 ",gen_password(5))
print("password length 20 ",gen_password(20))