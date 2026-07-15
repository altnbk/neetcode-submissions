class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            nd=target-num
            if nd in d:
                return [d[nd], i]
            d[num] = i

        