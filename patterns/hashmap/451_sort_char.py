class Solution:
    def frequencySort(self, s: str) -> str:
        char_dict = {}
        for char in s:
            char_dict[char] = char_dict.get(char, 0)+1
        
        freq_arr = []
        for keys, values in char_dict.items():
            freq_arr.append([values, keys])
        freq_arr.sort(reverse=True)

        ans = ''
        for val, char in freq_arr:
            ans += (char*val)

        return ans