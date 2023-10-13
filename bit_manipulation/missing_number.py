def find_missing_number(nums: list[int]) -> int:
    """
    Finds the missing number in a list of consecutive integers.

    Args:
        nums: A list of integers.

    Returns:
        The missing number.

    Example:
        >>> find_missing_number([0, 1, 3, 4])
        2
        >>> find_missing_number([1, 3, 4, 5, 6])
        2
    """
    low = nums[0]
    high = nums[-1]
    missing_number = high

    for i in range(low, high):
        missing_number ^= i ^ nums[i - low]

    return missing_number
