class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        
        return self.merge(intervals)
    
    def merge(self, intervals: List[List[int]]):
        
        merge = [intervals[0]]
        print(merge)
        for interval in intervals:            
            if merge[-1][1]>=interval[0]:
                merge[-1][1] = max(merge[-1][1], interval[1])
            else:
                merge.append(interval)
        return merge
##HARD