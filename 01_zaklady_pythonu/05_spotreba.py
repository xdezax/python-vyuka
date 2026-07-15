kilometry = float(input("Kolik kilometrů jsi ujel? "))
litry = float(input("Kolik litrů nafty jsi natankoval? "))
cena = float(input("Kolik stojí litr nafty? "))

spotreba = (litry/kilometry)*100

print()
print("Výsledek")
print("--------------------")
print("Spotřeba je", round(spotreba, 2),"l/100km")

if spotreba < 30:
    print("Výborná spotřeba!")

cena_celkem = litry*cena

print("Cena nafty")
print("--------------------")
print(f"Nafta stála celkem {cena_celkem:.2f} Kč")




