n = [1, 3, 5, 7, 4, 3, 7, 4, 2, 4, 10]
m = [10, 111, 2, 5, 50, 2, 7]

my_dict = {}

for i in range(len(n)):
    my_dict[n[i]] = my_dict.get(n[i], 0)+1

for j in range(len(m)):
    if m[j] in my_dict:
        print(m[j], ':', my_dict.get(m[j]))

# print(my_dict)
s = 'aabhhsoigjsjsssjjjghhr'
q = ['a', 'h', 'f', 'j', 'i']
hash_list = [0]*26

for ch in s:
    ascii_val = ord(ch)
    index = ascii_val - 97
    hash_list[index] += 1

for ch in q:
    ascii_val = ord(ch)
    index = ascii_val - 97 
    print(ch,':' ,hash_list[index])

# print(hash_list)



