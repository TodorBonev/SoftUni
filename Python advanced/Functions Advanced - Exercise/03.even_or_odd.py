def even_odd(*args):
    return [n for n in args[:-1] if (n % 2 == 0) == (args[-1] == "even")]
