import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    docs = deque(map(int, input().split()))
    
    result = 0
    
    while docs:
        if docs[0] < max(docs):
            docs.append(docs.popleft())
            
            if M == 0:
                M = len(docs) - 1
            
            else:
                M -= 1
            
        else:
            docs.popleft()
            result += 1
        
            if M == 0:
                break
            
            else:
                M -= 1
        
    print(result)
