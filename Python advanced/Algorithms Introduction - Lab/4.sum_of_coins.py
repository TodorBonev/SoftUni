def get_minimum_coins(coin_values, target_sum):
    coin_values.sort(reverse=True)
    coins_used = {}
    total_coins = 0
    
    for coin in coin_values:
        if target_sum == 0:
            break
        
        count = target_sum // coin 
        if count > 0:
            coins_used[coin] = count
            total_coins += count
            target_sum -= count * coin 
        
    if target_sum > 0:
        return "Error"
    
    result = [f"Number of coins to take: {total_coins}"]
    for coin, count in coins_used.items():
        result.append(f"{count} coin(s) with value {coin}")
    
    return "\n".join(result)

coin_values = list(map(int, input().split(", ")))
target_sum = int(input())

print(get_minimum_coins(coin_values, target_sum))
