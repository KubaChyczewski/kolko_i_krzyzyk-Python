import numpy as np
import pytest
import os
clear = lambda: os.system('cls')

def wywolanie_planszy(plansza):
    pusta_plansza="""
  1 | 2 | 3
--------------
  4 | 5 | 6
--------------
  7 | 8 | 9
"""
    for i in range(1,10):
        if (plansza[i] in ['O','X']):
            pusta_plansza=pusta_plansza.replace(str(i), plansza[i])
    print(pusta_plansza)




def znak_gracza():
    i=True
    while i==True:
        gracz1=input("Wybierz symbol X lub O dla gracza 1: ")
        if gracz1 in ['x','X']:
            gracz1=gracz1.upper()
            gracz2='O'
            i=False
            print("Symbol pierwszego gracza: %s \nSymbol drugiego gracza: %s" %(gracz1,gracz2))
            return gracz1,gracz2
        elif gracz1 in ['o','O']:
            gracz2="X"
            i=False
            gracz1=gracz1.upper()
            print("Symbol pierwszego gracza: %s \nSymbol drugiego gracza: %s" %(gracz1,gracz2))
            return gracz1,gracz2
        else:
            print("Błędy znak")
        



def wybor_pola(plansza,znak):
    liczba=input("Podaj numer od 1 do 9: ")
    if liczba not in ["1","2","3","4","5","6","7","8","9"]:
        print("Błędna liczba")
        wybor_pola(plansza,znak)
    elif plansza[int(liczba)]!='*':
        print("Pole już zajęte!")
        wybor_pola(plansza,znak)
    elif int(liczba)<1 or int(liczba)>9 :
        print("Błędna liczba")
        wybor_pola(plansza,znak)
    else:
        plansza[int(liczba)]=znak

def czy_komputer():
    a=input("""Wybierz tryb gry:
               A - z komputerem
               B - 2 graczy
: """)
            
    if a in ["A","a"]:
        return True
    elif a in ["B","b"]:
        return False
    else:
        print("Błędy wybór, wybierz jeszcze raz: ")
        czy_komputer()
            
def wybor_pola_z_komputerem(plansza,znak,j):
    if j==0:
        liczba=input("Podaj numer od 1 do 9: ")
        if liczba not in ["1","2","3","4","5","6","7","8","9"]:
            print("Błędna liczba")
            wybor_pola_z_komputerem(plansza,znak,j)
        elif plansza[int(liczba)]!='*':
            print("Pole już zajęte!")
            wybor_pola_z_komputerem(plansza,znak,j)
        elif int(liczba)<1 or int(liczba)>9 :
            print("Błędna liczba")
            wybor_pola_z_komputerem(plansza,znak,j)
        else:
            plansza[int(liczba)]=znak
    else:
        liczba=np.random.randint(1,10)
        if plansza[int(liczba)] != '*':
            print("Pole już zajęte!")
            wybor_pola_z_komputerem(plansza,znak,j)
        else:
            plansza[int(liczba)]=znak
        
        


def wygrana(plansza,znak):
    if plansza[1]==plansza[2]==plansza[3]==znak:
        return True
    if plansza[4]==plansza[5]==plansza[6]==znak:
        return True
    if plansza[7]==plansza[8]==plansza[9]==znak:
        return True
    if plansza[1]==plansza[4]==plansza[7]==znak:
        return True
    if plansza[2]==plansza[5]==plansza[8]==znak:
        return True
    if plansza[3]==plansza[6]==plansza[9]==znak:
        return True
    if plansza[1]==plansza[5]==plansza[9]==znak:
        return True
    if plansza[3]==plansza[5]==plansza[7]==znak:
        return True
    else:
        return False

def pelna_plansza(plansza):
    j=0
    for i in range(len(plansza)):
        if plansza[i]=='*':
            j+=1
    if j==1:
        return True
    else:
        return False
        

def main():
    plansza1=['*','*','*','*','*','*','*','*','*','*']
    j=0
    if czy_komputer() == False:
        gracze=znak_gracza()
        while pelna_plansza(plansza1)==False and wygrana(plansza1,gracze[0])==False and wygrana(plansza1,gracze[1])==False:
            wywolanie_planszy(plansza1)
            print("Ruch gracza "+str(j+1)+"("+gracze[j]+")")
            wybor_pola(plansza1,gracze[j])
            j=(0 if j==1 else 1)
            clear()
            
        wywolanie_planszy(plansza1)
        if pelna_plansza(plansza1)==True:
            print("Remis :D")
        elif wygrana(plansza1,gracze[0])==True:
            print("Wygrywa gracz 1 , GRATULACJE!!")
        else:
            print("Wygrywa gracz 2 , GRATULACJE!!")
    else:
        gracze=znak_gracza()
        while pelna_plansza(plansza1)==False and wygrana(plansza1,gracze[0])==False and wygrana(plansza1,gracze[1])==False:
            wywolanie_planszy(plansza1)
            if j ==0:
                print("Twój ruch"+"("+gracze[j]+")")
            wybor_pola_z_komputerem(plansza1,gracze[j],j)
            j=(0 if j==1 else 1)
            clear()
            
        wywolanie_planszy(plansza1)
        if pelna_plansza(plansza1)==True:
            print("Remis :D")
        elif wygrana(plansza1,gracze[0])==True:
            print("Wygrana :D , GRATULACJE!!")
        else:
            print("Przegrana :( ")
    input("Zamknij")
            

def test_nie_pelna_plansza():
    #given
    plansza=["*","*","*",8]
    #when
    result=pelna_plansza(plansza)
    #then
    assert result
    assert pelna_plansza(["*",1,3,"*"])

def test_pelna_plansza():
    #given
    plansza=["*",5,6,1]
    #when
    result=pelna_plansza(plansza)
    #then
    assert result == False
        
main()

                
