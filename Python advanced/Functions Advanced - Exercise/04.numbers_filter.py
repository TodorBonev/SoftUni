def even_odd_filter(**kwargs):
    filtered = {key: [num for num in value if (num % 2 == 0) == (key == "even")] for key, value in kwargs.items()}
    return dict(sorted(filtered.items(), key=lambda x: len(x[1]), reverse=True))
