x=[1,2,3]
y=[4,5,6]
#Zip the lists together
list(zip(x,y))

x=[1,2,3]
y=[4,5,6,7,8]

#Zip the lists together
list(zip(x,y))

d1={'a':1,'b':2}
d2={'c':4,'d':5}
list(zip(d1,d2))
list(zip(d2,d1.values()))

def switcharoo(d1,d2):
    dout={}
    for d1key,d2val in zip(d1,d2.values()):
        dout[d1key]=d2val
    return dout

lst=['a','b','c']
for number,item in enumerate(lst):
    print(str(number),item)
    
for count,item in enumerate(lst):
    if count >=2:
        break 
    else:
        print(item)
        
months=['March','April','May','June']
list(enumerate(months,start=3))
lst=[True,True,False,True]
all(lst)
any(lst)
complex(2,3)
complex(10,1)
complex('12+2j')



               