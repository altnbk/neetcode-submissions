class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        d = defaultdict()
        for x in nums:
            key = str(x)  # または文字カウントのタプルでもOK
            if key not in d:
                d[key] = 0
            d[key]+=1

        lst=[]
        while k!=0:
            max_key=max(d, key=d.get)
            lst.append(int(max_key))
            del d[max_key]
            k-=1
        return lst
