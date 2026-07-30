import json
from pathlib import Path

SOUBOR_JIZD = Path(__file__).resolve().parent / "jizdy.json"
# 1. FUNKCE
def uloz_jizdy(jizdy):
    with SOUBOR_JIZD.open("w", encoding="utf-8") as soubor:
        json.dump(jizdy, soubor, ensure_ascii=False, indent=4)

    print(f"Jízdy byly uloženy do souboru: {SOUBOR_JIZD}")    


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



def vypis_souhrn(jizdy):
    if not jizdy:
        print("Nebyla zadána žádná jízda")
        return
    
    celkem_km = 0
    celkem_tkm = 0
    celkem_nafta = 0
    celkove_naklady = 0
    celkova_cena_jizd = 0
    

    for jizda in jizdy:
        celkem_nafta += jizda["palivo"]
        celkem_km += jizda["kilometry"]
        celkem_tkm += spocitej_tkm(jizda["kilometry"], jizda["hmotnost"])
        celkove_naklady += spocitej_naklady_na_palivo(jizda)
        celkova_cena_jizd += spocitej_cenu_jizdy(jizda)
        
    prumer_jizdy = celkem_km / len(jizdy)
    celkovy_zisk = (celkova_cena_jizd - celkove_naklady)
    spotreba_prumer = (celkem_nafta / celkem_km) * 100
   
        
    print("            SOUHRN")
    print("==================================")
    print(f"Počet jízd: {len(jizdy)}")
    print(f"Celkem kilometrů: {celkem_km:.2f} km")
    print(f"Celkem tkm: {celkem_tkm:.2f} tkm")
    print(f"Průměrná délka jízdy: {prumer_jizdy:.2f} km")
    print(f"Průměrná spotřeba: {spotreba_prumer:.2f} l/100 km")
    print(f"Celkem natankováno: {celkem_nafta:.2f} l")
    print(f"Celkové náklady : {celkove_naklady:.2f} Kč")
    print(f"Celková cena všech jízd: {celkova_cena_jizd:.2f} Kč")
    print(f"Celkový zisk po odečtení paliva: {celkovy_zisk:.2f} Kč")



                
def spocitej_tkm(kilometry, hmotnost):
    return kilometry * hmotnost



def spocitej_cenu_jizdy(jizda):
    return jizda["kilometry"] * jizda["sazba_za_km"]  


def spocitej_naklady_na_palivo(jizda):
    return jizda["palivo"] * jizda["cena_paliva"]


def spocitej_zisk_po_palivu(jizda):
    cena_jizdy = spocitej_cenu_jizdy(jizda)
    naklady_na_palivo = spocitej_naklady_na_palivo(jizda)

    return cena_jizdy - naklady_na_palivo



def spocitej_spotrebu(jizda):

    return jizda["palivo"] / jizda["kilometry"] * 100


def spocitej_naklad_na_km(jizda):

    return spocitej_naklady_na_palivo(jizda) / jizda["kilometry"]


def spocitej_zisk_na_km(jizda):
    return spocitej_zisk_po_palivu(jizda) / jizda["kilometry"]

def najdi_nejdelsi_jizdu(jizdy):
    if not jizdy:
        return None

    nejdelsi = jizdy[0]

    for jizda in jizdy:
        if jizda["kilometry"] > nejdelsi["kilometry"]:
            nejdelsi = jizda

    return nejdelsi


def najdi_nejvyhodnejsi_jizdu(jizdy):
    if not jizdy:
        return None

    nejvyhodnejsi = jizdy[0]

    for jizda in jizdy:
        zisk_jizdy = spocitej_zisk_po_palivu(jizda)
        zisk_nejvyhodnejsi = spocitej_zisk_po_palivu(nejvyhodnejsi)

        if zisk_jizdy > zisk_nejvyhodnejsi:
            nejvyhodnejsi = jizda

    return nejvyhodnejsi        




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

    sazba_za_km = nacti_kladne_cislo("Sazba za kilometr: ")

    palivo = nacti_kladne_cislo("Kolik litrů nafty bylo tankováno: ")

    cena_paliva = nacti_kladne_cislo("Cena nafty: ")


    jizda = {
        "nakladka": nakladka,
        "vykladka": vykladka,
        "kilometry": kilometry,
        "hmotnost": hmotnost,
        "sazba_za_km": sazba_za_km,
        "palivo": palivo,
        "cena_paliva": cena_paliva,
    }

    jizdy.append(jizda)

#4. VÝPIS JEDNOTLIVÝCH JÍZD
print()
print("         Přehled jízd")
print("================================")

for poradi, jizda in enumerate(jizdy, start=1):


    tkm = spocitej_tkm(jizda["kilometry"], jizda["hmotnost"])

    cena_jizdy = spocitej_cenu_jizdy(jizda)

    naklady_na_palivo = spocitej_naklady_na_palivo(jizda)

    zisk_po_palivu = spocitej_zisk_po_palivu(jizda)

    spotreba = spocitej_spotrebu(jizda)

    naklad_na_km = spocitej_naklad_na_km(jizda)

    zisk_na_km = spocitej_zisk_na_km(jizda)




    print(f"{poradi}. jízda")
    print(f"Trasa: {jizda['nakladka']} " f"====> {jizda['vykladka']}")
    print(f"Kilometry: {jizda['kilometry']:.2f} km")
    print(f"Hmotnost: {jizda['hmotnost']:.2f} t")
    print(f"Dopravní výkon {tkm:.2f} tkm")
    print(f"Cena jízdy: {cena_jizdy:.2f} Kč")
    print(f"Náklady na palivo: {naklady_na_palivo:.2f} Kč")
    print(f"Zisk po odečtení paliva: {zisk_po_palivu:.2f} Kč")
    print(f"Spotřeba: {spotreba:.2f} l/100 km")
    print(f"Naklady na jeden kilometr: {naklad_na_km:.2f} Kč")
    print(f"Zisk na jeden kilometr: {zisk_na_km:.2f} Kč")
    print("------------------------------")


#5. CELKOVÝ SOUHRN


#else:
#    print("Nebyla zadána žádná jízda.")

vypis_souhrn(jizdy) 


nejdelsi_jizda = najdi_nejdelsi_jizdu(jizdy)

if nejdelsi_jizda is not None:
    print()
    print("       Nejdelší jízda")
    print("==============================")
    print(f"Trasa: {nejdelsi_jizda['nakladka']} "
          f"===> {nejdelsi_jizda['vykladka']}")
    print(f"Kilometry: "f"{nejdelsi_jizda['kilometry']:.2f} km")



nejvyhodnejsi_jizda = najdi_nejvyhodnejsi_jizdu(jizdy)

if nejvyhodnejsi_jizda is not None:
    zisk = spocitej_zisk_po_palivu(nejvyhodnejsi_jizda)


    print()
    print("    Nejvýhodnější jízda")
    print("============================")
    print(f"Trasa: {nejvyhodnejsi_jizda['nakladka']} " f"====> {nejvyhodnejsi_jizda['vykladka']}")
    print(f"Zisk po odečtení paliva: {zisk:.2f} Kč")

uloz_jizdy(jizdy)    
          

