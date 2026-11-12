'''Calculatrice 1.0'''
def addition(nombre1,nombre2):
	return nombre1 + nombre2

def soustraction(nombre1,nombre2):
	return nombre1 - nombre2

def multiplication(nombre1,nombre2):
	return nombre1 * nombre2

def division(nombre1,nombre2):
	if nombre2 == 0:
		return None
	else:
		return nombre1 / nombre2

def demander_nombre(message):
	while True:
		try:
		     return float(input(message))
		except ValueError:
		     print("C'est pas un nombre, reessaie!")

def main():
	print("==== CALCULATRICE 1.0 ====")
	print("Operation pour deux nombres par : (+),(-),(×) et (÷).")
	print("Tape 'q' pour quiter.\n")
	while True:
		op = input("Choisir une opreation (+) (-) (*) (/) ou q:").strip()
		if op == "q":
			print("Mercie : Abiento!")
			break
		if op not in("+","-","*","/"):
			print("Operation invalide !")
			continue
		nombre1 = demander_nombre("Etrer le premier nombre:")
		nombre2 = demander_nombre("Etrer la deuxieme nombre:")

		if op == "+":
			resultat = addition(nombre1,nombre2)
		elif op == "-":
			resultat = soustraction(nombre1,nombre2)
		elif op == "*":
			resultat = multiplication(nombre1,nombre2)
		else:
			resultat = division(nombre1,nombre2)
		if resultat is None:
			print("Erreur : division par zero!")
		else:
			print(f"{nombre1} {op} {nombre2} = {resultat:.2f}")

if __name__ == "__main__" :
	main()

