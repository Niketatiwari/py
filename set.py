# set is an unordered collection of items
my_set = {1,2,3}
print(my_set)

my_set = set([1,2,3,2])
print(my_set)

my_set = {1,2,[3, 4]} # this will cause error
print(my_set)

#create empty set
a = set()
print(type(a))

#modifying a set 
my_set ={1,2,3}
print(my_set)

my_set.add(4)
print(my_set)

my_set.update([2,3,4,5])
print(my_set)

my_set.update([4,5],{1,6,8})
print(my_set)

my_set.remove(6)
print(my_set)

my_set.discard(4)
print(my_set)

my_set.pop()
print(my_set)

my_set.clear()
print(my_set)




