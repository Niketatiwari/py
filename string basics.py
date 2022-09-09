my_string = 'Hello'
print(my_string)
my_string = "hello"
print(my_string)
my_string = '''hello'''
print(my_string)
my_string = """heyyy!, i am annu
and i am from lucknow"""
print(my_string)

#index concept
a='ekanshi'
print(a)
print(a[0])
print(a[5])
print(a[-3])

#slicing 
name='ayush kumar tiwari'
for i,c in enumerate(name):
    print(i,c)
print(name[6 :-6 ])
print(name[-6: ])
print(name[ :5])

#reverse the string
print(name[ ::-1])
print(name[ :6][::-1])

#every even index char.
print(name[::2]) 

#every odd index char.
print(name[1::2])

x = chr(65) #convert integer to string char
print(x)
x = chr(2365) 
print(x)
for i in range(15000,20000):
    print(i, chr(i))

y = ord('A') #CONVERT TO CHAR IN INTEGER
print(y)
y = ord('a') 
print(y)
y = ord('{') 
print(y)
y = ord('🤧') 
print(y)

#concatenation (joinig two or more string)
a ='apple'
b ='shake'
ab = a+b
print(ab)

w1 ='this'
w2 ='is'
w3 ='amazing'
msg = w1+w2+w3
print(msg)
msg = w1+' '+w2+' '+w3
print(msg)

#duplication
a = 'hii'
print(a*2)
print('$'* 10)
print('-'* 100)










