kilometry = float(input("Kolik kilometrů jsi ujel? "))
litry = float(input("Kolik litrů nafty jsi natankoval? "))
vaha1 = float(input("Kolik kilogramů průměrně vážil náklad?  "))
cena = float(input("Kolik stojí litr nafty? "))
vaha = float(input("Kolik kilogramů bude vážit další náklad? "))
dalsi_cesta = float(input("Kolik kilometrů bude mít další cesta? "))
cena1 = float(input("Kolik zaplatí za tkm? "))

spotreba = litry/kilometry*100
cena_celkem = litry*cena
cena_na_km = cena_celkem/kilometry
dalsi = dalsi_cesta*cena_na_km
dalsi_tkm = dalsi_cesta*vaha 
tkm = vaha1*kilometry
sazba = cena_celkem/(vaha1*kilometry)
sazba1 = (cena_na_km*dalsi_cesta)/(vaha*dalsi_cesta)
naklady = (cena_na_km*dalsi_cesta)
trzba = dalsi_tkm*cena1
zisk = trzba -naklady 

def hlavicka():
    print("============================================")
    print("           KALKULAČKA KAMIONU")
    print("============================================")




def vypis_vysledku():
    print()
    print("Výsledek")
    print("--------------------------------------------")
    print(f"Spotřeba je {spotreba:.2f} l/100km")
    print()
    print(f"Nafta stála celkem {cena_celkem:.2f} Kč")
    print()
    print(f"Cena na 1 km je {cena_na_km:.2f} Kč")
    print()
    print(f"Výkon byl {tkm:.2f} tkm")
    print()
    print(f"Sazba je {sazba:.2f} Kč/tkm")
    print()
    print(f"Další cesta bude stát {dalsi:.2f} Kč")
    print()
    print(f"Výkon na další jízdu je {dalsi_tkm:.2f} tkm")
    print()
    print(f"Sazba na další jízdu je {sazba1:.2f} Kč/tkm")
    print()
    print(f"Zisk z další jízdy je {zisk:.2f} Kč")
print()
print("Výsledek")
print("--------------------------------------------")
print(f"Spotřeba je {spotreba:.2f} l/100km")
print()
print(f"Nafta stála celkem {cena_celkem:.2f} Kč")
print()
print(f"Cena na 1 km je {cena_na_km:.2f} Kč")
print()
print(f"Výkon byl {tkm:.2f} tkm")
print()
print(f"Sazba je {sazba:.2f} Kč/tkm")
print()
print(f"Další cesta bude stát {dalsi:.2f} Kč")
print()
print(f"Výkon na další jízdu je {dalsi_tkm:.2f} tkm")
print()
print(f"Sazba na další jízdu je {sazba1:.2f} Kč/tkm")
print()
print(f"Zisk z další jízdy je {zisk:.2f} Kč")
print()
print()
if spotreba < 30:
    print("Máš výbornou spotřebu!")

elif spotreba <= 35:
    print("Máš dobrou spotřebu.")
    
elif spotreba >= 50:
    print("Šlapej na top míň kokote!!!")   
else:
    print("Máš vysokou spotřebu!!")
print()
print()
if zisk <= 0:
    print("Na téhle cestě proděláš!")

elif zisk <=5000:
    print("Zisk z téhle cesty je nízký.")

elif zisk <= 15000:
    print("Zisk z téhle cesty je dobrý.")    

else:
    print("Super kšeft!!!")    
print()
print()
print()
print("Šťastnou cestu.")    


vypis_vysledku()
hlavicka()








