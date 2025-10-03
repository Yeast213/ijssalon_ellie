from algemene_functies import mijn_functie_2

def aanbieding_1(smaak,prijs,korting):
    prijsNaKorting = prijs * (1 - korting)
    reclame = (f"Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijsNaKorting} euro.")
    print (reclame)

aanbieding_1("aardbei",4,0.1)

def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for bedrag in inkomsten:
        totaal += bedrag
    btw_bedrag = totaal * btw
    uitvoer = (f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden.")
    return uitvoer

inkomsten = inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09)
print (inkomsten)

def hoog_en_laag(mijn_lijst):
    hoog = max(mijn_lijst)
    laag = min(mijn_lijst)
    uitvoer = [hoog, laag]
    return uitvoer

getallen = hoog_en_laag([220, 430, 125, 160, 205, 90, 345])
print (getallen)

def gemiddelde(mijn_lijst):
    totaal = 0
    for bedrag in mijn_lijst:
        totaal += bedrag
    gemiddelde = totaal / 7
    uitvoer = (f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro.")
    return uitvoer

getallen = gemiddelde([220, 430, 125, 160, 205, 90, 345])
print (getallen)

def meervoudig(invoer_lijst):
    hoog_laag = hoog_en_laag(invoer_lijst)
    uitvoer = hoog_laag
    return uitvoer

invoerLijst = meervoudig([10,5,3,2,1,2,9])
print (invoerLijst)

def combinatie(invoer_lijst_2):
    korte_lijst = hoog_en_laag(invoer_lijst_2)
    hoog = korte_lijst[0]
    laag = korte_lijst[1]
    uitvoer = mijn_functie_2(hoog, laag)
    return uitvoer

invoer_lijst_2 = combinatie([5,9,2,4,7,10,3])
print (invoer_lijst_2)