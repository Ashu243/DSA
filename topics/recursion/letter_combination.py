
digit = '23'

def letter_combination(digit):
    letter_num = {
    "2": 'abc',
    "3": 'def',
    "4": 'ghi',
    "5": 'jkl',
    "6": 'mno',
    "7": 'pqrs',
    "8": 'tuv',
    "9": 'wxyz',
    }
    result = []

    def backtrack(index, current):
        if index >= len(digit):
            result.append("".join(current))
            return
        
        for ch in letter_num[digit[index]]:
            current.append(ch)
            backtrack(index+1, current)
            current.pop()

    
    backtrack(0, [])
    return result

print(letter_combination(digit))