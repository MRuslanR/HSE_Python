"""
https://leetcode.com/problems/count-primes/description/
"""


class Solution(object):
    def countPrimes(self, n):
        if n < 2:
            return 0
        primes = [1] * (n + 1)
        p = 2
        ans = n - 2
        while p * p <= n:
            if primes[p] == 1:
                for i in range(p * p, n + 1, p):
                    primes[i] = 0
                    ans -= 1
            p += 1

        ans = 0
        for i in range(n):
            ans += primes[i]
        return ans - 2
