num_to_check = int(input())

def is_it_prime_number(num):
    is_it_prime = False
    if num <= 1:
        is_it_prime = False
    elif num == 2:
        is_it_prime = True
    else:
        for current_num in range(2, num):
            if num % current_num == 0:
                is_it_prime = False
                break
            else:
                is_it_prime = True

    print(is_it_prime)


is_it_prime_number(num_to_check)