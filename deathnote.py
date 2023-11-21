print("Kişi kim?")
isim = input()
print("Kişinin Yaşı?")
age = input()
print("Nasıl ölecek?")
death = input()
years = 90 - int(age)
weeks = years * 52
print(f"{isim} kişisinin ölmesine yaklaşık {weeks} hafta kaldı. Ayrıca {death} şeklinde ölecek.")

