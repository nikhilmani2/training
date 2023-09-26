def dectooct(number):
    return oct(number)

def reversenum(number):
    return str(number)[::-1]
def fibonactilln(number):
    series=[]
    for i in range(number):
        series.append(fibonacci(i))
    return series

def fibonacci(number):
    if number<=0:
        return 0
    elif number==1:
        return 1
    else:
        return fibonacci(number-1)+fibonacci(number-2)
    
number=int(input("Enter the number: "))
print("Octal Representation: "+ str(dectooct(number)))
print("Reverse: "+str(reversenum(number)))
print("Fibonacci Series: "+ str(fibonactilln(number)))
print(str(number)+"th value from the fibonacci sequence: "+str((fibonactilln(number))[number-1]))
    