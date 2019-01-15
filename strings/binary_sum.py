# -*- coding: utf-8 -*-
##
# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_size = len(a)
        b_size = len(b)
        max_size = max(a_size,b_size)
        result = ''
        carry = 0

        a = a.zfill(max_size)
        b = b.zfill(max_size)

        for i in range(max_size-1,-1,-1):
            r = carry
            if a[i] == '1':
                r+=1
            if b[i] == '1' :
                r+=1
            result = ('1' if r%2==1 else '0')+result
            carry = 0 if r<2 else 1

        if carry != 0:
            result = '1'+result
        return result






    def main(self):
        a = "11"
        b = "1"
        print self.addBinary(a,b)


if __name__ == '__main__':
    sol = Solution()
    sol.main()