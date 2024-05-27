class Solution:
    def reverse(self, x: int) -> int:

        i = 1
        is_negative = x < 0
        x = abs(x)
        num = 0
        while(x > 0):
            rem = int(x % 10)
            print(f"rem:{rem}")
            x =  int(x // 10)
            num = num*10 + rem

        if not -2147483648 < num < 2147483647:
            return 0

        return num * -1 if is_negative  else num