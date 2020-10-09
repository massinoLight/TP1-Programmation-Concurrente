#!/usr/bin/python3.8
# calcul de l'aire d'un triangle avec la formule de Héron
2
#Calcul de l'aire 

#Fonction racine :
from math import sqrt

print("Bonjour! le prog calcule l'aire d'un trangle")

a= int(input("donnez le premier cote "))

b= int(input("donnez le second cote "))

c= int(input("donnez le dernier cote "))
	
p = (a + b + c) / 2                        
#p est le demi périmètre du triangle

	
aire = sqrt (p * (p - a) * (p - b) * (p - c))

print ("L'aire de ce triangle est", aire)






