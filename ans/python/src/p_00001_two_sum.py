"""
"Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order." - [1. Two Sum](https://leetcode.com/problems/two-sum/)
"""


class Solution:

    def __init__(self):
        pass

    def solve_001(self, nums: list[int], target: int) -> list[int]:
        """
        Complexity:
            - time complexity: O(n^2)
            - space complexity: O(1)
        """
        if not self.__validate_args(nums, target):
            raise TypeError

        for idx1, elm1 in enumerate(nums):
            for idx2, elm2 in enumerate(nums):
                if idx1 == idx2:
                    continue
                else:
                    if elm1 + elm2 == target:
                        return [idx1, idx2]

    def solve_002(self, nums: list[int], target: int) -> list[int]:
        """
        Complexity:
            - time complexity: O(n)
            - space complexity: O(n)
        """
        if not self.__validate_args(nums, target):
            raise TypeError

        seen = set()
        for idx, elm in enumerate(nums):
            remaining = target - elm
            if remaining in seen:
                return [idx, nums.index(remaining)]
            seen.add(elm)

    def solve_003(self, nums: list[int], target: int) -> list[int]:
        """
        Complexity:
            - time complexity: O(n)
            - space complexity: O(n)
        """
        if not self.__validate_args(nums, target):
            raise TypeError

        hashmap = {}
        for key, val in enumerate(nums):
            remaining = target - val
            if remaining in hashmap.keys():
                return [key, hashmap[remaining]]
            else:
                hashmap[val] = key

    def __validate_args(self, nums: list[int], target: int) -> bool:

        if not isinstance(nums, list) or not all(isinstance(num, int) for num in nums):
            return False
        elif not isinstance(target, int):
            return False
        elif len(nums) < 2 or len(nums) > 10**4:
            return False
        else:
            for num in nums:
                if num <= -10**9 or num >= 10**9:
                    return False
            if target <= -10**9 or target >= 10**9:
                return False
            else:
                return True
