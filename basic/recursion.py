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



# palindrome

# check a string is palindrome or not
string = 'nitir'

# index = len(string) - 1
# temp = ''
# for i in range(index):
#     ch = string[i]
#     temp = ch + temp

# if(string == temp):
#     print('palindrome string!')
# else:
#     print('Not a palindrome String!')

# def palindrome_checker(index):
#     if(index < 0):
#         return ""
#     return string[index] + palindrome_checker(index-1)

# result = palindrome_checker(index)
# print(result)



# string2 = 'nitir'

# left = 0 
# right = len(string2) -1

# def palindrome_checker(left, right):
#     if(left >= right):
#         return "palindrome string"
#     if(string2[left] != string2[right]):
#         return "Not a palindrome string"
#     return palindrome_checker(left+1, right-1)

# result = palindrome_checker(left, right)
# print(result)

string1 = 'hey there'


string = ['h', 'e', 'l', 'l', 'o']
left = 0
right = len(string) - 1


def reverseStr(left, right):
    if(left >= right):
        return string
    string[left], string[right] = string[right], string[left]

    return reverseStr(left+1, right-1)

result = reverseStr(left, right)
print(result)



n = 6

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(n))