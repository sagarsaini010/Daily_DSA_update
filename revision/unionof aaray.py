def union(arr1,arr2):
    left = 0
    right = 0
    result = []
    n = len(arr1)
    m = len(arr2)
    while left < n and right < m:
        while left > 0 and left < n and arr1[left] == arr1[left-1]:
            left+=1
        while right > 0 and right < m and arr2[right] == arr2[right-1]:
            right+=1
        if left >= n or right >= m:
            break

        if arr1[left] < arr2[right]:
            result.append(arr1[left])
            left+=1
        elif arr2[right] < arr1[left]:
            result.append(arr2[right])
            right+=1
        elif arr1[left] == arr2[right]:
            result.append(arr1[left])
            left+=1
            right+=1
    
    while left < n:
        if left ==0 or arr1[left] != arr1[left-1]:
            result.append(arr1[left])
        left+=1
    while right < m:
        if right == 0 or arr2[right] != arr2[right-1]:
            result.append(arr2[right])
        right+=1
    return result
                
arr1= [1,2,3,4,5,6,8]        
arr2= [2,3,4,5,5,6,7]        

print(union(arr1,arr2))