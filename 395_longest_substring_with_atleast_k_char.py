from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        charCount = Counter(s)        
        charToRemove = [key for key, val in charCount.items() if val<k]
        # print(charToRemove)
        
        for ch in charToRemove:
            return max(self.longestSubstring(t,k) for t in s.split(ch))
        return len(s)