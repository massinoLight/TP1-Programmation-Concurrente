#!/usr/bin/python3.8
# calcul de l'aire d'un triangle avec la formule de Héron
2
#Calcul de l'aire 

#Fonction racine :
from math import sqrt

print("Bonjour! le prog definie si 3 valeurs representent un trangle ou pas ")

a= int(input("donnez le premier cote "))

b= int(input("donnez le second cote "))

c= int(input("donnez le dernier cote "))
	
if a>0 and b>0 and c>0 and a<(a+b+c)/2 and b<(a+b+c)/2 and c<(a+b+c)/2 :
    print("oui les points peuvent representer un triangle")


else :

    print("non les points ne peuvent pas representer un triangle")






