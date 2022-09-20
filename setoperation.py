# Union
A ={1,2,3,4,5}
B ={4,5,6,7,8}
print(A|B)

print(A.union(B))

print(B.union(A))

#set intersection
A ={1,2,3,4,5}
B ={4,5,6,7,8}
print(A & B)
print(A.intersection(B))

#set difference
print(B - A)
print(A-B)
print(A.difference(B))

#set symmetric difference
A ={1,2,3,4,5}
B ={4,5,6,7,8}
print(A^B)

print(A.symmetric_difference(B))

