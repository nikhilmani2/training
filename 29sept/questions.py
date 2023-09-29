import matplotlib.pyplot as plt
import numpy as np

#problem1
xpoints=np.array([1,2,3,4,5])
ypoints=np.array([3,3,3,3,3])
plt.plot(xpoints,ypoints)
plt.show()

#problem2
xpoints=np.array([1,2,3,4,5])
ypoints=np.array([3,3,3,3,3])
plt.plot(ypoints,xpoints)
plt.show()

#problem3
x=np.array(['A','B','C','D'])
y=np.array([5,6,3,1])
plt.bar(x,y,color='black',width=0.5)
for i,v in enumerate(y):
    plt.text(i,(v+0.1),str(v))
plt.show()

#problem4
xpoints=np.array([10,20,30,40,50])
ypoints=np.array([30,60,90,120,150])
plt.plot(xpoints,ypoints)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Draw a line')
plt.show()


#problem5
xpoints=[]
ypoints=[]
with open ("test.txt","r") as file:
    for line in file:
        x,y=map(float,line.strip().split(" "))
        xpoints.append(x)
        ypoints.append(y)
plt.plot(xpoints,ypoints)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Sample graph!')
plt.show()