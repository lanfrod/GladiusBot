import random, os
simple = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
          'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
          'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
          'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3',
          '4', '5', '6', '7', '8', '9', '0']
diff = []
s = random.sample(range(0, 62), k=62)
for i in range(len(simple)):
    diff.append(simple[s[i]])
hesh = ""
for i in range(len(diff)):
    hesh += simple[i] + " "
    hesh += diff[i] + " "
with open('hesh.txt', 'w') as file: file.write(str(hesh))