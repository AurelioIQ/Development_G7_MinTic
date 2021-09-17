n=int(input('Digite un numero ',))
"""for i in range (n+1):
   print(i)"""
cont=0
sum=0
for i in range (2,n+1):
   if i%5==0:
      print(i)
      sum=i+sum
      cont=1+cont
print('la suma de los pares es', sum)
print('El numero de pares es  pares es', cont)
