def math_operations(*numbers, **operations):
    keys = ["a", "s", "d", "m"]
    for i, num in enumerate(numbers):
        key = keys[i % 4]  
        if key == "a":
            operations[key] += num
        elif key == "s":
            operations[key] -= num
        elif key == "d":
            if num != 0:  
                operations[key] /= num
        elif key == "m":
            operations[key] *= num

    sorted_result = sorted(operations.items(), key=lambda x: (-x[1], x[0])) 
    return "\n".join(f"{key}: {value:.1f}" for key, value in sorted_result)
