#!/usr/bin/python3
"""
In a text file, there is a single character H.
text editor can execute only two operations in this file: Copy All and Paste.
Given a number n, a method that calculates
the fewest number of operations needed
to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0

Example:
n = 9
H => Copy All => Paste => HH => Paste =>HHH =>
Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
Number of operations: 6
"""


def minOperations(n):
    """
    Method that calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    num_of_operations = 0
    h_count = 1
    last_paste = 0

    if n <= 1:
        return 0

    while h_count < n:
        if n % h_count == 0:
            num_of_operations += 2
            last_paste = h_count
            h_count *= 2
        else:
            num_of_operations += 1
            h_count += last_paste

    return num_of_operations
