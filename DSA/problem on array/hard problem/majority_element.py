def majority_element(arr):
    n = len(arr)
    x =int(n/3)+1  
    # mapp ={}
    ans =[]
    # for i in range(n):
    #     mapp[arr[i]] = mapp.get(arr[i],0)+1
    #     # if arr[i] in mapp and mapp[arr[i]] > x:
    #     if mapp[arr[i]] == x:
    #         # if len(ans)==0 or arr[i] !=ans[0]:
    #            ans.append(arr[i])
        # if len(ans)==2:
        #     break
    count1 =0 
    count2 =0
    el1 = -10**9
    el2 = -10**9
    for i in range(n):
        if count1 ==0 and el2 != arr[i]:
            count1+=1
            el1=arr[i]
        elif count2 == 0 and el1 != arr[i]:
            count2 +=1
            el2 = arr[i]
        elif arr[i] == el1:
            count1 +=1
        elif arr[i] == el2:
            count2 +=1
        else:
            count1 -=1
            count2 -=1
    count1 =0
    count2 =0
    for i in range(n):
        if arr[i] ==el1:
            count1+=1
        if arr[i] == el2:
            count2 +=1
    if count1 >= x:
        ans.append(el1)
    if count2 >= x:
        ans.append(el2)
    return ans

            
    


arr =[3,2,3]
ans = majority_element(arr)
print(ans)
