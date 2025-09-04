<<<<<<< HEAD
def movezero(nums):
    n = len((nums))
    for i in range(n):
        if nums[i]==0:
            j=i
            break

    for i in range(j,n):
        if nums[i]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            j+=1

nums = [0,1,0,3,12]
movezero(nums)
=======
def movezero(nums):
    n = len((nums))
    for i in range(n):
        if nums[i]==0:
            j=i
            break

    for i in range(j,n):
        if nums[i]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            j+=1

nums = [0,1,0,3,12]
movezero(nums)
>>>>>>> 43770906e4a7262d2e46780fa65a746a602e35d3
print(nums)