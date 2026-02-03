# tail recursion
# def printNum(x, count):
#     if(count == 0):
#         return
#     print(x)
#     printNum(x, count - 1)

# printNum(48, 3)


def sumNum(sum, num, n):
    if num>n:
        print(sum)
        return
    sumNum(sum+num, num+1, n)

sumNum(0, 1, 5)


# def addNum(n):
#     if n == 1:
#         return n
#     return n + addNum(n-1)

# result = addNum(4)
# print(result)

# def fact(n):
#     if n == 1:
#         return n
#     return n * fact(n-1)

# result = fact(5)
# print(result)

# fact = 1
# for i in range(1, 6):
#     fact = fact * i
    
# print(fact)


arr = [2, 5, 6, 9, 2, 6, 3, 5]
left = 0
right = len(arr) - 1

# def reverseArr(left, right):
#     if left >= right:
#         return
#     arr[left], arr[right] = arr[right], arr[left]
#     return reverseArr(left+1, right-1)

# reverseArr(left, right)
# print(arr)

while right >= left:
    arr[left], arr[right] = arr[right], arr[left]
    left +=1 
    right -=1 

print(arr)