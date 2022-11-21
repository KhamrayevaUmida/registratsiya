try:
    name = input("Ismingizni kiriting: ")
    surname = input("Familiyangizni kiriting: ")
    age = int(input("Tugilgan yilingizni kiriting: "))
    while True:

        parol1 = input("Parolingizni kiriting: ")
        parol2 = input("Parolni qayta kiriting: ")

        if parol1 == parol2:
            print(surname, name, (2022-age), "yoshdasiz. Siz muvoffaqiyatli registratsiyad utdingiz")
            break

        elif parol1 != parol2:
            print("siz bir xil parol kiritmadingiz. Qayta urining")

        else:
            print("Xatolik bor")

except ValueError:
    print("Siz string kirityapsiz")