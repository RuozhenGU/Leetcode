
class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        process = []
        lst = list(s)

        for idx, s in enumerate(lst):
            
            if s == '[':
                stack.append(idx)
            if s == ']':
                process.append((stack.pop(), idx))
                
        for idx, item in enumerate(process):
            l, r = item
            # parse
            num_str = ''
            digit_count = 0
            
            for _i in range(l-1, -1, -1):
                if lst[_i].isdigit():
                    num_str = lst[_i] + num_str
                    digit_count += 1
                else:
                    break
                    
            repeat = int(num_str)

            decode = lst[l+1: r] * repeat

            # mask all encode part to ''
            for i in range(l-digit_count, r+1):
                lst[i] = ''
                
            lst[l-digit_count] = ''.join(decode) # very important, make changes first does not affect index since you are working on list
            
        
        # remove all empty string
        str_new = ''.join(lst)
        
        
        return str_new