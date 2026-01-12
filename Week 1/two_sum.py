class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}

        for i, n in enumerate(nums):
            subtracted = target - n
            if subtracted in hashmap:
                return (hashmap[subtracted], i)
            hashmap[n] = i
        
        return None
    
