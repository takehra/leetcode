class TwoSum:

    def __init__(self):
        pass

    def solve_001(self, nums: list[int], target: int) -> list[int]:
        """
        Complexity:
            - time complexity: O(n^2)
            - space complexity: O(1)
        """
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
        hashmap = {}
        for key, val in enumerate(nums):
            remaining = target - val
            if remaining in hashmap.keys():
                return [key, hashmap[remaining]]
            else:
                hashmap[val] = key
