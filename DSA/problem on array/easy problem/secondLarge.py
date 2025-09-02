def getSecondLargest(arr, n):
        # # Code Here
        # largest =0
        # slargest =0
        # for i in range(n):
        #         if arr[i] >largest:
        #                 largest =arr[i]
        # for j in range(n):
        #         if arr[j]>slargest and arr[j] <largest:
        #                 slargest = arr[j]
         
        # if slargest == 0:
        #     return -1
        # else:
        #     return slargest



        # arr.sort() 
        # n = len(arr)  
        # SecondLargest= 0     
        # for i in range(n,0,-1):
        #         if arr[i-1]<arr[n-1]:
        #                 SecondLargest = arr[i-1]
        #                 break
         
        # if SecondLargest == 0:
        #     return -1
        # else:
        #     return SecondLargest

        n = len(arr)
        largest = arr[0]
        slargest = -1
        for i in range(n):
                if largest < arr[i]:
                        slargest = largest
                        largest = arr[i]
                elif arr[i] < largest and arr[i] > slargest:
                        slargest = arr[i]
        return slargest
                                  
      

arr= [2,1,1,4,1,1,3]
ans =getSecondLargest(arr,len(arr))
print(ans)