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
        for i in range(k):
            max_key=max(d, key=d.get)
            lst.append(int(max_key))
            del d[max_key]
        return lst
