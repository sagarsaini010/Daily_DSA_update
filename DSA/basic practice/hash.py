# list_1 = [1,1,2,2,3,3,3,3,4,5,6,6]
# list_2 = [0]*7

# i=0
# while(i < len(list_1)):
#     list_2[list_1[i]]+=1
#     i+=1

# # print(list_2)

# x = int(input("Enter number for occurence"))

# print(list_2[x])

# string = 'aabcdedfedabc'

# list_s = [0]*26
# i = 0
# while i < len(string):
#     list_s[ord(string[i]) - ord('a')] += 1
#     i+=1
# x = input("enter a chracter")

# print(list_s[ord(x)- ord('a')])

# from collections import Counter
# l1 = [1,1,1,2,2,2,33,3444,5,532,2]
# dictn = {}
# i = 0 
# while i < len(l1):
#     dictn[l1[i]] = dictn.get(l1[i],0) + 1
#     i+=1

# x =int(input("enter a number"))

# print(dictn.get(x,0))

from collections import Counter

l1 = [1,1,2,2,2,3,3,4,44,5,6,7,7,7,77655]
dictn = Counter(l1)

# x = int(input("Enter a number: "))
# print(dictn)
for char , count in dictn.items():
    print(f"{char} : {count}")