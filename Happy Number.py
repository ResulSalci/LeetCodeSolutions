class Solution:
    def take_sum_square(n: int):
        result = 0
        temp = n
        while temp > 0:
            result += (temp % 10) ** 2
            temp //= 10

        return result

    def isHappy(self, n: int) -> bool:
        exist_sum = set()
        while n != 1:
            n = Solution.take_sum_square(n)
            print(n)
            if n in exist_sum:
                return False

            exist_sum.add(n)
        return True


