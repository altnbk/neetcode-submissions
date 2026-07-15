class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers=nums
        s=set()
        count=0
        for num in numbers:
            if num in s:
                return True
            else:
                s.add(num)
        return False
