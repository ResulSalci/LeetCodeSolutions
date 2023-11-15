class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        lmao = str(x)
        for i in range(int(len(lmao) / 2)):
            if lmao[i] != lmao[len(lmao) - 1 - i]:
                return False
        return True
