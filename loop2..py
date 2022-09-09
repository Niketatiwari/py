#for i in range (100):
 #   print('hi',i)

  #  for i in range (1,20):
   #     print('hello',i)
#for i in range (1,15,2):
 #   print('heyyyyyy!',i)

#for i in range (100):
 #   print(i,end=' ')

#for i in range (10, 21):
 #    print(i,end='x')


#for i in range (1,11,2):
 #   print(i,end='0')

 #reverse loop
#for i in range (100,0,-1):
 #   print(i, end=' ')

#print('=>')
# data = ['milkybar','perk','dairymilk','5star','kitkat']
# for i,d in enumerate(data):
#     print(i,d)


# data = ['milkybar','perk','dairymilk','5star','kitkat']
# for i,d in enumerate(data):
#     print(i)

names=['cakes','kurkure','fruti','chocolate','golgappa']
prices=[500, 20, 45, 80, 20]
for n,p in zip(names,prices):
    print(f'{n}=> Rs.{p}')