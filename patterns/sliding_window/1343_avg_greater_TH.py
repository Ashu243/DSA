arr = [11,13,17,23,29,31,7,5,2,3]
k = 3
threshold = 5


def numofSubarray(arr, k, threshold):
    left = 0
    window_sum = 0
    result = 0

    for right in range(len(arr)):
        window_sum += arr[right]

        if right - left + 1 == k:
            if window_sum/k >= threshold:
                result += 1
            window_sum -= arr[left]
            left += 1
    return result

print(numofSubarray(arr, k, threshold))
