class Solution:
    def merge(self, arr, l, mid, r):
        # Temporary array to store merged results
        temp = []
        left = l      # Starting index of left subarray
        right = mid + 1  # Starting index of right subarray

        # Merge elements from both subarrays in sorted order
        while left <= mid and right <= r:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        # Add remaining elements from the left subarray (if any)
        while left <= mid:
            temp.append(arr[left])
            left += 1

        # Add remaining elements from the right subarray (if any)
        while right <= r:
            temp.append(arr[right])
            right += 1

        # Copy merged elements back into the original array
        for i in range(l, r + 1):
            arr[i] = temp[i - l]

    def merge_sort(self, arr, l, r):
        # Base case: Array with one or no elements is already sorted
        if l >= r:
            return

        # Find the middle point of the array
        mid = (l + r) // 2

        # Recursively divide the left and right halves
        self.merge_sort(arr, l, mid)
        self.merge_sort(arr, mid + 1, r)

        # Merge the sorted halves
        self.merge(arr, l, mid, r)

# Example usage:
solution = Solution()
array = [5, 3, 8, 6, 2]
print("Original array:", array)
solution.merge_sort(array, 0, len(array) - 1)
print("Sorted array:", array)







# def sort(arr,l,mid,r):
#      tem =[]
#      left = l
#      right =  mid+1

#      while (left<=mid and right <=r):
#          if arr[left] <= arr[right]:
#              tem.append(arr[left])
#              left +=1
#          else:
#              tem.append(arr[right])
#              right +=1

#      while left<=mid :
#          tem.append(arr[left])
#          left+=1
#      while right <= r:
#          tem.append(arr[right])
#          right+=1
#      for i in range(l,r+1):
#          arr[i] = tem[i-l]



# def mergSort(arr,l,r):
#     if l>=r:
#         return
#     mid = int((l+r)/2)
#     mergSort(arr,l,mid)
#     mergSort(arr,mid+1,r)
#     sort(arr,l,mid,r)




# arr=[6,5,4,3,2,1]
# mergSort(arr,0,5)
# print(arr)