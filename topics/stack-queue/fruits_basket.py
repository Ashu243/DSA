fruits = [3,3,3,1,2,1,1,2,3,3]

# def fruits_basket(fruits):
#     n = len(fruits)
#     left, right = 0, 0
#     my_dict = {}
#     maximum = 0

#     while right<n:
#         my_dict[fruits[right]] = my_dict.get(fruits[right], 0)+1
#         while len(my_dict) > 2:
#             my_dict[fruits[left]] -= 1
#             if my_dict[fruits[left]] == 0:
#                 del my_dict[fruits[left]]
#             left += 1

#         maximum = max(maximum, right-left+1)
#         right += 1
    
#     return maximum

# print(fruits_basket(fruits))


def fruits_basket(fruits):
    n = len(fruits)
    left, right = 0, 0
    my_dict = {}
    maximum = 0

    while right<n:
        my_dict[fruits[right]] = my_dict.get(fruits[right], 0)+1
        if len(my_dict) > 2:
            my_dict[fruits[left]] -= 1
            if my_dict[fruits[left]] == 0:
                del my_dict[fruits[left]]
            left += 1

        if len(my_dict)<=2:
            maximum = max(maximum, right-left+1)
        right += 1
    
    return maximum

print(fruits_basket(fruits))


        

