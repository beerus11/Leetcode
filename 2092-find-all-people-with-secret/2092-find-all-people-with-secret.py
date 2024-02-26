class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x:x[2])
        time_arr = [inf]*(n+1)
        g = defaultdict(list)
        for a,b,t in meetings:
            g[a].append((b,t))
            g[b].append((a,t))
            
        time_arr[0]=0
        time_arr[firstPerson]=0
        
        st = [(0,0),(firstPerson,0)]
        while st:
            p,time = st.pop()
            for next_person,next_time in g[p]:
                if next_time>=time and time_arr[next_person]>next_time:
                    time_arr[next_person]=next_time
                    st.append((next_person,next_time))
        return [k for k,v in enumerate(time_arr) if v!=inf]
            
        