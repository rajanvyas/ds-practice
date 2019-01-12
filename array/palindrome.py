import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        first = 0
        second = len(s)-1
        while first < second:

            while first < second and not s[first].isalnum():
                first += 1
            while first < second and not s[second].isalnum():
                second -= 1
            if s[first].lower() != s[second].lower():
                return False
            first +=1
            second -= 1
        return True

    def main(self):
        s = "A man, a plan, a canal: Panama"
        print self.isPalindrome(s)

if __name__ == '__main__':
    sol = Solution()
    sol.main()