class Solution:

    def encode(self, strs: List[str]) -> str:
        st=''
        for i in strs:
            st=f"{st}{len(i)}${i}"
        return st

    def decode(self, s: str) -> List[str]:
        strs=[]
        i=0
        while i<len(s):
            symb=s.find("$",i)
            endp=symb+1+int(s[i:symb])
            strs.append(s[symb+1:endp])
            i=endp
        return strs
