import random

def PasswordGenerator():
    Password=""
    rand_chara=random.randint(8, 24)
    print(f"Password conatins {rand_chara} characters.\n")
    for _ in range (0,rand_chara):
        _ = random.randint(32, 125)
        character=chr(_)
        Password=Password+character
    print(Password)
    return Password
PasswordGenerator()