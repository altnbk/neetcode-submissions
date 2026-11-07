class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            # (A) nums[i] が前と同じ値ならスキップ
            if i>0 and nums[i]==nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    # (B) 合計を小さくしたい → どっちを動かす？
                    right-=1
                elif total < 0:
                    # (C) 合計を大きくしたい → どっちを動かす？
                    left+=1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    # (D) 次の組を探すために left を進める
                    left+=1
                    #     + nums[left] が前と同じ値の間はさらに進める
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
        return res





        