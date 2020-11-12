class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        str_pointer = 0
        while str_pointer < len(s):
            if s[str_pointer] == 'M':
                inc = 1
                num += 1000
                if str_pointer + 1 < len(s) and s[str_pointer + 1] == 'M':
                    inc += 1
                    num += 1000
                    if str_pointer + 2 < len(s) and s[str_pointer + 2] == 'M':
                        inc += 1
                        num += 1000
                str_pointer += inc                
            elif s[str_pointer] == 'D':
                num += 500
                str_pointer += 1
            elif s[str_pointer] == 'C':
                inc = 1
                if str_pointer + 1 < len(s) and s[str_pointer + 1] == 'M':
                    inc += 1
                    num += 900
                elif str_pointer + 1 < len(s) and s[str_pointer + 1] == 'D':
                    inc += 1
                    num += 400
                else:
                    num += 100
                    if str_pointer + 1 < len(s) and s[str_pointer + 1] == 'C':
                        inc += 1
                        num += 100
                        if str_pointer + 2 < len(s) and s[str_pointer + 2] == 'C':
                            inc += 1
                            num += 100
                str_pointer += inc
            elif s[str_pointer] == 'L':
                num += 50
                str_pointer += 1
            elif s[str_pointer] == 'X':
                inc = 1
                if str_pointer + 1 < len(s) and s[str_pointer + 1] == 'C':
                    inc += 1
                    num += 90
                elif str_pointer + 1 < len(s) and s[str_pointer + 1] == 'L':
                    inc += 1
                    num += 40
                else:
                    num += 10
                    if str_pointer + 1 < len(s) and s[str_pointer + 1] == 'X':
                        inc += 1
                        num += 10
                        if str_pointer + 2 < len(s) and s[str_pointer + 2] == 'X':
                            inc += 1
                            num += 10
                str_pointer += inc
            elif s[str_pointer] == 'V':
                num += 5
                str_pointer += 1
            elif s[str_pointer] == 'I':
                inc = 1
                if str_pointer + 1 < len(s) and s[str_pointer + 1] == 'X':
                    inc += 1
                    num += 9
                elif str_pointer + 1 < len(s) and s[str_pointer + 1] == 'V':
                    inc += 1
                    num += 4
                else:
                    num += 1
                    if str_pointer + 1 < len(s) and s[str_pointer + 1] == 'I':
                        inc += 1
                        num += 1
                        if str_pointer + 2 < len(s) and s[str_pointer + 2] == 'I':
                            inc += 1
                            num += 1
                str_pointer += inc
        return num
