string_of_cards = input()
shuffle_count = int(input())

cards_list = string_of_cards.split()
middle_of_the_cards = int(len(cards_list) / 2)
end_of_card_list = len(cards_list)

first_half = cards_list[0:middle_of_the_cards]
second_half = cards_list[middle_of_the_cards:]
result = []

for current_shuffle in range(1, shuffle_count + 1):
    for index in range(len(first_half)):
        result.append(first_half[index])
        result.append(second_half[index])

    first_half = result[0:middle_of_the_cards]
    second_half = result[middle_of_the_cards:]
    if current_shuffle != shuffle_count:
        result = []
print(result)