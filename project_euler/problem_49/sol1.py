"""
Prime permutations

Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of
the terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

"""
Solution:

First, we need to generate all 4 digits prime numbers. Then greedy
all of them and use permutation to form new numbers. Use binary search
to check if the permutated numbers is in our prime list and include
them in a candidate list.

After that, bruteforce all passed candidates sequences using
3 nested loops since we know the answer will be 12 digits.
"""

from itertools import permutations
from math import floor, sqrt


def is_prime(number: int) -> bool:
    """
    function to check whether the number is prime or not.
    >>> is_prime(2)
    True
    >>> is_prime(6)
    False
    >>> is_prime(1)
    False
    """

    if number < 2:
        return False

    for i in range(2, floor(sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def search(target: int, prime_list: list) -> bool:
    """
    function to search a number in a list using Binary Search.
    >>> search(3, [1, 2, 3])
    True
    >>> search(4, [1, 2, 3])
    False
    """

    l, r = 0, len(prime_list) - 1
    while l <= r:
        m = (l + r) // 2
        if prime_list[m] == target:
            return True
        elif prime_list[m] < target:
            l = m + 1
        else:
            r = m - 1

    return False


def solution():
    """
    Return the solution of the problem.
    >>> solution()
    296962999629
    """
    prime_list = [n for n in range(1001, 10000, 2) if is_prime(n)]
    candidates = []

    for x in prime_list:
        perm = list(permutations(list(str(x))))
        tmp_numbers = []

        for i in range(len(perm)):
            p = int("".join(list(perm[i])))

            if p % 2 == 0:
                continue

            if search(p, prime_list):
                tmp_numbers.append(p)

        tmp_numbers.sort()
        if len(tmp_numbers) >= 3:
            candidates.append(tmp_numbers)

    passed = []
    for candidate in candidates:
        length = len(candidate)
        found = False

        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    if (
                        abs(candidate[i] - candidate[j])
                        == abs(candidate[j] - candidate[k])
                        and len(set([candidate[i], candidate[j], candidate[k]])) == 3
                    ):
                        passed.append(
                            sorted([candidate[i], candidate[j], candidate[k]])
                        )
                        found = True

                    if found:
                        break
                if found:
                    break
            if found:
                break

    answer = set()
    for seq in passed:
        answer.add("".join(list(map(str, seq))))

    return [x for x in answer][1]


if __name__ == "__main__":
    print(solution())
