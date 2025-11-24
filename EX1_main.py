from EX1_banque import CompteBancaire

compte = CompteBancaire("Ali", 1000)
compte.deposer(200)
compte.retirer(150)
print(compte)
print("Solde accessible (lecture) :", compte.solde)

# Test de protection : modification directe interdite
try:
    compte.solde = 500
except AttributeError as e:
    print("Erreur :", e)
