class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            d = {}
            d[num1] = i
            for x, num2 in enumerate(nums):
                nd=target-num2
                if nd in d and i!=x:
                    return [d[nd], x]

        