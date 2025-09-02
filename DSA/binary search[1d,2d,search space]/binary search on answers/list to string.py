l = [1,2,3,4,5]

s= "".join(map(str,l))
s= int(s)
s+=1
s= str(s)
nl = [int(char) for char in s]
print(nl)