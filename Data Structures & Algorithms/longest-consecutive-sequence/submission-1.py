class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort=sorted(nums)
        l=len(sort)
        count=[1]*l
        if l!=0:
            num=sort[0]
        else:
            return 0
        index=0
        for i in range(l-1):
            if sort[i+1]==num+1:
                count[index]+=1
                num=sort[i+1]
            if sort[i+1]==num:
                num=sort[i+1]
            else:
                num=sort[i+1]
                index+=1
            
        return max(count)
