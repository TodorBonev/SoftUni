chicken_menus = int(input())
fish_menus = int(input())
vegan_menus = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.40
vegan_menu_price = 8.15
delivery = 2.50

menus_price = (chicken_menus * chicken_menu_price) + (fish_menus * fish_menu_price) + (vegan_menus * vegan_menu_price)

dessert_price = menus_price * 0.20

total_price = menus_price + dessert_price + delivery

print(total_price)