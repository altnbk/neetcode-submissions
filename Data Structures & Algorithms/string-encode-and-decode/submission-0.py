class Solution:

    def encode(self, strs: List[str]) -> str:
        st=''
        for i in strs:
            st=f"{st}{len(i)}${i}"
        return st

    def decode(self, s: str) -> List[str]:
        strs=[]
        while len(s)>0:
            stap=(s.find("$")+1)
            endp=stap+int(s[0:(s.find("$"))])
            a=s[stap:endp]
            strs.append(a)
            s=s[endp:]
        return strs
