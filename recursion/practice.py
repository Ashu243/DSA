# generate all parenthesis

n = 3
def generate_parenthesis(n):
    result = []

    def backtrack(current, opencount, closedcount):
        if len(current) == 2*n:
            result.append(current)
            return
        
        if opencount < n:
            backtrack(current+'(', opencount+1, closedcount)

        if closedcount < opencount:
            backtrack(current+')', opencount, closedcount+1)

    backtrack('', 0, 0)
    return result

print(generate_parenthesis(n))


digit = '34'

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

for ch in letter_num[digit[0]]:
    print(ch)