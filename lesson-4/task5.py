def fun():
    x = input("Password: ")
    if len(x) < 8:
        print("Password is too short.")
    else:
        for i in x:
            if i.isupper():
                print("Password is strong.")
                return
        print("Password must contain an uppercase letter.")
fun()
