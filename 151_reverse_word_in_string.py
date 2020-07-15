class Solution:
    def reverseWords(self, s: str) -> str:
        
        s_list = s.split(" ")        
        s_l = [x for x in s_list if x]        
        s_l.reverse()
        
        return ' '.join(s_l)
        