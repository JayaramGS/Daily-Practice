import sys
import itertools

No_strings = int(input())

strings = []
while No_strings > 0:
    string = sys.stdin.readline().strip()
    strings.append(string)
    No_strings -= 1

mix = 9999999999
for i in itertools.permutations(strings, len(strings)):
    a = i[0]
    for j in range(1, len(i)):
        b = 0
        for k in range(0, len(a)):
            s = a[k:]
            if len(s) <= len(i[j]):
                if s == i[j][0:len(s)]:
                    a = a + i[j][len(s):]
                    b = 1
                    break
        if b == 0:
            a = a + i[j]
    if mix > len(a):
        mix = len(a)

print(mix)
