<<<<<<< HEAD
def longest_palindrom(s):
    def find_palindrom(left,right):
        while left>=0 and right<len(s) and s[left] == s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    longest =""
    for i in range(len(s)):
        odd = find_palindrom(i,i)
       
        even = find_palindrom(i,i+1)
        current_long = max(odd,even,key=len)
        if len(current_long) > len(longest):
            longest = current_long
=======
def longest_palindrom(s):
    def find_palindrom(left,right):
        while left>=0 and right<len(s) and s[left] == s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    longest =""
    for i in range(len(s)):
        odd = find_palindrom(i,i)
       
        even = find_palindrom(i,i+1)
        current_long = max(odd,even,key=len)
        if len(current_long) > len(longest):
            longest = current_long
>>>>>>> 43770906e4a7262d2e46780fa65a746a602e35d3
    return longest