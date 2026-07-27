letters = ["c","f","j"]
target = "a"


def nextGreaterLetter(letters, target):
    left = 0
    right = len(letters) - 1
    ans = letters[0]

    while left <= right:
        mid = (left+right) // 2

        if target < letters[mid]:
            ans = letters[mid]
            right = mid-1
        else:
            left = mid + 1
    
    return ans

print(nextGreaterLetter(letters, target))