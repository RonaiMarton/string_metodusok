"""
Feladat: Kérj be egy felhasználónevet a regisztrációhoz, majd jelenítsd meg háromféleképpen:
nagybetűs (pl. címkén vagy azonosítóban),


kisbetűs (pl. email összehasonlításhoz),


csak az első betű nagy (személyes üdvözlésnél).

"""
txt = input("enter your username to get it in all lowercase, first charachter uppercase and all uppercase\n")
print(txt.casefold())
print(txt.capitalize())
print(txt.upper())