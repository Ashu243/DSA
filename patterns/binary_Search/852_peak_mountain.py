arr = [0,2,1,0]

def peakIndexInMountainArray(arr):
        left = 0
        right = len(arr)-1

        while left<=right:
            mid = (left+right) // 2
            
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] < arr[mid+1]:
                left = mid+1
            else:
                right = mid-1
            
print(peakIndexInMountainArray(arr))