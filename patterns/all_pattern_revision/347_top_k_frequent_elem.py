import heapq
nums = [1,1,1,2,2,3]
k = 2


def k_frequent_elem(nums, k):
    numsdict = {}

    for num in nums:
        numsdict[num] = numsdict.get(num, 0)+1
    
    result = []
    for key, value in numsdict.items():
        if len(result) < k:
            heapq.heappush(result, (value, key))
        else:
            if result[0][0] < value:
                heapq.heapreplace(result, (value, key))
    for i in range(k):
        result[i] = result[i][1]
    return result

print(k_frequent_elem(nums, k))