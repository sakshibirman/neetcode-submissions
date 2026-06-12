class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort=sorted(nums)
        current=1
        best=1
        if len(sort)==0:
            return 0
        for i in range(len(sort)-1):
            if sort[i+1]==sort[i]:
                continue
            if sort[i+1]==sort[i]+1:
                current+=1
            else:
                best=max(current,best)
                current=1
            
        return max(best,current)