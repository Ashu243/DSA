nums = [2,7,11,15]
target = 9


def two_sum(nums, target):
    my_dict = {}
    for i in range(len(nums)):
        remaining_value = target - nums[i]
        if remaining_value in my_dict:
            return [my_dict[remaining_value], i]
        my_dict[nums[i]] = i


print(two_sum(nums, target))

# my_dict = {"name": "Alice", "age": 25, 12: 1}

# for elem in my_dict:
#     print(my_dict[elem])
