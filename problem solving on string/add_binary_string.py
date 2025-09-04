<<<<<<< HEAD
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = int(a, 2)
        num2 = int(b, 2)
        num1 += num2
        s = str(bin(num1)[2:])
        return s
=======
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = int(a, 2)
        num2 = int(b, 2)
        num1 += num2
        s = str(bin(num1)[2:])
        return s
>>>>>>> 43770906e4a7262d2e46780fa65a746a602e35d3
