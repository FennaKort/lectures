# exercise: logical propositions with not
# Write a password checker program that asks the user for a username and a password, and prints:
# 	True if the username is not contained in the password
# 	False if the username is contained in the password
# plan:
# 1. ask for username input
# 2. ask for password input
# 3. check if the username is not contained in the password returnTrue - make this a function
def username_not_in_password(username: str, password: str) -> bool:
    if username not in password:
        return True
    else:
        return False

def main():
    username = input("Write your username here: ")
    password = input("Write your password here (must not contain username): ")
    print("This password can be approved: ", username_not_in_password(username, password))

main()
