arr = [0, 10, 0]
n = 0

def subsequence_count(arr, n):
    count = 0

    def backtracking(idx, sum):
        nonlocal count
        if idx >= len(arr):
            if sum == n:
                count+= 1
            return
        if sum > n:
            return
        sum += arr[idx]
        backtracking(idx+1, sum)

        sum -= arr[idx]
        backtracking(idx+1, sum)
    backtracking(0, 0)

    return count

print(subsequence_count(arr, n))



