def Multiplication(a,b):
	return a *b
	
def Table_Multiplication(n) :
 
	res = 0
	for i in range(0,10):
	
		res = Multiplication(n, i)
		print(f"{i} x {n} = {res}")
	
		
	
