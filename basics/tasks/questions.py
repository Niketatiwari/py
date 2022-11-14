###1...wap to create a list of 5 names taken from useer and then display 
# each name in reverse.

###2..wap to print a fibonacci series using the concept of list (0,1,1,2,3,5,8,11..)

###3...wap to generate a new list that contains squares of each numbers 
# from existing list  (ex: x= [2.3,4,5] => [4,8,16,25])

###4..WAP to generate a new list from an existing list of numbers that contains only odd numbers

###5.. WAP to generate a new list by adding 2 list element wise

#1 
x =[]
for i in range (5):
     x.append(input("name=> "))
for name in x:
    print(name[::-1])

#2
fib = [0,1]
for i in range(15):
    fib.append(fib[-1] + fib[-2])
print(fib)

#3
x =[1,2,3,4,5,6]
x2 =[]
for num in x:
    x2.append(num ** 2)
print(x)
print(x2)

#4
a =[4,5,6,3,2,6]
xodd = []
for i in a:
    if i % 2 !=0:
        xodd.append(i)
print(xodd)

#-------> list of comprehension
xodd = [i for i in x if i%2!=0]
#-------> list of comprehension

#5
x =[1,2,3,4]
y =[5,6,7,8]
z=[]
for i,j in zip(x,y):
    z.append(i+j)
print(x)
print(y)
print(z)

