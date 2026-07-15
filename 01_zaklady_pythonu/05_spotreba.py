kilometry = float(input("Kolik kilometrů jsi ujel? "))
litry = float(input("Kolik litrů nafty jsi natankoval? "))

spotreba = (litry/kilometry)*100

print()
print("Výsledek")
print("--------------------")
print("Spotřeba je", round(spotreba, 2),"l/100km")

if spotreba < 30:
    print("Výborná spotřeba!")

print()
print("Cena nafty")
cena = float(input("Kolik stojí litr nafty? "))
cena_celkem = (litry*cena)
print(f"Nafta stála celkem {cena_celkem:.2f} Kč")



