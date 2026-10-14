class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rzl=1
        lst=[]
        am=nums.count(0)
        if am>1:
            for i in nums:
                lst.append(0)
            return lst

        else:
            if 0 in nums:
                plc=nums.index(0)
                for i in nums:
                    lst.append(0)
                del nums[plc]
                
                for i in nums:
                    rzl*=i
                    lst[plc]=rzl
                return lst
            else:
                for i in nums:
                    rzl*=i
            
                for i in nums:
                    lst.append(int(rzl/i))
                return lst
