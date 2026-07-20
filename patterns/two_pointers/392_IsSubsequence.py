
def isSubsequence(s: str, t: str) -> bool:
    arr1 = 0
    arr2 = 0
    n = len(s)

    if n == 0:
        return True

    while arr2 < len(t) and arr1 < n:
        if t[arr2] == s[arr1]:
            arr1 += 1

        arr2 += 1

    if n == arr1:
        return True

    return False