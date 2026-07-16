# nums = [6, 3, 4, 1, 9, 7]

# def quickSort(nums, low, high):
#     if(low<high):
#         p = partition(nums, low, high)
#         quickSort(nums, low, p-1)
#         quickSort(nums, p+1, high)

# def partition(nums, low, high):
#     pivot = nums[low]
#     i,j = low, high

#     while i<j:
#         while i<=high and nums[i]<=pivot:
#             i += 1
        
#         while j>=low and nums[j]>pivot:
#             j -= 1
        
#         if(i<j):
#             nums[i], nums[j] = nums[j], nums[i]

#     nums[j], nums[low] = nums[low], nums[j]

#     return j

# quickSort(nums, 0, len(nums)-1)
# print(nums)


def quick_sort(nums, low, high):
    if(low < high):
        p = partition(nums, low, high)
        quick_sort(nums, low, p-1)
        quick_sort(nums, p+1, high)


nums = [4, 1, 3, 2, 6, 7, 9]

def partition(nums, low, high):
    pivot = nums[low]
    i, j = low, high

    while i< j:
        while i<= high and nums[i] <= pivot:
            i += 1

        while j>=low and nums[j] > pivot:
            j -= 1

        if(i< j):
            nums[i], nums[j] = nums[j], nums[i]

    nums[low], nums[j] = nums[j], nums[low]
    return j

quick_sort(nums, 0, len(nums)-1)
print(nums)