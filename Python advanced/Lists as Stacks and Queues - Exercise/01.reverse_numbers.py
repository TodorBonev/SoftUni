def reverse_integers_with_stack(integers):

    stack = []
    
    for num in integers:
        stack.append(num)

    reversed_integers = []
    while stack:
        reversed_integers.append(stack.pop())
    
    return reversed_integers


input_string = input()

integers = input_string.split()

reversed_integers = reverse_integers_with_stack(integers)

print(' '.join(reversed_integers))
