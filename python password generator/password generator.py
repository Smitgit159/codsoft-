import random
import string

def generate_password(length=10, complexity="hard"):
    if complexity == "easy":
        chars = string.ascii_letters + string.digits
    elif complexity == "medium":
        chars = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "hard":
        chars = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
    
    password = "".join(random.choice(chars) for i in range(length))

    return password

password_length = 10
password_complexity = "hard"
generate_password = generate_password(password_length, password_complexity)
print(generate_password)



    