<<<<<<< HEAD
def left_rotate(arr):
    n = len(arr)
    rotated_element = arr[0]
    for i  in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = rotated_element


arr = [1,2,3,4,5,9,8,65,4,3]
left_rotate(arr)

=======
def left_rotate(arr):
    n = len(arr)
    rotated_element = arr[0]
    for i  in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = rotated_element


arr = [1,2,3,4,5,9,8,65,4,3]
left_rotate(arr)

>>>>>>> 43770906e4a7262d2e46780fa65a746a602e35d3
print(arr)