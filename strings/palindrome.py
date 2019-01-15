# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.

class Solution(object):
    def isPalindrome(self, string):
        """
        :type string: str
        :rtype: bool
        """
        first = 0
        second = len(string) - 1
        while first < second:

            while first < second and not string[first].isalnum():
                first += 1
            while first < second and not string[second].isalnum():
                second -= 1
            if string[first].lower() != string[second].lower():
                return False
            first +=1
            second -= 1
        return True

    def makePelindrome(self,s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True




    def main(self):
        s = "acbca"

        print self.makePelindrome(s)

if __name__ == '__main__':
    sol = Solution()
    sol.main()