from random import randint
cartedemineur = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

affichage = [["☐","☐","☐","☐","☐","☐"],["☐","☐","☐","☐","☐","☐"],["☐","☐","☐","☐","☐","☐"],["☐","☐","☐","☐","☐","☐"],["☐","☐","☐","☐","☐","☐"],["☐","☐","☐","☐","☐","☐"]]

def fonction(morpion):
  print("   1 2 3 4 5 6")
  for ligne in range (0,len(morpion)):
    print(ligne+1,end=" |")
    for colonne in range(0,len(morpion[0])):
      print(morpion[ligne][colonne],end=" ")
    print("")

def addcase(mat,lign,colon):
  if(lign-1>=0 and colon-1>=0):

    if(mat[lign-1][colon-1]!="💣"):
      mat[lign-1][colon-1]+=1

  if(lign-1>=0):

    if(mat[lign-1][colon]!="💣"):
      mat[lign-1][colon]+=1
  
  if(lign+1<6):

    if(mat[lign+1][colon]!="💣"):
      mat[lign+1][colon]+=1

  if(lign-1>=0 and colon+1<6):

    if(mat[lign-1][colon+1]!="💣"):
      mat[lign-1][colon+1]+=1
    
  if(colon-1>=0):

    if(mat[lign][colon-1]!="💣"):
      mat[lign][colon-1]+=1  
    
  if(colon+1<6):

    if(mat[lign][colon+1]!="💣"):
      mat[lign][colon+1]+=1
      
  if(lign+1<6 and colon+1<6):

    if(mat[lign+1][colon+1]!="💣"):
      mat[lign+1][colon+1]+=1


def bombes(matrice):
  bombe=0
  while bombe < 6 :
    ligne = randint(0,5)
    colonne= randint(0,5)
    if(matrice[ligne][colonne] != "💣"):
      matrice[ligne][colonne]="💣"
      bombe+=1
      addcase(matrice,ligne,colonne)

def interact(me):
  choixL=int(input("choix de la ligne :"))-1
  choixC=int(input("choix de la colonne :"))-1
  affichage[choixL][choixC]=cartedemineur[choixL][choixC]
  fonction(affichage)
  if(cartedemineur[choixL][choixC]=="💣"):
    print("you lose")
    return False
  return True



victoire = True
bombes(cartedemineur)
fonction(affichage)
while(victoire):
  victoire = interact(cartedemineur)
