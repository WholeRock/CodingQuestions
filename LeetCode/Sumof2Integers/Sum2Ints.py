
'''
source: https://leetcode.com/problems/sum-of-two-integers/

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.


'''

def getSum( a, b):
    if a<0 and b<0:


    n = len(bin(a))-2
    if(len(bin(b))>len(bin(a))):
        n = len(bin(b))-2
    carry=0
    l = []
    print bin(a)
    while n>0:
        s=0
        a1 = a & 1
        b1 = b & 1
        if a1 == b1:
            s = 0
            if carry ==1:
                s=1
            if a1 == 1:
                carry = 1
            else:
                carry = 0
        else:
            if carry ==1:
                s=0
                carry=1
            else:
                s=1
                carry=0

        l.append(s)
        a >>= 1
        b >>= 1
        n-=1
    if carry ==1:
        l.append(carry)

    l.reverse()
    sum = map(str, l)
    sum = ''.join(sum)
    sum = int(sum,base=2)
    return sum

print getSum(-1, 1)