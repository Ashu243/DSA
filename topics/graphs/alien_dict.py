from collections import deque
words = ["ab", "cd", "ef", "ad"]

def alien_dict(words):

    adj_list = {}
    indegrees = {}

    for word in words:
        for ch in word:
            if ch not in adj_list:
                adj_list[ch] = []
                indegrees[ch] = 0

    
    for i in range(len(words)-1):
        current_word = words[i]
        next_word = words[i+1]

        # words = ["abc", "ab"] that's why this is necessary
        if len(current_word) > len(next_word) and current_word.startswith(next_word):
            return ""

        for j in range(min(len(current_word), len(next_word))):
            if current_word[j] != next_word[j]:
                adj_list[current_word[j]].append(next_word[j])
                indegrees[next_word[j]] += 1
                break

    print(adj_list)
    print(indegrees)
    queue = deque([])

    for ch, val in indegrees.items():
        if val == 0:
            queue.append(ch)
    
    result = []

    while queue:
        ch = queue.popleft()
        result.append(ch)
        values = adj_list[ch]
        for ch in values:
            indegrees[ch] -= 1
            if indegrees[ch] == 0:
                queue.append(ch)
    
    if len(result) == len(adj_list):
        return "".join(result)
    
    return ""


print(alien_dict(words))