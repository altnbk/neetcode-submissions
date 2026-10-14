class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        lst=[1]*n

        a=1
        for i in range(n):
            lst[i]=a
            a*=nums[i]
        
        a=1
        for i in range(n-1, -1, -1):
            lst[i]*=a
            a*=nums[i]

        return lst