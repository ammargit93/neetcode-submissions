class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h = {}
        res= []
        
        for n in nums:
            h[n] = h.get(n,0) + 1
        n = len(nums)
        for k, v in h.items():
            if v > n//3:
                res.append(k)
        return res