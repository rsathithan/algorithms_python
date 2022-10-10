# https://byjus.com/equivalent-resistance-formula/

from __future__ import annotations


def resistor_parallel(
    resistors: list[float],
) -> float:  # Req = 1/ (1/R1 + 1/R2 + ... + 1/Rn)
    """
    >>> resistor_parallel([3.21389, 2, 3])
    0.8737571620498019
    >>> resistor_parallel([3.21389, 2, -3])
    Traceback (most recent call last):
        ...
    ValueError: Resistor at index 2 has a negative or zero value!
    >>> resistor_parallel([3.21389, 2, 0.000])
    Traceback (most recent call last):
        ...
    ValueError: Resistor at index 2 has a negative or zero value!
    """

    firstSum = 0.00
    index = 0
    for resistor in resistors:
        if resistor <= 0:
            raise ValueError(f"Resistor at index {index} has a negative or zero value!")
        firstSum += 1 / float(resistor)
        index += 1
    return 1 / firstSum


def resistor_series(resistors: list[float]) -> float:  # Req = R1 + R2 + ... + Rn
    """
    This function can calculate the equivalent resistance for any number of
    resistors in parallel.
    >>> resistor_series([3.21389, 2, 3])
    8.21389
    >>> resistor_series([3.21389, 2, -3])
    Traceback (most recent call last):
        ...
    ValueError: Resistor at index 2 has a negative value!
    """
    sum = 0.00
    index = 0
    for resistor in resistors:
        sum += resistor
        if resistor < 0:
            raise ValueError(f"Resistor at index {index} has a negative value!")
        index += 1
    return sum


if __name__ == "__main__":
    import doctest

    doctest.testmod()
