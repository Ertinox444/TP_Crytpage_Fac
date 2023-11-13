import time
import os


b = 3
mot = ""
Liste = []
CryptListe = []
ListeCrypte = []
DecryptListe = []
global texte

def conversion(Liste:list)->list:
    for pos in texte:
        for x in pos:
            Liste.append(ord(x))
    return Liste


#Menu utilisateur, permet le choix de la base de cryptage
print("-------------------------""\n""Bienvenue dans ce programme de cryptage par clé de César""\n""-------------------------")
print("Base de cryptage :""\n""-   -   -   -   -   -   -" "\n""1.Ficier prédéfinis""\n""2.Rédaction console""\n""3.Fichier importé""\n""-------------------------")

select = int(input("Séléctionner la base de cryptage : "))
print("-------------------------")    


#via fichier prédéfini, donc conversion en nombre directement
if select == 1:
    with open("fichier_predefini.txt","r")as fic:
      texte = fic.readlines()
      conversion(Liste)

#via fichier que l'on écrit sois-même dans la console, donc rédaction puis conversion
if select == 2:
    with open("fichier_modifier.txt", "w+") as fic:
       fic.write(input("Rédiger le texte que vous souhaiter crypter : ""\n""\n"))
    with open("fichier_modifier.txt", "r") as fic:
       texte = fic
       conversion(Liste)
    print("-------------------------")

#via fichier importé dans le dossier, donc demande du fichier puis conversion
if select == 3:
    print("Mettez le fichier souhaiter dans le dossier_fichier_perso""\n""-------------------------")
    os.chdir('Dossier_fichier_perso')
    nom_fichier = str(input("Séléctionnez le fichier souhaité :"))
    with open(nom_fichier,"r", encoding = 'UTF-8') as fic:
        texte = fic.readlines()
    conversion(Liste)
    
            
#saisie de la clé
clef = int(input("Entrez la clé de cryptage : "))


#cryptage puis affichage
for x in Liste:
    CryptListe.append(x + clef)


motus = ""
for x in CryptListe:
    motus = motus + chr(x)

#export du cryptage dans un fichier

print("-------------------------""\n""Votre fichier est donc crypté, le voici""\n""-------------------------""\n" + motus)

if select == 1:
    with open("fichier_crypter_fichier_prédéfini.txt","w+",encoding='UTF-8')as f:
        f.write(motus)
if select==2:
    with open("fichier_crypter_fichier_modifier.txt","w+",encoding='UTF-8')as f:
        f.write(motus)
if select == 3:
    with open("fichier_crypter"+"_"+nom_fichier,"w+",encoding='UTF-8')as f:
        f.write(motus)

print("-------------------------")

#possibilité de décryptage pour vérification

rep = str(input("Voulez vous le décrypter (oui ou non) ? : "))

print("-------------------------")

if rep == "non":

    while(b >= 0):
        print(b,"...")
        time.sleep(0.5) 
        b -=1
    print("-------------------------")
    print("EXPLOSION !")
    print("-------------------------")
    time.sleep(1)
    print("C'est une boutade !")
    print("-------------------------")




if rep == "oui":
    for x in motus:
        ListeCrypte.append(ord(x))
  
 
    for x in ListeCrypte:
        DecryptListe.append(x - clef)
   
    motd = ""
    for x in DecryptListe:
        motd = motd + chr(x)
        

    print(motd)
    print("-------------------------")
    print("Et voilà ! Votre fichier avait donc été crypté avec succès !")
    print("-------------------------")
    

print("merci d'avoir utiliser notre programme")
print("^ ^")






    

        


