import random
simple = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3',
            '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$',
            '%', '^', '&', '*', '_']
diff = []
print(len(simple))
s = random.sample(range(0, 71), k=71)
for i in range(len(simple)):
    k = simple[s[i]]
    diff.append(k)
    print(k)
hesh = ""
print(len(diff))
print(len(""))
for i in range(len(diff)):
    hesh += simple[i] + " "
    hesh += diff[i] + " "
with open('hesh.txt', 'w') as file: file.write(str(hesh))