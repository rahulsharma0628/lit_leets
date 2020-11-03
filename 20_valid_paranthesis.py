class Solution:
    def isValid(self, s: str) -> bool:
        
        if s[0] == ')' or s[0] == '}' or s[0] == ']':
            return False
        
        paranthesis = dict({
            ')':'(', '}':'{', ']':'['
        })
        
        stack = [s[0]]        
        for p in s[1:]:
            # print(stack)
            if p in paranthesis:
                top = stack.pop() if stack else '*'
                
                if paranthesis[p] != top:
                    return False
            else:
                stack.append(p)        
        
        return not stack
            
            
        