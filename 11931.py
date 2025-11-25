import sys

input = sys.stdin.readline

def merge_sort(arr):
  if len(arr) <= 1:
    return arr

  # 1. Divide (분할)
  mid = len(arr) // 2       # 리스트를 절반으로 나눌 인덱스
  left_half = arr[:mid]     # 왼쪽 절반
  right_half = arr[mid:]    # 오른쪽 절반

  # 재귀적으로 각 절반을 다시 정렬
  left_sorted = merge_sort(left_half)
  right_sorted = merge_sort(right_half)

  # 2. Conquer (병합)
  return merge(left_sorted, right_sorted)

def merge(left, right):
  result = []
  i = 0  # left 리스트의 인덱스
  j = 0  # right 리스트의 인덱스

  while i < len(left) and j < len(right):
    if left[i] > right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  # 한쪽 리스트의 요소가 모두 소진되었을 때,
  # 남아있는 다른 쪽 리스트의 요소들을 result 뒤에 그대로 붙임
  result.extend(left[i:])
  result.extend(right[j:])
  
  return result


N = int(input())

numbers = []

for _ in range(N):
  numbers.append(int(input()))

sorted_numbers = merge_sort(numbers)

for num in sorted_numbers:
  print(num)
  