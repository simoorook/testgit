#!/usr/bin/env python
# coding: utf-8

# In[ ]:


counter=[0,0,0,0,0,0]


# In[ ]:


import random


# In[ ]:


i=int(1)
while i<=100:
    v=random.randint(0,5)
    if v==0:
        counter[0]=counter[0]+1
    elif v==1:
        counter[1]=counter[1]+1
    elif v==2:
        counter[2]=counter[2]+1
    elif v==3:
        counter[3]=counter[3]+1
    elif v==4:
        counter[4]=counter[4]+1
    else:
        counter[5]=counter[5]+1
    i=i+1;


# In[ ]:


print("주사위가1인경우:",counter[0])
print("주사위가2인경우:",counter[1])
print("주사위가3인경우:",counter[2])
print("주사위가4인경우:",counter[3])
print("주사위가5인경우:",counter[4])
print("주사위가6인경우:",counter[5])


# In[ ]:


domains={"kr":"대한민국","sk":"슬로바키아","no":"노르웨이","us":"미국","jp":"일본","hu":"헝가리","ge":"독일"}


# In[ ]:


for k,v in domains.items():
    print(k,": ",v)


# In[ ]:


n1=int(input("숫자1 입력:"))
n2=int(input("숫자2 입력:"))


# In[ ]:


print("n1+n2=",n1+n2)
print("n1-n2=",n1-n2)
print("n1*n2=",n1*n2)
print("n1/n2=",n1/n2)
print("n1//n2=",n1//n2)
print("n1%n2=",n1%n2)


# In[ ]:


from string import ascii_lowercase,ascii_uppercase
alphabet=list(ascii_lowercase)+list(ascii_uppercase)
print(alphabet)

infile=open("d:\\학교\\test01.txt","r")
lines=infile.read()
str=list(lines)
print(str)
count=0
c=0
ca=list
for i in str:
    char='a'
    count=count+i.count(char)
    ca[c]=count
    char=ord(char)+1
    count=0
    if char==ord('z')+1:
        char='A'
    elif char=='Z':
        break
print(ca)
    
infile.close()


# In[ ]:


infile=open("d:\\학교\\test01.txt","r")
lines=infile.read()
str=list(lines)
print(str)
char=65

while char<123:
    count=0
    for i in str:
        count=count+i.count(chr(char))
    dic={chr(char):count}
    char=chr(char+1)
    print(dic)
    char=ord(char)
    if char==90:
        char=97


infile.close()


# In[ ]:


infile=open("d:\\학교\\test02.txt","r")
outfile=open("d:\\학교\\test03.txt","w")
n=[0]
i=0
for line in infile:
    line = line.rstrip()
    n.append(float(line))
    i=i+1
    print(line)
    
print(n)
s=sum(n)
print(s)
p=n.index(16.6)
print(n.index(16.6))
avg=s/p
print(avg)
outfile.write("합: ")
outfile.write(str(s))
outfile.write("\n평균:")
outfile.write(str(avg))
infile.close()
outfile.close()


# In[ ]:


class circle:
    def __init__(self):
        self.radius=input('반지름:')
    def calcP(self):
        print(float(self.radius)*3.141592*2)
    def calcA(self):
        print(float(self.radius)**2*3.141592)
c=circle()
c.calcP()
c.calcA()


# In[1]:


import turtle
class myturtle(turtle.Turtle):
    def drawSquare(self):
        self.shape("turtle")
        self.right(90)
        self.forward(100)
        self.right(90)
        self.forward(100)
        self.right(90)
        self.forward(100)
        self.right(90)
        self.forward(100)
t=myturtle()
t.drawSquare()


# In[ ]:





# In[ ]:




