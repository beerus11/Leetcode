class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.winners = []
        self.times = times
        counter = defaultdict(int)
        curwinner,curmax = -1,0
        for p, t in zip(persons, times):
            counter[p] += 1
            if counter[p] >= curmax:
                curwinner = p
                curmax = counter[p]
            self.winners.append(curwinner)

    def q(self, t: int) -> int:
        i = bisect_right(self.times, t)
        return self.winners[i-1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)