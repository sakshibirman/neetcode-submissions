class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort=sorted(nums)
        l=len(sort)
        current=1
        best=1
        if l!=0:
            num=sort[0]
        else:
            return 0
        index=0
        for i in range(l-1):
            if sort[i+1]==num+1:
                current+=1
                num=sort[i+1]
            if sort[i+1]==num:
                num=sort[i+1]
            else:
                num=sort[i+1]
                if current>best:
                    best=current
                    current=1
                else:
                     current=1
            
        return max(current,best)