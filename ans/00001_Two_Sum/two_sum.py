class Solution:

    def __init__(self):
        pass

    def solve(self, nums: list[int], target: int) -> list[int]:
        seen = set()
        for idx, elm in enumerate(nums):
            remaining = target - elm
            if remaining in seen:
                return [idx, nums.index(remaining)]
            seen.add(elm)
