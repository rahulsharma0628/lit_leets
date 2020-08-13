from itertools import combinations
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        
        self.combinations = list(combinations(characters, combinationLength))
        # print(list(self.combinations))
        self.stringCombs = [''.join(x) for x in list(self.combinations)]
        # self.stringCombs.sort()
        # print(self.stringCombs)
        
        self.count = 0

    def next(self) -> str:
        if self.hasNext():
            self.count += 1
            return self.stringCombs[self.count-1]
        return 
        
    def hasNext(self) -> bool:
        if self.count<len(self.stringCombs):
            return True
        return False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()