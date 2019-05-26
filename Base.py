
import csv
dane=[]
csvreader=None
with open('1.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=';')
    for row in csvreader:
        dane.append(row)


def Zdawalnosc(filtr,woj,rok):
    wyniki=[]
    wynik=[]
    zdane=0
    przystapilo=0
    if filtr==1:
        for i in range(len(dane)):
                    if dane[i][1]=='przystąpiło' and dane[i][0]==woj and dane[i][3]==rok:
                        przystapilo+=(int(dane[i][4]))
                    if dane[i][1]=='zdało' and dane[i][0]==woj  and dane[i][3]==rok:
                        zdane+=int(dane[i][4])
        #print(rok, int(zdane/przystapilo*100),"%")
        wynik=(woj,rok,int(zdane/przystapilo*100))
        wyniki.append(wynik)
        zdane=0
        przystapilo=0
        
    elif filtr==2:
            for i in range(len(dane)):
                if dane[i][1]=='przystąpiło' and dane[i][0]==woj and dane[i][3]==rok and dane[i][2]=='kobiety':
                    przystapilo=(int(dane[i][4]))
                if dane[i][1]=='zdało' and dane[i][0]==woj  and dane[i][3]==rok and dane[i][2]=='kobiety':
                    zdane=int(dane[i][4])
            #print("Tylko kobiety" ,rok, int(zdane/przystapilo*100),"%")
            wynik=(woj,rok,int(zdane/przystapilo*100))
            wyniki.append(wynik)
            zdane=0
            przystapilo=0
    else:
            for i in range(len(dane)):
                if dane[i][1]=='przystąpiło' and dane[i][0]==woj and dane[i][3]==rok and dane[i][2]=='mężczyźni':
                    przystapilo=(int(dane[i][4]))
                if dane[i][1]=='zdało' and dane[i][0]==woj  and dane[i][3]==rok and dane[i][2]=='mężczyźni':
                    zdane=int(dane[i][4])
            #print("Tylko mężczyźni" ,rok, int(zdane/przystapilo*100),"%")
            wynik=(woj,rok,int(zdane/przystapilo*100))
            wyniki.append(wynik)
            zdane=0
            przystapilo=0
    return wyniki

def Konwertuj(woj):
    if woj==1: woj='Zachodniopomorskie'
    elif woj==2: woj='Śląskie'
    elif woj==3: woj='Łódzkie'
    elif woj==4: woj='Lubelskie'
    elif woj==5: woj='Dolnośląskie'
    elif woj==6: woj='Opolskie'
    elif woj==7: woj='Podkarpackie'
    elif woj==8: woj='Podlaskie'
    elif woj==9: woj='Mazowieckie'    
    elif woj==10: woj='Małopolskie'
    elif woj==11: woj='Pomorskie'
    elif woj==12: woj='Warmińsko-Mazurskie'
    elif woj==13: woj='Kujawsko-pomorskie'
    elif woj==14: woj='Lubuskie'
    elif woj==15: woj='Wielkopolskie'
    elif woj==16: woj='Świętokrzyskie'
    else: 
        raise ValueError("Podana wartosć jest nieprawidłowa")
    return woj