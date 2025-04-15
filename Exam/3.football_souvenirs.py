team = input()
souvenir = input()
quantity = int(input())

price = 0

if team == "Argentina":
    if souvenir == "flags":
        price = 3.25
    elif souvenir == "caps":
        price = 7.20
    elif souvenir == "posters":
        price = 5.10
    elif souvenir == "stickers":
        price = 1.25
    else:
        print("Invalid stock!")
        exit()
elif team == "Brazil":
    if souvenir == "flags":
        price = 4.20
    elif souvenir == "caps":
        price = 8.50
    elif souvenir == "posters":
        price = 5.35
    elif souvenir == "stickers":
        price = 1.20
    else:
        print("Invalid stock!")
        exit()
elif team == "Croatia":
    if souvenir == "flags":
        price = 2.75
    elif souvenir == "caps":
        price = 6.90
    elif souvenir == "posters":
        price = 4.95
    elif souvenir == "stickers":
        price = 1.10
    else:
        print("Invalid stock!")
        exit()
elif team == "Denmark":
    if souvenir == "flags":
        price = 3.10
    elif souvenir == "caps":
        price = 6.50
    elif souvenir == "posters":
        price = 4.80
    elif souvenir == "stickers":
        price = 0.90
    else:
        print("Invalid stock!")
        exit()
else:
    print("Invalid country!")
    exit()

total_price = quantity * price
print(f"Pepi bought {quantity} {souvenir} of {team} for {total_price:.2f} lv.")
