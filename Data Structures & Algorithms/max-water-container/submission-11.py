class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        count=2
        mcw=0
        l=0
        r=len(heights)-1
        for i in range(n-1):
            nw=min(heights[l],heights[r])*abs(r-l)
            if nw>mcw:
                mcw=nw
            if (r-l)==1:
                return mcw
            if heights[l]==heights[r]:
                r-=1
                l+=1
            elif heights[l]>heights[r]:
                r-=1
            elif heights[l]<heights[r]:
                l+=1
            # if min(heights[r-1],heights[l])==min(heights[l+1],heights[r]):
            #     l+=1
            #     r-=1
            # elif min(heights[r-1],heights[l])>min(heights[l+1],heights[r]):
            #     r-=1
            # elif min(heights[r-1],heights[l])<min(heights[l+1],heights[r]):
            #     l+=1
                
            
        return mcw
