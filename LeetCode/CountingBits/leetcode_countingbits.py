#source: https://leetcode.com/problems/counting-bits/

'''
Given a non negative integer number num. For every numbers i in the range 0 ? i ? num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
'''

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num ==0:
            return [0]
        elif num == 1:
            return [0, 1]
        leading =[]
        range =3
        indexcount=0
        i=2
        total= []
        total.append(0)
        leading.append(0)
        total.append(1)
        leading.append(1)
        while(i<=num):
            total.append(total[i-1]-leading[i-1] +1)
            if(i==range):
                leading.append(leading[indexcount]+1)
                range = range*2 +1
                indexcount = -1
            else:
                leading.append(leading[indexcount])
            i+=1
            indexcount +=1
        return total