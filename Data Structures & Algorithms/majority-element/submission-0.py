class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        t = len(nums)//2
        h = {}
        for n in nums:
            h[n] = h.get(n, 0)+1
            if h[n]>t:
                return n