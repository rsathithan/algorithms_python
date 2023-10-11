# Ugly Number 2 Problem
# LeetCode Problem: https://leetcode.com/problems/ugly-number-ii/
"""
Prints the nth ugly number n being the user input.

Ugly numbers are a sequence of positive integers that are defined as numbers
whose only prime factors are 2, 3, and 5.
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers.
By convention, 1 is included

Parameters:
n (int): The index of the desired ugly number.

Returns:
int: The nth ugly number.

Algorithm:
The nth ugly number is generated by multiplying previous ugly numbers with 2, 3, or 5.
The ugly numbers are stored in an array k, and the algorithm uses
three pointers ptr1, ptr2, and ptr3
to keep track of the positions in the array for
multiplying with 2, 3, and 5 respectively.

Time Complexity:
O(n) - The algorithm generates the nth ugly number in linear time.

Space Complexity:
O(n) - The algorithm uses an array of size n to store the ugly numbers.


Sources:
- Dynamic Programming and Ugly Numbers: https://www.geeksforgeeks.org/ugly-numbers/
"""

import doctest


def nth_ugly_number(index: int) -> int:
    """
    Return the nth ugly number.
    >>> nth_ugly_number(5)
    5
    >>> nth_ugly_number(7)
    8
    >>> nth_ugly_number(1)
    1
    >>> nth_ugly_number(-1)
    Traceback (most recent call last):
    ValueError: Index for nth ugly number should be ≥ 0

    """
    if index < 0:
        raise ValueError("Index for nth ugly number should be ≥ 0")
    dp = [1] * (index + 1)
    ptr1 = 0
    ptr2 = 0
    ptr3 = 0
    for i in range(1, index):
        two = dp[ptr1] * 2
        three = dp[ptr2] * 3
        five = dp[ptr3] * 5
        dp[i] = min(two, three, five)
        if dp[i] == two:
            ptr1 += 1
        if dp[i] == three:
            ptr2 += 1
        if dp[i] == five:
            ptr3 += 1

    return dp[index - 1]


if __name__ == "__main__":
    # User input to find the nth Ugly Number
    print("\n********* Ugly Numbers Using Dynamic Programming ************\n")
    print("\n*** Enter -1 to quit ***")
    print("\nEnter the index (≥ 0) of the Ugly number to find: ", end="")
    try:
        while True:
            index = int(input().strip())
            if index < 0:
                print("\n********* END ************")
                break
            else:
                ugly_number = nth_ugly_number(index)
                print(f"The {index}th Ugly Number is: {ugly_number}")
                print("Try another index to find a Ugly Number: ", end="")
    except (NameError, ValueError):
        print("\n********* Invalid input, END ************\n")


# Test cases for nthUglyNumber function
doctest.testmod()
