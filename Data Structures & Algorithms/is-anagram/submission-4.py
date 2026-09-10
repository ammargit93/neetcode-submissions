class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):return False
        arrs, arrt = [0]*26, [0]*26 
        for i in range(len(s)):
            arrs[ord(s[i])-ord('a')]+=1
            arrt[ord(t[i])-ord('a')]+=1
        return arrs==arrt