gain = [-5, 1, 5, 0, -7]

def highest_altitude(gain):
    max_sum = gain[0]
    curr_sum = 0

    for i in range(len(gain)):
        curr_sum += gain[i]
        max_sum = max(max_sum, curr_sum)
    
    return max_sum

print(highest_altitude(gain))