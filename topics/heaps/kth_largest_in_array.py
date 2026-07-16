import heapq
arr = [3,2,1,5,6,4]
k = 2


# using max heap
# def k_largest_elem(arr, k):
#     n = len(arr)

#     def heapify_down(arr, index):
#         size = len(arr)
#         leftidx = (2*index)+1
#         rightidx = (2*index)+2
#         largestidx = index

#         if leftidx < size and arr[largestidx] < arr[leftidx]:
#             largestidx = leftidx
#         if rightidx < size and arr[largestidx] < arr[rightidx]:
#             largestidx = rightidx

#         if largestidx != index:
#             arr[index], arr[largestidx] = arr[largestidx], arr[index]
#             heapify_down(arr, largestidx)

#     for i in range((n // 2) - 1, -1, -1):
#         heapify_down(arr, i)

#     for _ in range(k-1):
#         arr[0], arr[-1] = arr[-1], arr[0]
#         arr.pop()
#         heapify_down(arr, 0)
#     return arr[0]


# print(k_largest_elem(arr, k))


def k_largest_elem(arr, k):
    ans = []
    n = len(arr)

    for i in range(k):
        heapq.heappush(ans, arr[i])
    
    for j in range(k, n):
        if arr[j] > ans[0]:
            heapq.heappop(ans)
            heapq.heappush(ans, arr[j])

    print(ans)
    return ans[0]

print(k_largest_elem(arr, k))