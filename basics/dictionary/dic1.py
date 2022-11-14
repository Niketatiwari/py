#dictionary is an collection of items
my_dict = {1: 'apple', 2: 'ball'}
print(my_dict)

val = ['rajendra singh', 30, 10, 'accounts', 'staff officer', 600000, 7,]
val_dict = {
    'employee' : 'rajendra singh', 'age' : 30,
    'experience' : 10, 'dept' : 'accounts', 
    'designation' : 'staff officer', 'salary' : 600000,
    'team_size' : 7
}
print(val_dict)

#retreival a dict
ans = val_dict['designation'] #key in square brackets
print(ans)
print(val_dict['salary'])   #correct
print(val_dict['experience'])  #incorrect

#adding a data inside dict
val_dict['company'] = 'Acme.inc'
print(val_dict)

from pprint import pp
pp(val_dict)