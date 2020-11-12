from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        offset = {
            '2': [0, 3],
            '3': [3, 3],
            '4': [6, 3],
            '5': [9, 3],
            '6': [12, 3],
            '7': [15, 4],
            '8': [19, 3],
            '9': [22, 4]
        }
        combos = []
        for i in range(len(digits)):
            digit = digits[i]
            number = offset[digit]
            if not combos:
                for i in range(number[1]):
                    letter = chr(ord('a') + number[0] + i)
                    combos.append(letter)
            else:
                buffer = []
                for combo in combos:
                    for i in range(number[1]):
                        letter = chr(ord('a') + number[0] + i)
                        buffer.append(combo + letter)
                combos = buffer

        return combos
