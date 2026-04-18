val = [60, 100, 140]
wt = [10, 20, 40]
capacity = 50


def fractional_knapsack(val, wt, capacity):
    items = []

    for i in range(len(val)):
        ans = val[i] / wt[i]
        items.append([ans,val[i],wt[i]])

    items.sort(reverse=True)
    print(items)
    output = 0
    i= 0

    for ratio, value, weight in items:
        if capacity >= weight:
            output += value
            capacity -= weight
        else:
            output += ratio * capacity
    return output

print(fractional_knapsack(val, wt, capacity))
