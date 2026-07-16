import heapq
nums = [3,0,1,0]
k = 1

def top_frequent_elem(nums, k):
    mydict = {}

    for i in range(len(nums)):
        mydict[nums[i]] = mydict.get(nums[i], 0) + 1
    
    result = []
    for key, value in mydict.items():
        if len(result) < k:
            heapq.heappush(result, (value, key))
        else:
            if result[0][0] < value:
                heapq.heapreplace(result, (value, key))
    
    ans = []
    for i in range(k):
        ans.append(result[i][1])

    return ans


print(top_frequent_elem(nums, k))