# LeetCode 125. Valid Palindrome
import collections
from typing import Deque

# 내 풀이
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = " ".join(word.lower() for word in s if word.isalnum())
        reverse_s = s[::-1]

        if s == reverse_s:
            return True
        else:
            return False


# # Sol 2) 리스트로 반환
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         strs = []
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())

#         # 팰린드롬 여부 판별
#         while len(strs) > 1:
#             if strs.pop(0) != strs.pop():
#                 return False
#         return True


# Sol 3) deque를 사용한 최적화
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         strs: Deque = collections.deque()
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())

#             while len(strs) > 1:
#                 if strs.popleft() != strs.pop():
#                     return False
#             return True


# Test Case)
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))
