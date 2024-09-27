class MyCalendarTwo:

    def __init__(self):
        self.events = []
        self.overlaps = []
        
    def book(self, start: int, end: int) -> bool:
        for o_start, o_end in self.overlaps:
            if start < o_end and end > o_start:
                return False
        for e_start, e_end in self.events:
            if start < e_end and end > e_start:
                self.overlaps.append((max(start, e_start), min(end, e_end)))
        self.events.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)