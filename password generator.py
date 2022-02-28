# lauren cook
# feb 25 2022
# password generator lab
import random
import string
symbol = ["!", "?", ":", "$", "&"]
number = ["0","1","2","3","4","5","6","7","8","9"]
letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print("Welcome to the passwordy generator")
length = int(input("Enter a digit for the length of your password. It is case sensitive: "))
if length == int():
    print("Your password will be" + length + " digits long.")
elif not int:
    print("Please type a valid digit.")
    
symbol_use = str(input("Do you want symbols in your password? Type 'yes' or 'no'. It is case sensitive: "))
if symbol_use == "yes" :
    all = symbol + number + letter
    temp = random.sample(all, length)
    passwordy = "".join(temp)
    print(passwordy)
elif symbol_use == "no":
    pee = random.sample(number + letter, length)
    passwordy = "".join(pee)
    print(passwordy)              

