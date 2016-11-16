__author__ = 'pup'

"""
https://leetcode.com/problems/power-of-two/

Given an integer, write a function to determine if it is a power of two.
"""

def isPowerOfTwo(self, n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0:
        return False
    while n >1:
        if n%2 ==0:
            n = int(n/2)
        else:
            return False
    return True

# Time complexity: O(lgn)
# Space complexity: O(1)

# another solution

def isPowerOfTwo_2(self, n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0:
        return False
    if bin(n).count('1') == 1:
        return True
    return False

