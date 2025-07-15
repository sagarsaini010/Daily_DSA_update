class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = int(a, 2)
        num2 = int(b, 2)
        num1 += num2
        s = str(bin(num1)[2:])
        return s
