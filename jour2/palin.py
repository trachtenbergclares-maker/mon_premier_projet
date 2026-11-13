def est_palindrome(texte):
	texte_propre = texte.lower().replace(" ", "")
	texte_inverse = texte_propre[::-1]

	if texte_propre == texte_inverse:
		return True
	else:
		return False
mot = input("Entrer un mot : ")
print(est_palindrome(mot))

