#Generator function for the cube of numbers(power of 3)
def gencubes(n):
    for num in range(n):
        yield num**3

for x in gencubes(10):
    print(x)
            
def genfibon(n):
    """"1 1 2 3 5 8
        a b
          a b
            a b
              a b
    Generate a fibonnaci sequence up to n
    """
    a=1
    b=1
    for i in range(n):
        yield a
        a,b=b,a+b 
       
for num in genfibon(10):
    print(num)
            
def fibon(n):
    a=1
    b=1
    output=[]
    for i in range(n):
        output.append(a)
        a,b=b,a+b
    return output
print(fibon(10))  

def simple_gen():
    for x in range(3):
        yield x
        
#Assign simple_gen
g=simple_gen()
print(next(g))        
print(next(g))        
print(next(g))        
print(next(g))        

s='hello'
#Iterate over string
for let in s:
    print(let)
next(s)
s_iter=iter(s)
next(s_iter)    
next(s_iter)    
next(s_iter)    
next(s_iter)    
next(s_iter)    

                                         