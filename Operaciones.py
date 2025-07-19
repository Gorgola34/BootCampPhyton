import numbers
a=40
b=20
Listanumeros=[0,0]
Listanumeros[0]=a+b
Listanumeros[1]=a-b

print(Listanumeros)

if isinstance(a,numbers.Number):
    print("a es un numero")
else :
    print("a no es un numero")

    