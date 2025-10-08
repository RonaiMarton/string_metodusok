"""
Feladat: Kérj be egy felhasználónevet a regisztrációhoz, majd jelenítsd meg háromféleképpen:
nagybetűs (pl. címkén vagy azonosítóban),


kisbetűs (pl. email összehasonlításhoz),


csak az első betű nagy (személyes üdvözlésnél).

"""
txt = input("enter your username to get it in all lowercase, first charachter uppercase and all uppercase\n")
print(f"lowercase: {txt.casefold()}")
print(f"First letter uppercase: {txt.capitalize()}")
print(f"uppercase: {txt.upper()}")

