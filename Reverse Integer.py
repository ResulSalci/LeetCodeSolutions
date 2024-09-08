from math import log10, floor
class Solution:
    def is_invalid(self, x: int) -> bool:
        return not (-2**31 <= x <= 2**31 - 1)

    def reverse(self, x: int) -> int:
        if self.is_invalid(x):
            return 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        result = 0
        while x != 0:
            result = result * 10 + x % 10
            x //= 10
        result *= sign
        return 0 if self.is_invalid(result) else result