while True:
    try:
        n = int(input("Son kiriting: "))
        if n <= 0:
            print("Iltimos faqat musbat va butun son kiriting: ")
        else:
            print(f"{n} gacha bo'lgan sonlar kvadrati")
            for i in range(1, n):
                print(i**2)
            break
    except ValueError:
        print("Iltimos faqat musbat va butun son kiriting")