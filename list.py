#EXAMPLE 1

movies = ['RRR','KS','DDLJ','sanam re',
'shiddat','shershaah','heropanti','kkhh','major']
print(len(movies))

movies.sort()
print(movies)

movies.sort()
print(movies)

movies.reverse()
print(movies)

print('first movie',movies[0])
print('second movie',movies[-1])
print('first 3 movie',movies[ :3])
print('all movies expect first 3',movies[3:])
print('movies with even indexes',movies[::2])

#EXAMPLE 2

books = ['rich daddy','harry potter','beloved',
'the key of success']
books.append('3 mistake of my life')
books.append('u can win')
print(books)

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

books[1] = 'story of young girl'
books[-1] ='broken but beautifully'

print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

books.insert(3, '2 States')
books.insert(5 , 'harry potter')
print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

books.remove('rich daddy')
books.remove('beloved')
print('idx\t| book')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

a = ['apple', 'banana','mango']
b = ['walnut','cashew']
a.extend(b)
print(a)
print(b)

#EXAMPLE 3

x = [1,2,3,3,3,1,1,1,1,1,2,2,3,2,2,3,2,3,2]
x_one = x.count(1)
x_two = x.count(2)
x_three = x.count(3)
x_four = x.count(4)
print('1 occurred', x_one, 'times')
print('2 occurred', x_two, 'times')
print('3 occurred', x_three, 'times')
print('4 occurred', x_four, 'times')

y = [23,12,11,15,16]
z = [22,21,14]
print('x adding y')
x.extend(y)
print(x)
print('x adding z')
x.extend(z)
print(x)

xyz =  x+y+z
print(xyz)

a = ['apple', 'banana','mango']
b = a.pop(2) #pop can remove value from an index
print(a)
print(b)
lv = a.pop() #pop remove value from an index
print(a)
print(lv)





