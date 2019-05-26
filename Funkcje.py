
import csv
import Base 
dane=[]
csvreader=None
with open('1.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=';')
    for row in csvreader:
        dane.append(row)

def Srednia(filtr,woj,rok):
    sred=0
    if filtr==1:
        for i in range (len(dane)):
            if dane[i][0]==woj and dane[i][3]==rok and dane[i][1]=='przystąpiło':
                sred+=int(dane[i][4])
        print("W roku ",rok," w województwie" ,woj, "do egzaminu przystąpiło", sred, "osób")                
    elif filtr==2:    
        for i in range (len(dane)):
            
            if dane[i][0]==woj and dane[i][3]==rok and dane[i][1]=='przystąpiło' and dane[i][2]=='kobiety':
                sred=int(dane[i][4])
        print("W roku ",rok," w województwie" ,woj, "do egzaminu przystąpiło", sred, "kobiet")   
    else:    
        for i in range (len(dane)):
            if dane[i][0]==woj and dane[i][3]==rok and dane[i][1]=='przystąpiło' and dane[i][2]=='mężczyźni':
                sred=int(dane[i][4])
        print("W roku ",rok," w województwie" ,woj, "do egzaminu przystąpiło", sred, "mężczyzn")        
            

def Procent_zdawalnosc(filtr,woj):
    score=[]
    years=['2010','2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
    if filtr==2:
        print("Procent zdawalnosci kobiet")
    elif filtr==3:
        print("Procent zdawalnosci mężczyzn")
    for year in years:
            score.append(Base.Zdawalnosc(filtr,woj,year))
    return score


def Najlepsza_zdawalnosc(filtr, rok):
    if filtr==2:
        print('Wynik podawany dla kobiet')
    elif filtr==3:
        print('Wynik podawany dla mężczyzn')
    wojewodztwa=[]
    zdawalnosc_we_wszystkich_wojew=[]
    only_rate=[]
    wynik=[]
    for i in range(len(dane)):
        wojewodztwa.append(dane[i][0])
    wojewodztwa=list(set(wojewodztwa))
    wojewodztwa.remove('Polska') 
    wojewodztwa.remove('Terytorium')
    
    for wojew in wojewodztwa:
        zdawalnosc_we_wszystkich_wojew.append(Base.Zdawalnosc(filtr,wojew,rok))
    for x in range (len(zdawalnosc_we_wszystkich_wojew)):
        only_rate.append(zdawalnosc_we_wszystkich_wojew[x][0][2])    
    max_rate=max(only_rate)
    for i in range(len(zdawalnosc_we_wszystkich_wojew)):
        if zdawalnosc_we_wszystkich_wojew[i][0][2]==max_rate:
            wynik.append(zdawalnosc_we_wszystkich_wojew[i])
            print('rok: ', zdawalnosc_we_wszystkich_wojew[i][0][1], 'wojewodztwo: ', zdawalnosc_we_wszystkich_wojew[i][0][0])
    return wynik

def Regresja(filtr):
    wojewodztwa=[]
    for i in range(len(dane)):
            wojewodztwa.append(dane[i][0])
    wojewodztwa=list(set(wojewodztwa))
    wojewodztwa.remove('Polska') 
    wojewodztwa.remove('Terytorium')
    for wojew in wojewodztwa:
        zdawalnosc=Procent_zdawalnosc(filtr,wojew)
        for i in range(len(zdawalnosc)-1):
            if zdawalnosc[i][0][2]>zdawalnosc[i+1][0][2]:
                print('Zanotowano regresję: ', zdawalnosc[i][0][0], zdawalnosc[i][0][1],'->', zdawalnosc[i+1][0][1])

def Porównanie(filtr, woj,woj2):
    zdawalnosc_woj=Procent_zdawalnosc(filtr,woj)
    zdawalnosc_woj2=Procent_zdawalnosc(filtr,woj2)
    for i in range(len(zdawalnosc_woj)):
        if zdawalnosc_woj[i][0][2]>zdawalnosc_woj2[i][0][2]:
            print(zdawalnosc_woj[i][0][1],zdawalnosc_woj[i][0][0])
        elif zdawalnosc_woj[i][0][2]<zdawalnosc_woj2[i][0][2]:
            print(zdawalnosc_woj2[i][0][1],zdawalnosc_woj2[i][0][0])
        else: print(zdawalnosc_woj[i][0][0],zdawalnosc_woj2[i][0][0], "Zdawalnosc w tych wojewodztwach jest taka sama")

