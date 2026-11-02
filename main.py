print("Pisa Universiteti kalkulyatori")
ism = input("Ismingiz: ")
matematika = int(input("Matematika baho: "))
informatika = int(input("Informatika baho: "))
ingliz_tili = int(input("Ingliz tili baho: "))

ortacha = (matematika + informatika + ingliz_tili) / 3
print(f"{ism}, sening ortacha bahoying: {round(ortacha, 2)}")

if ortacha >= 4.5:
    print("Tabriklayman! Sen Pisa uchun idealsan!")
else:
    print("Hali ham harakat qil, Pisa seni kutmoqda!")
