# banque.py
class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        self._titulaire = titulaire
        self.__solde = solde_initial
        self._operations = []

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            self._operations.append(f"Dépôt : +{montant} €")
        else:
            print("Montant invalide.")

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            self._operations.append(f"Retrait : -{montant} €")
        else:
            print("Fonds insuffisants ou montant invalide.")

    @property
    def solde(self):
        return self.__solde

    def __str__(self):
        return f"Titulaire : {self._titulaire}, Solde : {self.solde} €"

    def historique(self):
        return "\n".join(self._operations)


class CompteEpargne(CompteBancaire):
    def __init__(self, titulaire, solde_initial=0, taux=0.02):
        super().__init__(titulaire, solde_initial)
        self._taux = taux

    def calculer_interet(self):
        interet = self.solde * self._taux
        self.deposer(interet)
        self._operations.append(f"Intérêt ajouté : +{interet} €")
