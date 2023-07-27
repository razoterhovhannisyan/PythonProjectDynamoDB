import re
def validator(func):
    def wrapper(password=None):
        if password is None:
            password = input("Type password:")

        if len(password) < 8:
            print("Invalid password less than 8 digits:Write password again:")
            return wrapper()

        if not any(char.isupper() for char in password):
            print("Invalid password:Must contain at least one capital letter")
            return wrapper()

        special = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if not special.search(password):
            print("Invalid password:Must contain at least one special char.")
            return wrapper()


        return func(password)
    return wrapper


@validator
def test_password(password):
    print("Password is valid.")
    return password
if __name__ == "__main__":
    print(test_password())
