#buenaaas
#Ejercicio 1
'''print('Hola mundo')'''

#Ejercicio 2
'''Hello=('Hola Mundo')
print(Hello)'''

#Ejercicio 3
'''print('¿Como te llamas?')
nombre=input() 
print('Es un placer conocerte, ' + nombre + '.')'''

#Ejercicio 4
'''print(((3+2)/(2*5))**2)'''

#Ejercicio 5
'''print('¿Cuantas horas trabajas?')
hora=float(input())
print('¿Cuanto te pagan por hora?')
pago=float(input())
print(hora*pago) '''

#Ejercicio 6
'''print('Ingrese un numero')
n=int(input())
print(((n*(n+1))/2))'''

#Ejercicio 7
'''print('¿Cuantas pesas? (Kg)')
peso=float(input())
print('¿Cuanto mides (m)?')
estatura=float(input())
n=(peso/estatura)**2
m= round(n,2)
print('Tu indice de masa corporal es', m)'''

#Ejercicio 8 
'''print('Ingrese un numero')
n=int(input())
print('Ingrese otro numero')
m=int(input())
mns= n/m
mn= round(mns, 2)
r= (n%m)
c=round((n//m))
print('el resultado de la division es', mn, 'el residuo es', r, 'y el cociente es', c)'''

#Ejercicio 9
'''print('Ingrese la cantidad que desea invertir')
c=float(input())
print('Ingrese el interes anual')
i=float(input())
print('Ingrese el numero de años')
a=float(input())
cap=(c*((i/100)**a))
print('El capital obtenido por la inversion es', cap)'''

#Ejercicio 10
'''print('Ingrese la cantidad de payasos vendidos en el ultimo pedido')
pc=int(input())
print('Ingrese la cantidad de muñecas vendidas en el ultimo pedido')
mc=int(input())
p= 112
m= 75
pcp= pc*p
mcm= mc*m
print('El peso total del pedido es', (mcm+pcp), 'gramos')'''

#Ejercicio 11
'''print('Ingrese un numero')
n=int(input())
m=(((n*(n+1))/2))
if m>20: print(m, 'Es un gran numero')
else: print('La suma de todos los enteros desde 1 hasta', n, 'es', m )'''

#Ejercicio 12
'''print('Ingrese un numero')
n=int(input())
print('Ingrese otro numero')
m=int(input())
mns= n/m
mn= round(mns, 2)
r= (n%m)
c=round((n//m))
print('el resultado de la division es', mn, 'el residuo es', r, 'y el cociente es', c)
if c<1: print('El divisor es mayor al dividendo')
else if c>1: print('El divisor es menor que el dividendo')
else if c==1: print('El divisor y el dividendo son iguales')''' 


#Ejercicio 13
'''print('Ingrese la cantidad que desea invertir')
c=float(input())
print('Ingrese el interes anual')
i=float(input())
print('Ingrese el numero de años')
a=float(input())
cap=(c*((i/100)**a))
print("el valor del capital es", cap)
if cap<100000: print ("La inversion de", c, "tiene baja rentabilidad")
if cap>100000 and cap<1000000: print("La inversion de", c, "tiene una rentabilidad moderada")
if cap>1000000: print("La inversion de", c, "es una buena inversion")'''


#Ejercicio 14
print('Ingrese la cantidad de payasos vendidos en el ultimo pedido')
pc=int(input())
print('Ingrese la cantidad de muñecas vendidas en el ultimo pedido')
mc=int(input())
p= 112
m= 75
t= "si" 
pcp= pc*p
mcm= mc*m
mmpp= mcm+pcp
if mmpp>3000000: 
  print("¿Desea enviarlo?")
  r=input()
  if r==t: 
    print ("Contenedor enviado")
  else: print("Contenedor no enviado")
else: print('El peso total del pedido es', (mmpp/1000), 'kilos')
