class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            ss=set()
            for c in s:
                ss.add(c)
            ts=set()
            for c in t:
                ts.add(c)
            if ss==ts:
                count=0
                for c in ss:
                    if s.count(c)==t.count(c):
                        count+=1
                    else: 
                        return False
                if count==len(ss):
                    return True
            else:
                return False
        else:
            return False            
    

                

            
        
        
        
