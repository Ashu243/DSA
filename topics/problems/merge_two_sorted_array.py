nums1 = [1, 1, 2, 3, 5, 5, 5, 7, 9]
nums2 = [-3, 1, 2, 3, 3, 4, 5, 7, 7]

def merge_sort(num1, num2):
    i, j = 0, 0
    n, m = len(num1), len(num2)
    result = []

    while i<n and j<m:
        if num1[i] <= num2[j]:
            if not result or result[-1] != num1[i]: 
                result.append(num1[i])
            i += 1
        
        else:
            if not result or result[-1] != num2[j]: 
                result.append(num2[j])
            j += 1 
    
    while i<n:
        if not result or result[-1] != num1[i]: 
            result.append(num1[i])
        i += 1

    while j<m: 
        if not result or result[-1] != num2[j]: 
            result.append(num2[j])
        j += 1

    return result

answer = merge_sort(nums1, nums2)
print(answer)
