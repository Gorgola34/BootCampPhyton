# Ejercicio secuancia fibonacci con Phyton
a=0
b=1
n=5000
print(a)
print(b)

while(b<n):
 sum=a+b
 if(sum >n):
  break
 a=b
 b=sum
 print(b)

print("Fin de la secuancia Fibonacci")