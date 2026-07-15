class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count=1
        for i in range(len(nums)):
            nlist=nums[i+1:]
            for x in range(len(nlist)):
                if (nums[i]+nlist[x])==target:
                    return [i,x+count]
                    break
            count+=1

        