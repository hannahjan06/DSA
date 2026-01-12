"""
runtime: 8ms
time complexity: O(n)
space complexity: O(n)
link: https://leetcode.com/problems/valid-parentheses/
tags: #string #stack
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
        
        return not stack