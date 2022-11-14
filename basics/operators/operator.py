#Arithmetic operator
a = 11
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b) #division
print(a // b) #rounded off (quotient)
print(a % b) #(remainder)
print(a ** b) # exponentiation

#Assignment operator
print('ASSIGNMENT OPERATOR')
x = 15  #Simple assignment
y = x + 15
z = x + y
a = x**2 + y**2
print (x,y,z,a)
b = 10
b += 5 # updation assignment
print(b)
b -= 2
print(b)
b *= 3
print(b)
b /= 2
print(b)

#comparison operator
print("COMPARISON OPERATOR")
a =1000
b = 40
print(a == 100)
print(b == 100)
print(5 == 3)
print(a != 20 )
print(a > b)
print(a < b)
print(a <= 400)
print(b >= 65)

#Logical operator
print("LOGICAL OPERATOR")
a = 10
b = 9
c = 11
print (a > b and a > c)
print(a > b and a < c)
print(a > b or a < c)
print(a > b or a > c)
print(a < b and a < c)
print( not a > b ) # not reverse the answer
print( not False)
print(not True)

# in operator
print('IN OPERATOR')
names = ['annu', 'rashi', 'nikki']
print('priya' in names)
print('annu' in names)
print('rashi' in names)
print('supriya' in names)

message = 'once upon a time, there was a ghost' 
print('upon' in message)
print('there' in message)
print('that is' in message)

#is operator
print('is operator')
x = 10
y = 10
z = x
c = 5
d = 10
print(x is y)
print(x is c)
print(x is z)
print(y is z)
print(y is x)
print(c is c)
print(c is d)

x = [1,3,5]
y = [7,8,9]
z = x
print(x is z) #true
print(x is y) #false
print(y is x) #false





