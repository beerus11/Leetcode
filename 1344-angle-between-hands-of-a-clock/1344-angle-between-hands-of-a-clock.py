class Solution:
    def angleClock(self, h: int, m: int) -> float:
        hour_pos = 30*h + 0.5*m
        min_pos = 6*m
        x = abs(hour_pos-min_pos)
        return min(x,360-x)
        