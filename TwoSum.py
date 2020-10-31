class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, val in enumerate(nums):
            if val in d:\
                return [i, d.get(val)]
            else:
                d[target-val] = i