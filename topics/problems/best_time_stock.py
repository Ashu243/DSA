prices = [7,6,4,3,1]

# def max_profit(prices):
#     n = len(prices)
#     profit = 0
#     max_profit = float('-inf')
#     for i in range(n):
#         for j in range(i+1, n):
#             profit = prices[j] - prices[i]
#             if profit > max_profit:
#                 max_profit = profit

#     if max_profit<0:
#         return 0
#     return max_profit
# print(max_profit(prices))

def max_profit(prices):
    n = len(prices)
    min_price = float('inf')
    max_sum = 0
    for i in range(n):
        if prices[i] < min_price:
            min_price = prices[i]
        
print(max_profit(prices))
