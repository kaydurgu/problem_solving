class Solution:
    def scheduleCourse(self, courses: 'List[List[int]]') -> 'int':
        lst = list(map(lambda x: [x[1], x[0]], courses))
        lst.sort()
        
        from queue import PriorityQueue
        
        pq = PriorityQueue()
        
        #print(lst)
        
        ans = 0
        cnt = 0
        for i in range(len(lst)):
            d, t = lst[i]
            if cnt + t <= d:
                ans += 1
                cnt += t
                pq.put(-t)
            
            elif pq.qsize() > 0 and -pq.queue[0] > t:
                cnt = cnt + pq.get() + t
                pq.put(-t)
                
                
            #print('cnt', cnt)
        
        return ans