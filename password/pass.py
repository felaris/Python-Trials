import string
import random
import math

# Function for the Password Gererating


def generate():
    for i in range(1, 99):

        s1 = string.ascii_uppercase

        s2 = string.ascii_lowercase

        s3 = string.digits

        #s4 = [',',',']

        # Password Lenght
        passlen = input ("type in the password lenght ")

        passlen = int(passlen)

        s = []
        s.extend(list(s1))

        s.extend(list(s2))

        s.extend(list(s3))

        s.extend(list(s4))
        # print(s)

        random.shuffle(s)
        # print(s)
        password = ("".join(s[0:passlen]))
        # print(password)
        output = open("Passwords4.txt", "a")
        # This writes outputs on a new line
        output.write(password + "\n")
        output.close()


generate()
