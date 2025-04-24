def grocery_store(**kwargs):
    sorted_items = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    return "\n".join(f"{name}: {quantity}" for name, quantity in sorted_items)
