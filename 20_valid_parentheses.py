class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 0:          # if s is empty , retun 
            return True
        
        if len(s) % 2 != 0:      # if s's item no is odd , retun 
            return False
        
        par = {
            '(':')', 
            '{':'}', 
            '[':']'
        }

        stack = list()           # declare stack, to store the close character
        
        for i in range(len(s)):
            if par.get(s[i]):                  # if the character is in par
                stack.append(par.get(s[i]))    # store the correspondence close into stack
                                               # ** if it comes a "(", then store ")"

            else:                              # if the character is no in par, it cloud be:
                if len(stack) == 0:            # case (1) not a valid character (neither the open /close character)
                    return False               #          return False is this is the case
                if stack[-1] == s[i]:          # case (2) a close characher
                    stack.pop(-1)              #          it it is match the lastest close character, then it fulfill the closing order
                                               #          pop out the fulfiled pair
                else: 
                    return False
        
        if len(stack) > 0:
            return False
        
        return True


s = "({})[]"
x = Solution()
print(x.isValid(s))







                            
                            
                            
               

   
     
    