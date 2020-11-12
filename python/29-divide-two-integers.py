import math

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        err = 2147483647
        max_pos = 2147483647
        min_neg = -2147483648

        sign = ((dividend > 0) == (divisor > 0))
        dividend, divisor = abs(dividend), abs(divisor)
        
        power = 1
        tmp_dividend, tmp_divisor = dividend, divisor
        while tmp_dividend > tmp_divisor:
            tmp_dividend -= tmp_divisor
            power *= 2
            tmp_divisor *= 2
        
        quot = 0
        while power > 0:
            if dividend >= tmp_divisor:
                dividend -= tmp_divisor
                quot += power
            power >>= 1
            tmp_divisor >>= 1
        
        if sign:
            return err if quot > max_pos else quot
        else:
            return err if quot < min_neg else -quot
