    class Voiture(object):
        def __init__(self, marque, prix, couleur):
    	self.marque = marque
    	self.prix = prix
    	self.couleur = couleur
     
    super_voiture = Voiture("Lamborghini", 150000, "rouge")
    print(super_voiture.marque)
    print(super_voiture.prix)
    print(super_voiture.couleur)
