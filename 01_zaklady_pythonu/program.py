# 1. FUNKCE
def nacti_kladne_cislo(vyzva):
    while True:
        text = input(vyzva).strip().replace(",", ".")

        try:
            hodnota = float(text)

            if hodnota <= 0:
                print("Číslo musí být větší než nula.")
                continue

            return hodnota
        
        except ValueError:
            print("Zadej platné číslo")
            


#2. PŘÍPRAVA DAT
jizdy =[] 

#3. ZADÁVÁNÍ JÍZD
while True:
    nakladka = input("\nMísto nakládky ,nebo slovo konec: ").strip()

    if nakladka.lower() == "konec":
        break
    vykladka = input("Místo vykládky: ").strip()

    kilometry = nacti_kladne_cislo("Počet kilometrů: ")

    hmotnost = nacti_kladne_cislo("Hmotnost nákladu v tunách: ")

    jizda = {
        "nakladka": nakladka,
        "vykladka": vykladka,
        "kilometry": kilometry,
        "hmotnost": hmotnost,
    }

    jizdy.append(jizda)

#4. VÝPIS JEDNOTLIVÝCH JÍZD
print()
print("         Přehled jízd")
print("================================")

for poradi, jizda in enumerate(jizdy, start=1):
    tkm = jizda["kilometry"] * jizda["hmotnost"]


    print(f"{poradi}. jízda")
    print(f"Trasa: {jizda['nakladka']} " f"====> {jizda['vykladka']}")
    print(f"Kilometry: {jizda['kilometry']:.2f} km")
    print(f"Hmotnost: {jizda['hmotnost']:.2f} t")
    print(f"Dopravní výkon {tkm:.2f} tkm")
    print("------------------------------")

#5. CELKOVÝ SOUHRN
if jizdy:
    celkem_km = 0
    celkem_tkm = 0


    for jizda in jizdy:
        celkem_km += jizda["kilometry"]
        celkem_tkm += jizda['kilometry'] * jizda['hmotnost']
    prumer_jizdy = celkem_km / len(jizdy)
        
    print("            SOUHRN")
    print("==================================")
    print(f"Počet jízd: {len(jizdy)}")
    print(f"Celkem kilometrů: {celkem_km:.2f} km")
    print(f"Celkem tkm: {celkem_tkm:.2f} tkm")
    print(f"Průměrná délka jízdy: {prumer_jizdy:.2f} km")

else:
    print("Nebyla zadána žádná jízda.")
          

