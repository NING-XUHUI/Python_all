f = open('./gkb.txt', 'r')
# print(f.read())
str = f.read()
print(len(str))
str_n = {}
n_str = {}
for i in range(len(str)):
    n_str[i] = str[i]
    str_n[str[i]] = i
f.close()