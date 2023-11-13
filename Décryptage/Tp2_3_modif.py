import string
import os
import time

k=0
n=[]
cle = 0
Liste = []
liste2 = []
mot = ""
newtext=""
dico1={"e" : 12.10,"a": 7.11, "i" : 6.59, "s": 6.51 }
dico2={"e" : 0, "a" : 0, "i" : 0, "s" : 0}
fin = 0
b = 3
nom_fichier = str

#Menu de séléction
print("-------------------------""\n""Bienvenue dans ce programme de décryptage de clé de César""\n""-------------------------")
print("Base de cryptage :""\n""-   -   -   -   -   -   -" "\n""1.Ficier prédéfinis""\n""2.Fichier perso""\n""-------------------------")

select=int(input("Séléctionner la base de cryptage : "))
print("-------------------------")

#décryptage du fichier prédéfini

if select == 1:
    with open("fichier_crypter_predefini.txt","r", encoding = 'UTF-8')as fic:
        texte = fic.readlines()

    for i in texte:
        for x in i:
            Liste.append(ord(x))

#décryptage fichier séléctionnée par l'utilisateur
if select == 2:
    print("Mettez le fichier souhaiter dans le dossier_fichier_perso""\n""-------------------------")
    os.chdir('Dossier_fichier_perso')
    nom_fichier = str(input("Séléctionnez le fichier souhaité :"))
    with open(nom_fichier,"r", encoding = 'UTF-8') as fic:
        texte = fic.readlines()
    for i in texte:
        for x in i:
            Liste.append(ord(x))
    
#programme pour trouver la clé de cryptage
def bruteforce(Liste:list, i:int):
    dico2={"e" : 0, "a" : 0, "i" : 0, "s" : 0}
    liste2 = []
    print("pour un décalge :" , i)
    for x in Liste:
        liste2.append(chr((x+i)%256))
    for x in liste2:
        if x == 'e' or x == 'a' or x == 'i' or x == 's':
            dico2[x] += 1
    dico2['e'] = round(dico2['e']/len(liste2)*100, 2)
    dico2['a'] = round(dico2['a']/len(liste2)*100, 2)
    dico2['i'] = round(dico2['i']/len(liste2)*100, 2)
    dico2['s'] = round(dico2['s']/len(liste2)*100, 2)
    print(dico2)
    if (dico2['e'] > dico1['e'] -2 and dico2['e'] <dico1['e']+2 ):
        if (dico2['a'] > dico1['a']-2 and dico2['a'] <dico1['a']+2):
            if (dico2['i'] > dico1['i']-2 and dico2['i'] <dico1['i']+2):
                if (dico2['s'] > dico1['s']-2 and dico2['s'] <dico1['s']+2):
                    if ((i-256)%256) > 128:
                         print("-------------------------""\n""La clé de décryptage est : ",256-(i-256)%256,"\n""-------------------------")
                    else:
                         print("-------------------------""\n""La clé de décryptage est : ",(i-256)%256,"\n""-------------------------")

                    return 1
    return 0;

while(fin == 0 and k < 256):
    k += 1
    fin = bruteforce(Liste, k)
    cle = 256-k

#possibilité de décryptage via la clé trouvé

rep = str(input("Voulez vous le décrypter (oui ou non) ? : "))

print("-------------------------")

if rep == "non":

    while(b>=0):
        print(b,"...")
        time.sleep(0.5) 
        b-=1
    print("-------------------------")
    print("EXPLOSION !")
    print("-------------------------")
    time.sleep(1)
    print("C'est une boutade")
    print("-------------------------")




if rep == "oui":
  for z in texte:
    for x in z:
        newtext = newtext +  chr(ord(x)-cle) 
    print(newtext)
    print("-------------------------")
    print("Et voilà ! Votre fichier a donc été décrypté avec succès !")
    print("-------------------------")
    

print("merci d'avoir utiliser notre programme")
print("^ ^")





    

































