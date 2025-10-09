def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def onderstreep(tekst):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    uitvoer = uit
    return uitvoer

def som(dictionary):
    totaal = 0
    for item in dictionary:
        totaal += (dictionary[item])
    return totaal