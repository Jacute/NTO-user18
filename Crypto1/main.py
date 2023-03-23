import string


with open('hashed', 'r') as f:
    data = f.read()
with open('8cc2c71b-6aed-451b-b346-fa1bee0501a1_hashed.txt', 'r') as f:
    data1 = f.read()
data1 = list(map(int, data1[1:-1:].split(', ')))
data = list(map(int, data[1:-1:].split(', ')))
alphabet = string.ascii_lowercase + '1234567890' + '{}_!?'
flag = ''
for i in data1:
    flag += alphabet[data.index(i)]
print(flag)
