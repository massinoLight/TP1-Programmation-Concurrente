#!/usr/bin/python3.8

# -*-coding:Utf-8 -*
import os # On importe le module os
from math import sqrt
print("Bonjour! le prog dit donne le nombre de triangles possible avec un cote de valeur entiere  ")

a= int(input("donnez le premier cote "))

b= int(input("donnez le second cote "))

s=a+b+1
c=0
 
 
for i in range(min(a,b),s) :
      p = (a + b + i) / 2   
      if p > b and p > a:                     
         aire = sqrt (p * (p - a) * (p - b) * (p - i))
         perimetre=a+b+i   
         if perimetre == aire:
            c=i
            break
       

if c==0:
    print("pas de triangle special avec les deux valeurs precedentes")


else :

    print(c," est une valeur possible pour le cote c afin d obtenir un triangle special")        

        

	
    



    






