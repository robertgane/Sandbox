minimum_length = 8
user_password = input("Password: ")
while len(user_password) < minimum_length:
    print("Password is not long enough")
    user_password = input("Password: ")
print("*" * len(user_password))