from collections import deque
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

def word_ladder(beginWord, endWord, wordList):
    if beginWord == endWord:
        return 0
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
    

    queue = deque([])
    queue.append((beginWord, 1))

    while queue:
        current_word, level = queue.popleft()
        if current_word == endWord:
            return level
        
        for i in range(len(current_word)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                new_word = current_word[:i]+ch+current_word[i+1:]
                if new_word in wordSet:
                    queue.append((new_word, level+1))
                    wordSet.remove(new_word)
    
    return 0
print(word_ladder(beginWord, endWord, wordList))
