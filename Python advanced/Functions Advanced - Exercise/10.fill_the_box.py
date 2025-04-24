def fill_the_box(height, length, width, *cubes):
    capacity = height * length * width
    leftover_cubes = 0

    for cube in cubes:
        if cube == "Finish":
            break
        if capacity >= cube:
            capacity -= cube
        else:
            leftover_cubes += cube - capacity
            capacity = 0

    return (f"No more free space! You have {leftover_cubes} more cubes."
            if capacity == 0 else
            f"There is free space in the box. You could put {capacity} more cubes.")

