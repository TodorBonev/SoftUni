population = list(map(int, input().split(", ")))
minimum_wealth = int(input())

total_wealth = sum(population)

if total_wealth < minimum_wealth * len(population):
    print("No equal distribution possible")
else:
    for i in range(len(population)):
        if population[i] < minimum_wealth:
            max_index = population.index(max(population))
            transfer_amount = minimum_wealth - population[i]
            population[max_index] -= transfer_amount
            population[i] += transfer_amount

    print(population)
