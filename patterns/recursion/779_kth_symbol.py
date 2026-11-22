n = 4
k = 1

def kth_symbol(n, k):
    if n == 1 and k == 1:
        return 0
    mid = (2**(n-1))//2
    if k <= mid:
        return kth_symbol(n-1, k)
    else:
        ans = kth_symbol(n-1, k-mid)
        if ans == 0:
            return 1
        return 0

print(kth_symbol(n, k))