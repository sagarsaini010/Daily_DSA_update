def removeOuterParentheses( s):
       count = 0
       out_result = ""

       for char in s:
            if char =='(':
                if count > 0:
                    out_result +=char
                count+=1
            elif char == ')':
                count-=1
                if count > 0:
                    out_result += char
       return out_result 