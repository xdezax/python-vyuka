def nacti_kladne_cislo(vyzva):
    while True:
        text = input(vyzva).strip().lower()

        if text == "konec":
           return None
            
            
        try:
            hodnota = float(text.replace(",", "."))           

            if hodnota <= 0:
                print("Číslo musí být větší než nula ")
                continue            
            

            return hodnota           
        
        except ValueError:
            print("Zadej pouze číslo. Text nebude akceptován! ")





jizdy = []


while True:
    kilometry = nacti_kladne_cislo("Kolik si najel kilometrů? ")
 
    if kilometry is None:
     break
 
    jizdy.append(kilometry)
 

 
 
celkem_km = sum(jizdy)         
pocet_jizd = len(jizdy)

print()
print("       Evidence jízd")
print("================================")



if pocet_jizd == 0:
    print("Nebyla zadána žádná jízda.")


else:
    for poradi, jizda in enumerate(jizdy, start=1):
        print(f"{poradi}. jízda: {jizda:.2f} km")

    prumer_km = celkem_km / pocet_jizd
    



    print(f"Celkem ujeto {celkem_km:.2f} km")
    print(f"Počet jízd {pocet_jizd}.")
    print(f"Průměrná trasa měří {prumer_km:.2f} km")
    print(f"Nejdelší trasa měří {max(jizdy):.2f} km")
    print(f"Nejkratší trasa měří {min(jizdy):.2f} km")


      
