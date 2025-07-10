def fun():
    password = input("Password: ")
    if len(password) < 8:
        print("Password is too short.")
    else:
        for i in password:
            if i.isupper():
                print("Password is strong.")
                return
        print("Password must contain an uppercase letter.")
fun()
