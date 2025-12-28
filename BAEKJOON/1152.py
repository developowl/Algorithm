import sys

input = sys.stdin.readline

strings = input()

count = 0

for ch in strings:
    if ch == " ":
        count += 1

if strings[0] == ' ':
    count -= 1

if strings[-1] == ' ':
    count -= 1

if strings[-2] == ' ':
    count -= 1
    
print(count + 1)
