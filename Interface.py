import Funkcje as f
import Base 

print ("Witaj w analizatorze bazy danych.")
print("1. Pokaż srenią liczbę osób, które przystąpiły do egzaminu w danym roku (2010-1018) w wybranym województwie")
print ("2. Oblicz procentową zawartosć zdawalnosci dla danego województwa w latach 2010-2018")
print("3. Podaj województwa o najlepszej zdawalności w konkretnym roku")
print("4. Wykryj województwa, które zanotowały regresję, jeżeli istnieją")
print("5. Porównaj dwa województwa, które z województw miało lepszą zdawalność w każdym dostępnym roku\nWybierz odpowiedni numer zapytania... ")
zad=int(input())
print ("Czy chcesz rozróżnienie na płeć?\n1.Nie\n2.Tak - tylko kobiety\n3.Tak - tylko mężczyźni")
filtr=int(input())


if zad == 1:
    print("Wybierz województwo: \n1.Zachodniopomorskie \n2.Śląskie \n3.Łódzkie \n4.Lubelskie \n5.Dolnośląskie \n6.Opolskie \n7.Podkarpackie \n8.Podlaskie \n9.Mazowieckie\n10.Małopolskie \n11.Pomorskie \n12.Warmińsko-Mazurskie \n13.Kujawsko-pomorskie \n14.Lubuskie \n15.Wielkopolskie\n16.Świętokrzyskie")
    w=int(input())
    woj=Base.Konwertuj(w)
    print("Podaj rok:")
    rok=str(input())
    f.Srednia(filtr,woj,rok)
elif zad==2:
    print("Wybierz województwo: \n1.Zachodniopomorskie \n2.Śląskie \n3.Łódzkie \n4.Lubelskie \n5.Dolnośląskie \n6.Opolskie \n7.Podkarpackie \n8.Podlaskie \n9.Mazowieckie\n10.Małopolskie \n11.Pomorskie \n12.Warmińsko-Mazurskie \n13.Kujawsko-pomorskie \n14.Lubuskie \n15.Wielkopolskie\n16.Świętokrzyskie")
    w=int(input())
    woj=Base.Konwertuj(w)
    temp=f.Procent_zdawalnosc(filtr,woj)
    for i in range(len(temp)):
        print(temp[i][0][1], temp[i][0][2],"%" )
elif zad==3:
    print("Podaj rok: ")
    rok=str(input())
    f.Najlepsza_zdawalnosc(filtr,rok)
elif zad==4:
    f.Regresja(filtr)
else:
    print("Wybierz województwo: \n1.Zachodniopomorskie \n2.Śląskie \n3.Łódzkie \n4.Lubelskie \n5.Dolnośląskie \n6.Opolskie \n7.Podkarpackie \n8.Podlaskie \n9.Mazowieckie\n10.Małopolskie \n11.Pomorskie \n12.Warmińsko-Mazurskie \n13.Kujawsko-pomorskie \n14.Lubuskie \n15.Wielkopolskie\n16.Świętokrzyskie")
    print("Wybierz województwo pierwsze")
    w=int(input())
    woj=Base.Konwertuj(w)
    print("Wybierz województwo drugie")
    w2=int(input())
    woj2=Base.Konwertuj(w2)
    f.Porównanie(filtr,woj,woj2)

    