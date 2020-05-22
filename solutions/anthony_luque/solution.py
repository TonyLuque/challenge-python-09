from typing import List


class Solution:

    def duplicate_zeros(self, l: List[int]):

        i = 0
        while i < len(l):
            if l[i] == 0:
                l.insert(i, 0)
                l.pop()
                i += 2
            else:
                i += 1