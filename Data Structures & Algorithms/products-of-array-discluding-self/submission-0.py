class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=[]
        l=len(nums)
        for i in range(l):
            prod=1
            for j in range(l):
                if i!=j:
                    prod*=nums[j]
            product.append(prod)
        return product