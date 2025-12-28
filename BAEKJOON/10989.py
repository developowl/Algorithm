import sys

input = sys.stdin.readline

def heap_sort(arr):
    n = len(arr)

    for i in range( n //2 -1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i +2

    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

N = int(input())

numbers = []

for _ in range(N):
    numbers.append(int(input()))

heap_sort(numbers)

for num in numbers:
    print(num)
    