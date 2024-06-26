#https://leetcode.com/problems/assign-cookies
from collections import deque
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        result = 0
        g.sort()
        s.sort()

        long_length = max(len(g),len(s))
        kid_deque = deque(g[:])
        cookie_deque = deque(s[:])
        for _ in range(long_length):
            if len(kid_deque) == 0 or len(cookie_deque) == 0:
                return result
            if kid_deque[0] <= cookie_deque[0]:
                result +=1
                kid_deque.popleft()
            cookie_deque.popleft()
        return cookie

s = Solution()
result = s.findContentChildren([1,2,3],[1,2])
print(result)