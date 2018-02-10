import math #Libreria de funciones matematicas
import os   #Libreria de funciones del sistema
 
os.system('clear') #Funcion miembro para limpiar pantalla de la consola
 
a = float(raw_input("Introduzca a = "))
 
b = float(raw_input("Introduzca b = "))
 
c = float(raw_input("Introduzca c = "))
 
print  #por estetica en la salida
 
discriminante = b*b -4*a*c
 
print "discriminante =", discriminante
 
print  #por estetica en la salida
 
if discriminante > 0:
 
    print "2 raices reales distintas"
 
    x1 = (-b + math.sqrt (discriminante))/(2*a) 
 
    x2 = (-b - math.sqrt (discriminante))/(2*a)
 
    print "x1 = ", x1
    print "x2 = ", x2
 
elif discriminante < 0:
 
    print "2 raices complejas conjugadas"
 
    real = -b/(2*a)
 
    imag = math.sqrt (-discriminante)/(2*a)
 
    print "x1 = ", real, " + ", imag,"i"
    print "x2 = ", real, " - ",  imag, "i"
 
elif discriminante == 0:
 
    print "1 sola raiz real"
 
    x = -b/(2*a)
 
    print "x = ", x
