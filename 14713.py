import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

parrots = []

for _ in range(N):
    q = deque(input().split())
    parrots.append(q)

L = deque(input().split())

while L:
    temp = L.popleft()
    flag = False
    
    i = 0
    
    while i < len(parrots):
        parrot = parrots[i]
        
        
        if parrot[0] == temp:
            parrot.popleft()
            flag = True
            
            if not parrot:
                parrots.pop(i)
            
            else:
                i += 1
                
            break # 일치하지 않는 앵무새 찾음
        
        else:
            i += 1
            
    if not flag: # flag == False인 경우
        print('Impossible')
        exit(0)

if parrots:
    print('Impossible')
    
else:
    print('Possible')
    
'''
parrots.remove() 를 해서 parrots 의 전체 길이가 달라지는 상황 발생
for parrot 말고 while i < len(parrots) 로 수정

break()문은 가까운 조건문만 중지. -> 바깥의 남아 있는 반복문 돌아가는 상황 발생
exit() 시스템 종료 -> 확실한 종료 가능(오류 앵무새 발견 시 굳이 더 찾아볼 필요 없다)
'''
