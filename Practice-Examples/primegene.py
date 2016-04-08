# Program-3 : primegene.py
import itertools
import sys

def gen_primes(n):


     if(n>1):

       count=0

       for num in range(1,n+1):

         if(n%num ==0):

           count=count+1

       if(count==2):


         yield n


if __name__ == '__main__':

    number=int(sys.argv[1])

    number=number+1

    pp=[]

    for j in range(number):


      k=list(gen_primes(j))

      if(k !=[]):

        pp.append(k)

    print(pp)
