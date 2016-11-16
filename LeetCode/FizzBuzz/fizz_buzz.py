__author__ = 'pup'
"""
https://leetcode.com/problems/fizz-buzz/

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five output “FizzBuzz”.
"""

def fizzBuzz(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    _list = []
    for i in range(1, n+1, 1):
        s = ""
        if i%3 == 0:
            s = "Fizz"
        if i%5 == 0:
            s += "Buzz"
        if s == "":
            s = str(i)
        _list.append(s)

    return _list

#Time complexity O(n)
