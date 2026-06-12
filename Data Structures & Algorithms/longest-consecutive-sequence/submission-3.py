class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort=sorted(nums)
        l=len(sort)
        current=1
        best=1
        if l==0:
            return 0
        for i in range(l-1):
            if sort[i+1]==sort[i]:
                continue
            if sort[i+1]==sort[i]+1:
                current+=1
            else:
                best=max(current,best)
                current=1
            
        return max(best,current)