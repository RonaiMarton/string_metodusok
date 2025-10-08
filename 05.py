"""
Feladat: Kérj be egy email címet a regisztrációhoz, majd ellenőrizd, hogy Gmail-es-e.

"""
txt = input("enter ur email to know it it is a gmail \n")
if txt.endswith("gmail.com"):
    print("it is a gmail")
else :
    print("it is not a gmail")
