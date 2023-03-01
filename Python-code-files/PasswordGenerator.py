from random import choice, shuffle
import string
 
def generate_strong_password(a,b,c):
    list = ["!","?","=","+","-","(",")","#"]
    str = ""
    for i in range(len(list)):
        char = list[i]
        str += char
    digits = string.digits
    letters = string.ascii_lowercase
    alphabet1 = letters
    alphabet2 = digits + letters
    alphabet3 = digits + str + letters
    alphabet4 = letters + str
    password = ''
    for i in range(a):
        if b == False and c == False:
            password += choice(alphabet1)
        elif b == True and c == False:
            password += choice(alphabet2)
        elif c == True and b == False:
            password += choice(alphabet4)
        else:
            password += choice(alphabet3)
    return password
 
if __name__ == "__main__":  
    for i in range(5):
        print(generate_strong_password(5, True, False))
