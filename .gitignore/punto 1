def horner(p, n, x):
	y=p[0]
	for i in range (n):
	        y = x*y + p[i]
	return y


def eval(p,n,x):
	s=0;
	i;
	for i in range (n):
    		s=s+p[i]*pow(x,n-i-1)
	return s

print ("digite el mayor exponente")
maximo = input ()
print ("digite el polinomio")
polinomio = input ()
numero = -1
exponente = int(maximo)
arreglo=[int(maximo)]
j=0
while (j<int(maximo)+1):
	for i in range (len(polinomio)):
		if (polinomio[i] == 'x' and i==0):        
			numero=1
		else:
			if (polinomio[i] == '-' and i==0):
				numero = int(polinomio [i+1])
				numero = numero*-1
			else:
				if (i==0):
					numero = int(polinomio [i])
			if (polinomio[i] == '+' or polinomio[i] == '-'):
				if (polinomio[i] == 'x'):
					numero = 1	
			if (polinomio[i] == '^'):
				if (int(polinomio[i+1]) == exponente-1):
					arreglo [j]=numero
					exponente = exponente-1
					j=j+1
				if (int(polinomio[i+1]) != exponente-1):
					while (int(polinomio[i+1]) != exponente-1):
						arreglo [j] = 0
						exponente = exponente-1
						j=j+1
print ("digite el valor de x")
x = input ()
horner (arreglo, maximo+1, x)
