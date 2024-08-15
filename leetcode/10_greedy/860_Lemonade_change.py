class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0

        for b in bills:
            five += 1 if b == 5 else 0
            ten += 1 if b == 10 else 0
            change = b - 5

            if change == 5:
                if five:
                    five -= 1
                else:
                    return False
            elif change == 15:
                if five and ten:
                    five, ten = five - 1, ten - 1
                elif five >= 3:
                    five -= 3
                else:
                    return False

        return True
