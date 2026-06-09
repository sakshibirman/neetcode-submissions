from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)
        for i in nums:
            freq[i]+=1
        top_k=sorted(freq, key=freq.get, reverse=True)[:k]
        return top_k



