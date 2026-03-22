nums = [1, 2, 3, 3, 3, 3, 3, 4, 6, 7, 8, 8, 9, 9]
target = 3

# def first_occurence(nums, target):
#     right = len(nums)-1
#     left = 0
#     first_occ = -1

#     while left<=right:
#         mid = (left+right)//2
#         if nums[mid]>=target:
#             first_occ = mid
#             right = mid -1
#         else:
#             left = mid+1
#     return first_occ

# def last_occurence(nums, target):
#     right = len(nums)-1
#     left = 0
#     last_occ = -1
#     while left<=right:
#         mid = (left+right)//2
#         if nums[mid] > target:
#             last_occ = mid-1
#             right = mid-1
#         else:
#             left = mid+1
#     return last_occ

            


# result1 = first_occurence(nums, target)
# result2 = last_occurence(nums, target)
# print([result1, result2])



def first_last_occ(nums, target):
    def first_occurence(nums, target):
        right = len(nums)-1
        left = 0
        first_occ = -1

        while left<=right:
            mid = (left+right)//2
            if nums[mid] >= target:
                if nums[mid] == target:
                    first_occ = mid
                right = mid -1
            else:
                left = mid+1
        return first_occ


    def last_occurence(nums, target):
        right = len(nums)-1
        left = 0
        last_occ = -1

        while left<=right:
            mid = (left+right)//2
            if nums[mid] <= target:
                if nums[mid] == target:
                    last_occ = mid
                left = mid+1
            else:
                right = mid-1
        return last_occ


    result1 = first_occurence(nums, target)
    result2 = last_occurence(nums, target)

    return [result1, result2]

print(first_last_occ(nums, target))