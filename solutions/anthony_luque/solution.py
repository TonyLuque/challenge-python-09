"""Script que duplica los 0 encontrados en una lista"""
from typing import List

"""Clase en la que se implementa la función"""
class Solution:
    """Duplica los 0 que encuentre en el arreglo"""
    def duplicate_zeros(self, l: List[int]):

        i = 0
        while i < len(l):
            if l[i] == 0:
                l.insert(i, 0)
                l.pop()
                i += 2
            else:
                i += 1
