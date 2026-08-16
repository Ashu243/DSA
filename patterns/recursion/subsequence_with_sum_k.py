arr = [10, 1, 2, 7, 6, 1, 5]
k = 139

def subsequence_sum_k(arr, k):

    def recursion(index, sum):
        if sum == k:
            return True
        if sum > k:
            return False
        if len(arr) == index:
            return False
        
        take = recursion(index+1, sum+ arr[index])
        not_take = recursion(index+1, sum)
        return take or not_take
    return recursion(0, 0)

print(subsequence_sum_k(arr, k))

