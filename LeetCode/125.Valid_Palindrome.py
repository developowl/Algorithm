class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = " ".join(word.lower() for word in s if word.isalnum())
        reverse_s = s[::-1]
        
        if s == reverse_s:
            return True
        else:
            return False


# Test Case)
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))
