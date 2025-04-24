def find_starting_pump(petrol_pumps):
    n = len(petrol_pumps)
    
    start = 0
    current_petrol = 0
    total_deficit = 0
    
    for i in range(n):

        petrol, distance = petrol_pumps[i]
        current_petrol += petrol - distance
        

        if current_petrol < 0:

            total_deficit += current_petrol
            start = i + 1
            current_petrol = 0
    
    if current_petrol + total_deficit >= 0:
        return start
    else:
        return -1 

n = int(input())
petrol_pumps = []
for _ in range(n):
    petrol, distance = map(int, input().split())
    petrol_pumps.append((petrol, distance))

print(find_starting_pump(petrol_pumps))