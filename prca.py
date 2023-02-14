import numpy as np

####INPUT

j=4 
i=5
t=10

x_var = np.zeros((j,i,t))
b_var = np.zeros((j,i,t))

#주어진 x_var
for t in range(10):
    x_var[0,0,t]=1
x_var[1,1,0]=1
x_var[1,1,6]=1
x_var[2,1,0]=1
x_var[1,2,2]=1
x_var[1,2,4]=1
x_var[1,2,8]=1
x_var[2,2,2]=1
x_var[2,2,8]=1
for i in range(4):
    x_var[2,3,i+4]=1
x_var[3,4,5]=1
x_var[3,4,8]=1

#주어진 b_var
b_var[0,0,0]=36
b_var[0,0,1]=100
b_var[0,0,2]=0
b_var[0,0,3]=0
b_var[0,0,4]=0
b_var[0,0,5]=0
b_var[0,0,6]=0
b_var[0,0,7]=0
b_var[0,0,8]=0
b_var[0,0,9]=0
b_var[1,1,0]=80
b_var[1,1,6]=74
b_var[2,1,0]=50
b_var[1,2,2]=80
b_var[1,2,4]=80
b_var[1,2,8]=80
b_var[2,2,2]=50
b_var[2,2,8]=50
b_var[2,3,4]=50
b_var[2,3,5]=47
b_var[2,3,6]=50
b_var[2,3,7]=16.25
b_var[3,4,5]=50
b_var[3,4,8]=113.75


'''print(x_var)
print("--------------------------")
print(b_var)
'''

#데이터 따오는 법

abclist=[]
x=np.where(x_var==1)

#print(x)

for n in x:
    abclist.append(n)

a= abclist[0]
b= abclist[1]
c= abclist[2]

print(a)
print(b)
print(c)