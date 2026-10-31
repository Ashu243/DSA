nums = [0,1,2,2,3,0,4,2]
val = 2

# keeping the good elements at the starting of the list
def remove_element(nums, val):
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

print(remove_element(nums, val))


def removeElement(self, nums: list[int], val: int) -> int:
    left = 0
    right = len(nums)-1
    while left <=right:
        if nums[right] == val:
            right -= 1
        elif nums[left] != val:
            left += 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
            left += 1
    return left