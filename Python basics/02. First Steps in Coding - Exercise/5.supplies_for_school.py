pens = int(input())
marker_packs = int(input())
detergent_liters = int(input())
discount = int(input()) /100

pen_price = 5.80
marker_price = 7.20
detergent_price = 1.20

price_before_discount = (pen_price * pens) + (marker_packs * marker_price) + (detergent_price * detergent_liters)
total_price = price_before_discount - price_before_discount * discount

print(total_price)