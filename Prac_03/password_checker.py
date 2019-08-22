MIN_LENGTH = 4
def main():
    password = get_password()
    astericks_creation(password)


def astericks_creation(password):
    for letters in password:
        print("*", end="")


def get_password():
    password = input("Please enter a password")
    while len(password) < MIN_LENGTH:
        password = input("Please enter a password with four or more letters")
    return password


main()
