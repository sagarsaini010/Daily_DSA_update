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
print(nums)