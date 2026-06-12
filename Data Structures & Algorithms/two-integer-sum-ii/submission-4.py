from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hah=defaultdict(int)
        for i,num in enumerate(numbers,start=1):
            a=target-num
            if a in hah:
                return [hah[a],i]
            hah[num]=i

