def largestOddNumber(num):
        n= len(num)
        index = -1
        if not num:
            return ""
        number = list(num)
        for i in range(n):
            if int(number[i])%2 !=0:
                index = i
        if index == -1:
            return ""
        else:
            return ''.join(number[0:index+1])

        
        