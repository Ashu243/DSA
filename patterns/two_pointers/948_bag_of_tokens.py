tokens = [100,200]
power = 150

def bag_tokens(tokens, power):
    score = 0
    left = 0
    right = len(tokens)-1
    tokens.sort()
    max_score = 0
    if power < tokens[0]:
        return 0
    while left <= right:
        max_score = max(score, max_score)
        if power >= tokens[left]:
            power -= tokens[left]
            score += 1
            left += 1

        elif power < tokens[left] and score > 0:
            power += tokens[right]
            right -= 1
            score -= 1
    
    return max_score

print(bag_tokens(tokens, power))


