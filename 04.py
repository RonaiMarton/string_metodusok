"""
Feladat: A rendelésben az „alma” helyett cseréld „körtére”, ha a boltban nincs alma.
"""
order = input("enter ur order \n")
x = input(" there apples in the store y/n")
apple = order.count("apple")
if x == "y":
    print(order)
else :
    print(order.replace("apple", "pear"))
