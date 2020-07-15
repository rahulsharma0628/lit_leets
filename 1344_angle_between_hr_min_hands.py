class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        hr_angle = hour*30 + minutes*0.5
        min_angle = minutes*6
        
        return min(abs(hr_angle-min_angle), 360-abs(hr_angle-min_angle))