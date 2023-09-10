def factoriel(n):
	if n==0:
		return 1
	else:
		return n * factoriel(n-1)

nombre = 3
resultat = factoriel(nombre)
print(f"Le factoriel de {nombre} is {resultat}.")
