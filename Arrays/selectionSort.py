# arr = [3, 6, 2, 1, 7, 4]

# ascending order
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
    
#     arr[i], arr[min_index] = arr[min_index], arr[i]

# print(arr)


# descending order
# for i in range(len(arr)):
#     max_index = i
#     for j in range(i+1, len(arr)):
#         if(arr[j] > arr[max_index]):
#             max_index = j

#     arr[i], arr[max_index] = arr[max_index], arr[i]

# print(arr)


# class Solution:
#     def selectionSort(self, nums: List[int]) -> List[int]:
#         for i in range(len(nums)):
#             min_index = i
#             for j in range(i+1, len(nums)):
#                 if nums[j]< nums[min_index]:
#                     min_index = j
        
#         nums[i], nums[min_index] = nums[min_index], nums[i]

#         return nums