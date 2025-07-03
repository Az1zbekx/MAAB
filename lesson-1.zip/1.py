try:
    name = input("Salom MAAB ga xush kelibsiz!\nIsmingiz nima: ")
    age_input = input("Yoshingiz nechida: ")

    if not age_input.isdigit():
        print("Iltimos, yoshingizni faqat sonlarda kiriting.")
    else:
        age = int(age_input)
        if age >= 18:
            print(f"{name}, sizning yoshingiz {age} bo'lgani uchun bizda ta'lim olishingiz mumkin.")
        else:
            print(f"{name}, sizning yoshingiz 18 dan kichik bo'lgani sababli bizda ta'lim olishingiz mumkin emas.")
except Exception as e:
    print("Noma'lum xatolik yuz berdi:", e)
