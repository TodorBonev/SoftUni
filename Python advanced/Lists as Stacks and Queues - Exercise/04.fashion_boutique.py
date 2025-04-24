def calculate_racks():

    clothes = list(map(int, input().split()))
    rack_capacity = int(input())
    
    racks_used = 1 
    current_rack_sum = 0
    
    while clothes:

        current_cloth = clothes.pop()
        
        if current_rack_sum + current_cloth <= rack_capacity:

            current_rack_sum += current_cloth
        else:

            racks_used += 1
            current_rack_sum = current_cloth
    
    return racks_used

print(calculate_racks())