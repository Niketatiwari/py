#WHILE LOOP
x=1
while x<5:
   print('run')
   x+=1
print('stop')

#complex program
n=10
sum=0 #initialize sum and counter
i=1
while i<=n:
    sum = sum+i
    i=i+1  #updated counter
print('thr sum is', sum)  #print the sum

#CONTINUE LOOP
#example 1 with for loop
x = [1,2,3,4,0,5,0,6,0,7,9,0]
for i in x:
    if i==0:
        continue
    print(i)

#example 2 with while loop
i = 1
while i<=5:
    data = input('enter data')
    if len(data) == 0:
        continue
    print(f'u entered a value of size {len(data)}' )
    i +=1

    #BREAK LOOP
    #example 1 with while loop
    while True:
      price = int(input('enter price of item: '))
    if price < 0:
          break
    print(f'u entered {price}) amount')

x = [1,2,3,4,5,6,7,8,78,87]
for i in x:
    if i<0:
        break
    print(i)
        
