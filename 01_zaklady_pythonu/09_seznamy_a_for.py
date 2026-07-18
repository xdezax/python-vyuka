jizdy = []

while True:
    zadani = input("Zadej počet kilometrů nebo napiš konec: ")
    zadani = zadani.strip().lower()
    
    if zadani == "konec":
         break
    

    try:
        kilometry = float(zadani.replace(",", "."))
        
        if kilometry <= 0:
            print("Počet kilometrů musí být větší než nula.")
            continue
        
        
        jizdy.append(kilometry)

        
    except ValueError:
        print("Zadej platné číslo nebo slovo konec")


print()
print("    Přehled jízd")
print("---------------------")

for poradi, jizda in enumerate(jizdy, start=1):
    print(f"{poradi}. jízda: {jizda:.2f} km")

celkem_km = sum(jizdy)
pocet_jizd = len(jizdy)

print("---------------------")
print(f"Celkem ujeto: {celkem_km:.2f} km")
print(f"Počet jízd: {pocet_jizd}")

if pocet_jizd > 0:
            
    prumer_km = celkem_km / pocet_jizd


    print(f"Průměrná délka jízdy: {prumer_km:.2f} km")
    print(f"Nejkratší jízda: {min(jizdy):.2f} km")   
    print(f"Nejdelší jízda: {max(jizdy):.2f} km")

    pocet_nad_prumerem = 0

    for jizda in jizdy:
       
        if jizda > prumer_km:
            pocet_nad_prumerem += 1
    print(f"Jízd delších než průměr: {pocet_nad_prumerem}")


else:
    print("Nebyla zadána žádná jízda.")
    
    
print("Na shledanou příště")

