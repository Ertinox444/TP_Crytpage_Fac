from random import randint
import string
from typing import Dict
import json
import random
import time
import os

dcrypt = {}
duncrypt = {}
lnb = []
comp = 0
mot = ""
motdec = ""
b=3



#définition des caractères utilisables

def enleve(nb:int):
    lnb.remove(lnb[nb])

for i in range(0,127):
    lnb.append(chr(i))
for i in range(160,256):
    lnb.append(chr(i))

#création du dictionnaire de cryptage

for x in range(0, 127):
    nb = randint(0,len(lnb) - 1)
    dcrypt[chr(x)] = lnb[nb]
    enleve(nb)
for i  in range(160,256):
    nb = randint(0, len(lnb) - 1)
    dcrypt[chr(i)] = lnb[nb]
    enleve(nb)

#création du dictionnaire de décryptage

duncrypt = {v: k for k, v in dcrypt.items()}


with open('dictcrypter.json', 'w+') as file:
   json.dump(dcrypt, file)
with open('dictcrypter.json', 'r') as file:
    mydict = json.load(file)
with open('dictuncrypt.json','w+') as file:
    json.dump(duncrypt,file)
with open('dictuncrypt.json', 'r') as file:
    dictiouncrypt = json.load(file)

#Menu de séléction

print("-------------------------""\n""Bienvenue dans ce programme de cryptage par dictionnaire""\n""-------------------------")
print("Base de cryptage :""\n""-   -   -   -   -   -   -" "\n""1.Ficier prédéfinis""\n""2.Fichier perso""\n""3.Fichier importé""\n""-------------------------")

select = int(input("Séléctionner la base de cryptage (1,2 ou 3) : "))
print("-------------------------")    

#via fichier prédéfini 
if select == 1:
    with open("texte_predefini.txt","r")as fic:
      texte = fic.readlines()
    for i in texte:
        for x in i:
            mot = mot + dcrypt[x]

#via fichier que l'on écrit sois-même dans la console
if select == 2:
     with open("fichier_modifer.txt", "w+") as fic:
       fic.write(input("Rédiger le texte que vous souhaiter crypter : ""\n""\n"))
     with open("fichier_modifier.txt", "r") as fic:
       texte = fic
       for pos in texte:
          for x in pos:
            mot = mot + dcrypt[x]

#via fichier importée dans le dossier
if select == 3:
    print("Mettez le fichier souhaiter dans le dossier_fichier_perso""\n""-------------------------")
    os.chdir('Dossier_fichier_perso')
    nom_fichier = str(input("Séléctionnez le fichier souhaité :"))
    with open(nom_fichier,"r", encoding = 'UTF-8') as fic:
        texte = fic.readlines()
        for pos in texte:
          for x in pos:
            mot = mot + dcrypt[x]

#export du cryptage dans un fichier
if select == 1:
    with open("fichier_crypter_fichier_prédéfini.txt","w+",encoding='UTF-8')as f:
        f.write(mot)
if select==2:
    with open("fichier_crypter_fichier_modifier.txt","w+",encoding='UTF-8')as f:
        f.write(mot)
if select == 3:
    with open("fichier_crypter"+"_"+nom_fichier,"w+",encoding='UTF-8')as f:
        f.write(mot)

print("-------------------------""\n""Votre fichier est donc crypté, le voici""\n""-------------------------""\n"+ mot+"\n""-------------------------")


#possibilité de décryptage pour vérification

rep = str(input("Voulez vous le décrypter (oui ou non) ? : "))

print("-------------------------")

if rep == "non":

    while(b>=0):
        print(b,"...")
        time.sleep(0.5) 
        b -=1
    print("-------------------------")
    print("EXPLOSION !")
    print("-------------------------")
    time.sleep(1)
    print("C'est une boutade")
    print("-------------------------")
 
if rep == "oui":

     for i in mot:
        for x in i:
            motdec = motdec + duncrypt[x]
     print(motdec)
     print("-------------------------")

     print("Et voilà ! Votre fichier avait donc été crypté avec succès !")
     print("-------------------------")

print("merci d'avoir utiliser notre programme")
print("^ ^")

