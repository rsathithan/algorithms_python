def mean(nums: list) -> float:
    """
    Find mean of a list of numbers.

    >>> mean([3, 6, 9, 12, 15, 18, 21])
    12.0
    >>> mean([5, 10, 15, 20, 25, 30, 35])
    20.0
    >>> mean([1, 2, 3, 4, 5, 6, 7, 8])
    4.5
    """
    return sum(nums) / len(nums)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
