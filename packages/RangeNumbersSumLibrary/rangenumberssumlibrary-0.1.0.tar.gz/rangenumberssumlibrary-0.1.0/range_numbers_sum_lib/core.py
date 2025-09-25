def range_sum(a: int, b: int) -> int:
    """Return the sum of numbers from a to b inclusive"""
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))
