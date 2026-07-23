fruits = [1,2,3,2,2]

def fruits_basket(fruits):
    left = 0
    fruitsdict = {}
    maxfruits = 0

    for right in range(len(fruits)):
        fruitsdict[fruits[right]] = fruitsdict.get(fruits[right], 0)+1

        if len(fruitsdict) > 2:
            fruitsdict[fruits[left]] = fruitsdict[fruits[left]] -1
            if  fruitsdict[fruits[left]] == 0:
                fruitsdict.pop(fruits[left])
            
            left += 1
        if len(fruitsdict) <= 2:
            maxfruits = max(maxfruits, right-left+1)

    return maxfruits

print(fruits_basket(fruits))