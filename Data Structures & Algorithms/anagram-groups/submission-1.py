class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        biglist=[]
        while len(strs)!=0:
            smalist=[]
            s=strs[0]
            smalist.append(s)
            strs.pop(0)
            delist=[]
            for i, t in enumerate(strs):
                d1 = {}
                d2 = {}
                
                for c in s:
                    d1[c] = d1.get(c, 0) + 1
                for c in t:
                    d2[c] = d2.get(c, 0) + 1
                if d1==d2:
                    smalist.append(t)
                    delist.append(t)
            for st in delist:
                    strs.remove(st)    
            biglist.append(smalist)
        return biglist
            

