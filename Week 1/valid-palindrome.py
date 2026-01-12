"""
runtime: 15ms
time complexity: O(n)
space complexity: O(n)
link: https://leetcode.com/problems/valid-palindrome/
tags: #string #two-pointers
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())
        return s == s[::-1]