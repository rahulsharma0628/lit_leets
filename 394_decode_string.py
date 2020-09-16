class Solution:
    def decodeString(self, s: str) -> str:
        
        final = []
        
        for ch in s:
            if ch == ']':
                subs = []
                
                while final[-1]!='[':
                    subs.append(final.pop())
                final.pop()
                
                n = 0
                dec = 0
                
                while (len(final)>0 and final[-1].isnumeric()):
                    n = n + 10**dec*int(final.pop())
                    dec+=1
                
                for i in range(n):
                    for j in range(len(subs)):
                        final.append(subs[len(subs)-1-j])           
            
            else:
                final.append(ch)
        return ''.join(final)