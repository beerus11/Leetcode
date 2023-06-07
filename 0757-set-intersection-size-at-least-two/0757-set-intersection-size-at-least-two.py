class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        size = 0
        prev_start = -1
        prev_end = -1

        for curr_start, curr_end in intervals:
            if prev_start == -1 or prev_end < curr_start:
                size += 2
                prev_start = curr_end-1
                prev_end = curr_end

            elif prev_start < curr_start:
                if prev_end != curr_end:
                    prev_start = prev_end    
                elif prev_end==curr_end :
                    prev_start = curr_end-1
                prev_end = curr_end

                size += 1

        return size
        