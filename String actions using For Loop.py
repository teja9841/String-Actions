#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 Write a Python program to convert a string to lower case


# In[1]:


x=input()
print(x.lower())


# In[2]:


#2 Write a python program to convert only odd index charecters to lower case


# In[74]:


x=input()
a=""
for letters in range(0,len(x)):
    if  letters%2!=0:
        a=a+x[letters].lower()
    else:
        a=a+x[letters]
print(a)


# In[4]:


#3 Write a python program to convert only even index charecters to lower case


# In[1]:


a=input()
b=""
for idx in range(0,len(a)):
    if idx%2==0:
        b+=a[idx].lower()
    else:
        b+=a[idx]
print(b)


# In[1]:


#4 Write a python program to convert only odd indexed characters to upper case


# In[2]:


c=input()
new=""
for idx in range(0,len(c)):
    if idx%2!=0:
        new+=c[idx].upper()
    else:
        new+=c[idx]
print(new)


# In[3]:


# Write a python program to convert only even indexed characters to upper case


# In[4]:


a=input()
evn=""
for l in range(0,len(a)):
    if l%2==0:
        evn+=a[l].upper()
    else:
        evn+=a[l]
print(evn)


# In[1]:


#Write a python program where you have different variable which contains your name ,sex,age, phone no ,fathers name and mothers name.And by using this variable create avariable named bio-data where you will use all this variable


# In[4]:


n=input("Name : ")
s=input("Sex : ")
a=int(input("Age : "))
p=int(input("Phno : "))
f=input("Father Name : ")
m=input("Mother Name : ")
bio_data="My Name is {} and I am {} years old {}. And My phone number is {}\nMy Father and my Mother name is {} and {}".format(n,a,s,p,f,m)
print(bio_data)


# In[5]:


# Write a python program to count how many times “@” occurred 


# In[6]:


n=input()
n.count("@")


# In[7]:


# Write a python program to get only names from the string


# In[70]:


a=input()
b=a.split(",")
m1=b[0]
m2=b[1]
m3=b[2]
M1=m1.index("@")
M2=m2.index("@")
M3=m3.index("@")
n1=m1[0:M1]
n2=m2[0:M2]
n3=m3[0:M3]
print("{} , {} , {}".format(n1,n2,n3))


# In[71]:


# Given a string of odd length greater that 9, return a new string made of the middle three characters of a given String


# In[84]:


name=input()
size=int(len(name)/2)
name[size-1:size+2]


# In[85]:


# Write a python program to insert a 2 string in the middle of 1 string


# In[3]:


name1=input()
name2=input()
size=int(len(name1)/2)
name1[size-1]+name2+name1[size:]


# In[4]:


# Write a program to remove vowels from the entire alphabets 


# In[6]:


vowels=["a","e","i","o","u","A","E","I","O","U"]
name=input()
a=""
for i in name:
    if i not in vowels:
        a+=i
print(a)

