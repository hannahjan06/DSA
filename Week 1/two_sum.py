"""
runtime: 3ms
time complexity: O(n)
space complexity: O(n)
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}

        for i, n in enumerate(nums): # O(n)
            subtracted = target - n 
            if subtracted in hashmap: # O(1) average    
                """
                using hashmap.keys() would be slower
                """
                return (hashmap[subtracted], i)
            hashmap[n] = i # O(1) average
        
        return None
    
"""
A hashmap (also called a hash table) is a data structure that stores data as key–value pairs.

It uses a hash function to convert a key into an index, where the corresponding value is stored.
This allows for very fast operations—on average, inserting, deleting, and searching all take O(1) time.

If two keys produce the same index (a collision), the hashmap handles it using techniques like
chaining (linked lists) or open addressing.

In Python, dictionaries (dict) are implemented using hashmaps.
"""
