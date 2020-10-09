#!/usr/bin/python3.8

# -*-coding:Utf-8 -*
import os # On importe le module os
print("Bonjour! le prog dit si un triangle est isocele ou pas")

a= int(input("donnez le premier cote "))

b= int(input("donnez le second cote "))

c= int(input("donnez le dernier cote "))




if a==b and c <= a+b:
    print("oui votre triangle est isocele")


else :

    print("non il n'est pas isocele")






