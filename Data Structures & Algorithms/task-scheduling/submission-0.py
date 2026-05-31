class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        total=0
        counter = {}
        for x in tasks:
            counter[ord(x) - ord('a')] = counter.get(ord(x) - ord('a'),0) + 1
        arr = [-cnt for cnt in counter.values()]
        heapq.heapify(arr) 
        q = deque()

        while q or arr:
            total+=1 
            if arr:
                cnt = 1 + heapq.heappop(arr)
                if cnt:
                    print(total)
                    print(n)
                    q.append([cnt,total+n])
            
            if q and q[0][1] ==total:
                pp = q.popleft()
                heapq.heappush(arr,pp[0])
        return total







        return 1