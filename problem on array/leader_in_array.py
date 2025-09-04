<<<<<<< HEAD
# def leaders_in_array(arr):
#     n = len(arr)
#     i = n-2
#     ans = []
#     ans.append(arr[n-1])
#     while i >= 0:
#         if arr[i] > ans[-1]:
#             ans.append(arr[i])
#         i-=1
#     return ans[::-1]

# arr = [10, 22, 12, 3, 0, 6]
# print(leaders_in_array(arr))

# import matplotlib.pyplot as plt
# def visualize_leaders(arr, leaders):
#     indices = list(range(len(arr)))
#     colors = ['skyblue'] * len(arr)

#     # Mark leader bars in a different color
#     for idx, _ in leaders:
#         colors[idx] = 'orange'

#     plt.bar(indices, arr, color=colors)
#     plt.xticks(indices, [f'Index {i}' for i in indices])
#     plt.ylabel('Value')
#     plt.title('Leaders in Array')
#     plt.show()

# # Run the visualization
# arr = [10, 22, 12, 3, 0, 6]
# leaders =visualize_leaders(arr)
# visualize_leaders(arr, leaders)

import matplotlib.pyplot as plt

# Function to find leaders in the array
def find_leaders(arr):
    leaders = []
    max_from_right = float('-inf')
    for i in reversed(range(len(arr))):
        if arr[i] > max_from_right:
            leaders.append((i, arr[i]))
            max_from_right = arr[i]
    return leaders[::-1]  # Reverse to maintain original order

# Visualization function
def visualize_leaders(arr, leaders):
    indices = list(range(len(arr)))
    colors = ['skyblue'] * len(arr)

    # Mark leader bars in a different color
    for idx, _ in leaders:
        colors[idx] = 'orange'

    plt.bar(indices, arr, color=colors)
    plt.xticks(indices, [f'Index {i}' for i in indices])
    plt.ylabel('Value')
    plt.title('Leaders in Array')
    plt.show()

# Run the visualization
arr = [10, 22, 12, 3, 0, 6]
leaders = find_leaders(arr)
visualize_leaders(arr, leaders)
=======
# def leaders_in_array(arr):
#     n = len(arr)
#     i = n-2
#     ans = []
#     ans.append(arr[n-1])
#     while i >= 0:
#         if arr[i] > ans[-1]:
#             ans.append(arr[i])
#         i-=1
#     return ans[::-1]

# arr = [10, 22, 12, 3, 0, 6]
# print(leaders_in_array(arr))

import matplotlib.pyplot as plt
def visualize_leaders(arr, leaders):
    indices = list(range(len(arr)))
    colors = ['skyblue'] * len(arr)

    # Mark leader bars in a different color
    for idx, _ in leaders:
        colors[idx] = 'orange'

    plt.bar(indices, arr, color=colors)
    plt.xticks(indices, [f'Index {i}' for i in indices])
    plt.ylabel('Value')
    plt.title('Leaders in Array')
    plt.show()

# Run the visualization
arr = [10, 22, 12, 3, 0, 6]
leaders =visualize_leaders(arr)
visualize_leaders(arr, leaders)

>>>>>>> 43770906e4a7262d2e46780fa65a746a602e35d3
