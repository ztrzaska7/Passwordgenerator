import string
import random
def generate_password(length):
    characters=string.ascii_lettersstring.digits+string.punctuation
    password="".join(random.choice(characters) for _ in range(length))
    return password
length=int(input("Put password's length: "))
password=generate_password(length)
print(f"Generated password is: {password}")

