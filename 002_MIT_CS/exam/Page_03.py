def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    return (1 + 8 * k) ** 0.5 % 2 == 1