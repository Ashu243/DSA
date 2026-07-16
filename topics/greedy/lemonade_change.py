bills = [5,5,5,10,20]

def lemonade_change(bills):
    five = 0
    ten = 0

    for i in range(len(bills)):
        if bills[i] == 5:
            five += 1
        elif bills[i] == 10:
            ten += 1
            five -= 1
        elif bills[i] == 20:
            if ten > 0:
                ten -= 1
                five -= 1
            else:
                five -= 3
        if five<0:
            return False
    
    return True

print(lemonade_change(bills))