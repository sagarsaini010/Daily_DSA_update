arr = [1,3,5,7,9,2,4,6,8,5,8]

# revers_arr = arr.reverse()
# print(arr)

# revers_arr= list(reversed(arr))
# print(revers_arr)
# print(arr)

# print(arr[ : :-1])

# rev_arr = []
# for i in range(len(arr)-1,-1,-1):
#     rev_arr.append(arr[i])
# print(rev_arr)

# left =0
# right= len(arr)-1
# count =0
# while left < right:
#     arr[left],arr[right] = arr[right] , arr[left]
#     left+=1
#     right-=1
#     count+=1

# print(arr,count)

def reverseArray( arr,i=None,rev_arr= None):
        # code here
        if i is None:
            i = len(arr)-1
        if rev_arr is None:
            rev_arr = []
        if i<0:
            return rev_arr
        rev_arr.append(arr[i])
        return reverseArray(arr,i-1,rev_arr)




print(reverseArray([2,3,4,5,6]))