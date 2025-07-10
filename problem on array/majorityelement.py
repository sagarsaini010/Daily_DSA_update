# def majority_element(arr):
#     n = len(arr)
#     count = 0

#     for i in range(n):
#         if count ==0:
#             el = arr[i]
#             count+=1
#         elif el == arr[i]:
#             count+=1
#         else:
#             count-=1
#     return el

# nums = [2,2,1,1,1,2,2]
# print(majority_element(nums))






def majorityElement(nums):
        n = len(nums)
        count=0
        count1=0
        for i in range(n):
            if count == 0:
                count+=1
                el=nums[i]
            elif nums[i] == el:
                count+=1
            else:
                count-=1
        for i in range(n):
            if nums[i]==el:
                count1+=1
            if count1 > int(n/2):
                return el
         
nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
