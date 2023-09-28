def fahrenheit(celsius):
    return (9/5)*celsius +32
temps=[0,22.5,40,100]
F_temps = map(fahrenheit,temps)

#Show
list(F_temps)

from functools import reduce
lst=[47,11,42,13]
reduce(lambda x,y: x+y,lst)

#from IPython.display import Image
#Image('http://www.python-course.eu/images/redice_diagram.png')

#Find the maximum of a sequence (This already exists as max())
max_find=lambda a,b:a if (a>b) else b

#Find max
reduce(max_find,lst)

#First let's make a function
def even_check(num):
    if num%2==0:
        return True
    
lst=range(20)
list(filter(even_check,lst))
list(filter(lambda x: x%2==0,lst))    
