class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        n = self.countAndSay(n-1)
        curr, counter = n[0], 1
        out = ''
        i = 1
        while i < len(n):
            if n[i] == curr:
                counter += 1
            else:
                out += str(counter) + str(curr)
                curr, counter = n[i], 1
            i += 1
        out += str(counter) + str(curr)
        return out
