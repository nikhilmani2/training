#problem1

def gensquares(N):
    for i in range(N):
        yield i**2
for x in gensquares(10):
    print(x)
    
print("-------------------------")  
          
#problem2

import random
#random.randint(1,10)
def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low,high)  
        
for num in rand_num(1,10,12):
    print(num)                
    
print("-------------------------")  

#problem3
s='hello'
for letter in iter(s):
    print (letter)
    
print("-------------------------")  


#problem4

def fib(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b =b,a+b
for num in fib(15):
    print(num)            
    
print("-------------------------")  
    