class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        while num >= 1000:
            roman += 'M'
            num -= 1000
        if num >= 100:
            cent = num // 100
            if cent >= 5:
                if cent == 9:
                    roman += 'CM'
                else:
                    roman += 'D'
                    roman += 'C' * (cent - 5)
            else:
                if cent == 4:
                    roman += 'CD'
                else:
                    roman += 'C' * cent
            num = num % 100
        if num >= 10:
            dec = num // 10
            if dec >= 5:
                if dec == 9:
                    roman += 'XC'
                else:
                    roman += 'L'
                    roman += 'X' * (dec - 5)
            else:
                if dec == 4:
                    roman += 'XL'
                else:
                    roman += 'X' * dec
            num = num % 10
        if num >= 5:
            if num == 9:
                roman += 'IX'
            else:
                roman += 'V'
                roman += 'I' * (num - 5)
        else:
            if num == 4:
                roman += 'IV'
            else:
                roman += 'I' * num
        
        return roman
