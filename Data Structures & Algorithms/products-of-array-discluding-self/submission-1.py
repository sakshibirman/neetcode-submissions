class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        prod=1
        zero_count=0
        product=[1]*l
        for i in range(l):
            if nums[i]==0:
                zero_count+=1
                if zero_count==1:
                    index=i
                if zero_count>1:
                    product=[0]*l
                    return product
                continue
            else:
                prod*=nums[i]
                        
        product=[0]*l
        for j in range(l):
            if zero_count==0:
                product[j]=int(prod/nums[j])
            else:
                product[index]=prod
        return product