
n = 7

def fibonacci_cal(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    
    return fibonacci_cal(n-1) + fibonacci_cal(n-2)

result = fibonacci_cal(n)
print(result)