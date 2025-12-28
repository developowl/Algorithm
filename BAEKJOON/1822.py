import sys

input = sys.stdin.readline

A, B = map(int, input().split())

listA = sorted(list(map(int, input().split())))
listB = sorted(list(map(int, input().split())))

result = []


def binary_search(target, array):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == target:
            return True
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


for a in listA:
    if not binary_search(a, listB):
        result.append(a)

print(len(result))
if result:
    print(*(result))
