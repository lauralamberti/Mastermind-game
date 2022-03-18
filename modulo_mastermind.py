#contiene le seguenti funzioni
# costruisci(N_colori)   - costruisce l'elenco delle disposizioni
# pulisci(prova, tentativo, codice) - elimina le disposizioni
#                                    che non possono essere la soluzione
# confronta(guess, code)   - confronta il tentativo con il codice
# verifica(n_neri)      -  verifica la soluzione
# stampa(win)      - stampa il commento alla fine
# build_guess(a, b, c, d)    -  costruisce il tentativo



def costruisci(N_colori):
      count=0
      prova=[0]*1296
      #costruzione dell'array prova[i] con tutte le possibili permutazioni
      for a in range(0,N_colori):
          for b in range(0,N_colori):
              for c in range(0,N_colori):
                  for d in range(0,N_colori):
                     prova[count]=build_guess(a, b, c, d)
                     count = count + 1

      return prova


##################################################
##################################################

def pulisci(prova, tentativo, codice):
      #list(prova)
      elimino=[]
      riparto=[]
      n_neri_cod=confronta(tentativo,codice)[0]
      n_bianchi_cod=confronta(tentativo,codice)[1]

      if (n_neri_cod==0 and n_bianchi_cod==0):
          for j in range (0,len(prova)):
            for i in range(4):
              if (prova[j][i] in tentativo):
                  if (prova[j] not in elimino):
                                          elimino.append(prova[j])
                                          break

      
  #    print("risposta dentro pulisci tra tentativo e codice  n_neri_cod= %i n_bianchi_cod= %i" %(n_neri_cod, n_bianchi_cod))
      for j in range (0,len(prova)):
             for i in range(4):
                    if (confronta(prova[j],tentativo)[0]!= n_neri_cod or confronta(prova[j],tentativo)[1]!= n_bianchi_cod) :
                             if (prova[j] not in elimino):
                                            elimino.append(prova[j])
                                            break        

      for item in elimino:
                       
        prova.remove(item)
      if tentativo in prova: 
        prova.remove(tentativo)
      #for i in range(len(prova)):
         #     print(i, "prova \n",prova[i] )
      elimino=[]
      return 
######################################################
def confronta(guess, code):
        n_neri = 0
        n_bianchi = 0
        for i in range(4):
            if guess[i] == code[i]:
                n_neri += 1    #aumento i chiodini neri
                guess[i] += "PEG!"
                code[i] += "PEG!"
        for i in range(4):
            if guess[i] in code and guess[i] != code[i]:
                n_bianchi += 1    #aumento i chiodini bianchi
                code[code.index(guess[i])] += "PEG!"
         
        for i in range(4):
            if len(code[i]) > 1:
                code[i] = (code[i])[0]
                guess[i]=(guess[i])[0]

         
        return n_neri, n_bianchi
######################################################

def verifica(n_neri):
   
    if (n_neri == 4):
            win = True
    else: 
            win = False
  
    return win
####################################################

def stampa(win, codice):
        if win == True:
          return print("Hai vinto! Il codice segreto è " + "".join(codice) + ".")
        else:
          return print("Mi dispiace il codice segreto era " + "".join(codice) + ". Hai perso.")
 

################################################

def build_guess(a, b, c, d):
    colours = ["V","R","G","B","A","L"]  
    guess_pc=[]
    guess_pc.append(colours[a])
    guess_pc.append(colours[b])
    guess_pc.append(colours[c])
    guess_pc.append(colours[d])
    guess_pc=list(guess_pc)
    return guess_pc
###############################################


def punteggio (item, S):
  
  punti=0
  occurrences=[0]*50
  max_occur=0
  t=0
  for j in range (len(S)):
  #  if (item!=S[j]):
          n_bianchi=confronta(item,S[j])[0]
          n_neri=confronta(item,S[j])[1]
          t=n_bianchi+10*n_neri
          occurrences[t] +=1
  for t in range(len(occurrences)):
 #   if (item ==[ "Y", "R", "B", "O"]):
         # print( "valore della risposta = %i frequenza %i" %(t, occurrences[t]))
 #         print(t, occurrences[t])
    if (occurrences[t]>max_occur):
          max_occur=occurrences[t]
      #max_scores fornisce il numero massimo di elementi di S che l'item che si sta valutando si porterebbe appresso
  #punti= len(S)-max_scores      
  #return punti
#  if (item ==[ "Y", "R", "B", "O"]):
 #         print( "caso peggiore= %i" %max_occur  )           
  return max_occur
        

     
