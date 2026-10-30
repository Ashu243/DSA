
s = 'ccc'

def longest_palindrome(s):
    char_dict = {}

    for char in s:
        char_dict[char] = char_dict.get(char, 0) + 1

    result = 0
    remaining_val = 0
    for keys, values in char_dict.items():
        if values % 2 != 0:
            result += values - 1
            remaining_val += 1
        else:
            result += values
    
    if result % 2 == 0 and remaining_val > 0:
        result += 1
    return result


print(longest_palindrome(s))