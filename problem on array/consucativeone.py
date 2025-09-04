<<<<<<< HEAD
def consucutive_one(arr):
    n = len(arr)
    count_max = 0
    count = 0
    for i in range(n):
        if arr[i] == 1:
            count+=1
        elif arr[i]!= 1:
            count_max = max(count_max,count)
            count = 0
    count_max = max(count_max,count)
    return count_max








nums = [1,1,0,1,1,1]
print(consucutive_one(nums))
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.






class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count1 = 0
        count2=0
        n =len(nums)
        for i in range(n):
            if nums[i] == 1:
                count1+=1
            elif nums[i] !=1:
                if count2<count1:
                    count2 = count1
                count1 =0
        if count2 ==0 or count2<count1 :
            return count1
        else:
            return count2

=======
def consucutive_one(arr):
    n = len(arr)
    count_max = 0
    count = 0
    for i in range(n):
        if arr[i] == 1:
            count+=1
        elif arr[i]!= 1:
            count_max = max(count_max,count)
            count = 0
    count_max = max(count_max,count)
    return count_max








nums = [1,1,0,1,1,1]
print(consucutive_one(nums))
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.






class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count1 = 0
        count2=0
        n =len(nums)
        for i in range(n):
            if nums[i] == 1:
                count1+=1
            elif nums[i] !=1:
                if count2<count1:
                    count2 = count1
                count1 =0
        if count2 ==0 or count2<count1 :
            return count1
        else:
            return count2

>>>>>>> 43770906e4a7262d2e46780fa65a746a602e35d3
