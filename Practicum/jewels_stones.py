count = 0
j = set(input())
s = input()

for i in set(j):
    for k in range(len(s)):
        if s[k] == i:
            count += 1

print(count)
