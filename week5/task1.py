"""
https://leetcode.com/problems/insert-delete-getrandom-o1/
"""

import random


class RandomizedSet:
    def __init__(self):
        self.table = {}

    def insert(self, val):
        if val not in self.table:
            self.table[val] = 0
            return True
        return False

    def remove(self, val):
        if val in self.table:
            del self.table[val]
            return True
        return False

    def getRandom(self):
        return random.choice(list(self.table.keys()))
