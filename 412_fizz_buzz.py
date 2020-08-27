class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        fizzBuzzArr = []
        for i in range(1, n+1):
            if i % 15 == 0:
                fizzBuzzArr.append('FizzBuzz')
            elif i % 5 == 0:
                fizzBuzzArr.append('Buzz')
            elif i % 3 == 0:
                fizzBuzzArr.append('Fizz')
            else: 
                fizzBuzzArr.append(str(i))
        
        return fizzBuzzArr