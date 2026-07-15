kilometry = float(input("Kolik kilometrů jsi ujel? "))
litry = float(input("Kolik litrů nafty jsi natankoval? "))

spotreba = (litry/kilometry)*100

print()
print("Výsledek")
print("--------------------")
print("Spotřeba je", round(spotreba, 2),"l/100km")

if spotreba < 30:
    print("Výborná spotřeba!")