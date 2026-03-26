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