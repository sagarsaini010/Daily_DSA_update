# a = 2
# b= 3
# a = a^b
# b = a^b
# a = a^b
# print(a,b)


n= 13
i =2
# if n & (1 << i) != 0:
#     print("set")
# else:
#     print("not set")

# if (n >> i) & 1 == 0:
#     print("not set")
# else:
#     print("set")

# n & ~(1 << i)
def findOneOccurnce(arr):
    ans = 0
    for bitIndex in range(32):
        count = 0
        for i in range(len(arr)):
            if arr[i] & (1 << bitIndex):
                count+=1
        if count % 3 == 1:
            ans = ans | (1 << bitIndex)
    return ans


arr = [1,1,1,2,2,2,3,3,3,4]

print(findOneOccurnce(arr))