jizdy= []

while True:
    kilometry = input("Zadej počet kilometrů nebo napiš konec: ")
    kilometry = kilometry.strip().lower()
    
    if kilometry == "konec":
        break

    try:
        kilometry = float(kilometry.replace(",", "."))
        
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

try:
    if pocet_jizd > 0:
        prumer_km = celkem_km / pocet_jizd
        print(f"Průměrná délka jízdy: {prumer_km:.2f} km")
    else:
        print("Nebyla zadána žádná jízda.")

except ValueError:
    print("Nezadán žádný vstup")        

    
           




