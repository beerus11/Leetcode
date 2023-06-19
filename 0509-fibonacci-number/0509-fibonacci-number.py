class Solution:
    def fib(self, n: int) -> int:
        @lru_cache(None)
        def f(x):
            if x<=1:
                return x
            return f(x-1)+f(x-2)
        return f(n)
        