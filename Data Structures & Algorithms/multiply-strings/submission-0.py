class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_int = 0
        num2_int = 0
        
        mult = 10 ** (len(num1)-1)
        for i in num1:
            num1_int += (ord(i) - 48) * mult
            mult //= 10

        mult = 10 ** (len(num2)-1)
        for i in num2:
            num2_int += (ord(i) - 48) * mult
            mult //= 10


        s = str(num1_int * num2_int)
        return s



