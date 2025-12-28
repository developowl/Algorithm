# import sys

# input = sys.stdin.readline

# def quick_sort(arr,low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         quick_sort(arr, low, pi - 1)
#         quick_sort(arr, pi + 1, high)

# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1

#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
    
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1

# N = int(input())

# numbers = []

# for _ in range(N):
#     x, y = map(int, input().split())
#     numbers.append((y, x))

# quick_sort(numbers, 0, N - 1)

# for y_value, x_value in numbers:
#     print(x_value, y_value)

# ----시간 초과로 인한 .sort 사용,,,
import sys

input = sys.stdin.readline
N = int(input())
numbers = []

for _ in range(N):
    x, y = map(int, input().split())
    numbers.append((y, x))

numbers.sort()

for y_value, x_value in numbers:
    print(x_value, y_value)
