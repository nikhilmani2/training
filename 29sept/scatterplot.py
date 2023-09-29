import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,3,4,5,6,8,6,5,4,3,2,1])
y=np.array([99,87,76,65,54,56,67,78,98,98,99,35,46])
plt.scatter(x,y)
plt.show()

x=np.array([5,6,7,8,7,17,2,4,9,12,9,6])
y=np.array([4,6,7,8,4,12,2,5,7,9,12,1])
plt.scatter(x,y,color='red')

x=np.array([1,2,3,4,5,6,8,6,5,4,3,2,1])
y=np.array([99,87,76,65,54,56,67,78,98,98,99,35,46])
plt.scatter(x,y,color='hotpink')

plt.show()

colors=np.array(['red','green','blue','yellow','orange','black','red','green','blue','yellow','orange','black'])
x=np.array([5,6,7,8,7,17,2,4,9,12,9,6])
y=np.array([4,6,7,8,4,12,2,5,7,9,12,1])
plt.scatter(x,y,c=colors)
plt.show()


colors=np.array([0,10,20,30,40,50,55,60,70,80,90,100])
x=np.array([5,6,7,8,7,17,2,4,9,12,9,6])
y=np.array([4,6,7,8,4,12,2,5,7,9,12,1])
plt.scatter(x,y,c=colors,cmap='viridis')
plt.colorbar()
plt.show()


x=np.array([5,6,7,8,7,17,2,4,9,12,9,6])
y=np.array([4,6,7,8,4,12,2,5,7,9,12,1])
sizes=np.array([10,20,30,40,50,55,200,65,70,75,80,85])
colors=np.array(['red','green','blue','yellow','orange','black','red','green','blue','yellow','orange','black'])
plt.scatter(x,y,s=sizes,c=colors)
plt.show()


x=np.random.randint(100,size=(100))
y=np.random.randint(100,size=(100))
colors=np.random.randint(100,size=(100))
xsizes=10*np.random.randint(100,size=(100))
plt.scatter(x,y,c=colors,s=xsizes,alpha=0.5,cmap='CMRmap')
plt.colorbar()
plt.show()


x=np.array(['A','B','C','D'])
y=np.array([5,6,3,1])
plt.bar(x,y,color='red',width=0.5)
plt.show()

x=np.array(['A','B','C','D'])
y=np.array([5,6,3,1])
plt.barh(x,y,height=0.2)
plt.show()


x=np.random.normal(170,10,250)
plt.hist(x)
plt.show()

y=np.array([0.5,10,20,30,40,50])
x=['z','a','b','c','d','e']
exp=[0,0,0,0,0,0.2]
plt.pie(y,labels=x,startangle=90,explode=exp,shadow=True)
plt.legend(title='Voting Result')
plt.show()




