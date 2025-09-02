def isPalindrome( s: str,clear_str = None, i=None) -> bool:
        if clear_str is None:
            clear_str = ''.join(char for char in s if char.isalnum())
            clear_str = clear_str.lower()
        if i is None:
            i = 0
        if i > len(clear_str)//2:
            return True
        if clear_str[i] != clear_str[-(i+1)]:
            return False
        return isPalindrome(s,clear_str,i+1)



print(isPalindrome("A man, a plan, a canal: Panama"))
        