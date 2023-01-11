import random
import string

def password_generator(length, characters):
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password

if __name__ == '__main__':
    length = int(input("Enter the desired length of the password: "))
    use_uppercase = input("Include uppercase letters? (y/n) ")
    use_lowercase = input("Include lowercase letters? (y/n) ")
    use_numbers = input("Include numbers? (y/n) ")
    use_special_characters = input("Include special characters? (y/n) ")

    characters = ""
    if use_uppercase == 'y':
        characters += string.ascii_uppercase
    if use_lowercase == 'y':
        characters += string.ascii_lowercase
    if use_numbers == 'y':
        characters += string.digits
    if use_special_characters == 'y':
        characters += string.punctuation

    print("Your password is: ", password_generator(length, characters))