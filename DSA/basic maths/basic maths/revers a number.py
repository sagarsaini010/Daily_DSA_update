def revers(n):
    rev = 0
    while(n!=0):
        rem = n%10
        rev = (rev*10)+rem
        n = int(n/10)
    return rev
        

print(revers(121))


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending in 0 (but not 0 itself) can't be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For even digit count: x == reversed_half
        # For odd digit count: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10