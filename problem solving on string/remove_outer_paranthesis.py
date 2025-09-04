<<<<<<< HEAD
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
=======
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
>>>>>>> 43770906e4a7262d2e46780fa65a746a602e35d3
       return out_result 