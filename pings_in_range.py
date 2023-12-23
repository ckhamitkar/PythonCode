from typing import List
def __init__(self):
    self.queue = deque()
    
def ping(self, t: int) -> int:
    self.queue.append(t)
    while self.queue[0] < t - 3000: 
        self.queue.popleft() 
    return len(self.queue)      
        
            
ping([[], [1], [100], [3001], [3002]])