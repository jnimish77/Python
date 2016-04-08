# Program-2 "primeiter.py",


import sys
import itertools

class PrimeIter:
    def __init__(self):
        self.current = 1

    def __next__(self):
        self.current = self.current + 1
        while 1:
            for i in range(2, self.current):
                if self.current % i == 0:
                    self.current = self.current + 1
                    break 
            else:
                break 
        return self.current

    def __iter__(self):
        return self

if __name__ == '__main__':
    b=[]
    end_number=int(input("enter the number: "))
    
    iterator = PrimeIter()
    
    for x in itertools.islice(iterator, end_number):
        
        b.append(x)
    print(b)
