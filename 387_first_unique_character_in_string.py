class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        s_count = collections.Counter(s)        
        s_count = {k:v for k,v in s_count.items() if s_count[k]==1}
        
        for i in range(len(s)):
            if s[i] in s_count.keys():
                return i
            
        return -1

    def firstUniqChar_alternate(self, s: str) -> int: # Concise Form
    
    
    s_count = collections.Counter(s)
    
    for idx, ch in enumerate(s):
        if s_count[ch] == 1:
            return idx
    return -1