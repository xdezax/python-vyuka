def nacti_kladne_cislo(vyzva):
    while True:
        try:
            text = input(vyzva).replace(",", ".")
            hodnota = float(text)

            if hodnota <= 0:
                print("Zadej číslo větší než nula")
                continue

            return hodnota
        
        except ValueError:
            print("Zadej platné číslo, například 1250 nebo 35,90")




def spocitej_spotrebu(kilometry, litry):
    return  litry / kilometry * 100
    



def spocitej_cenu_paliva(litry, cena_za_litr):
    return litry * cena_za_litr
    




def spocitej_cenu_paliva_na_km(cena_paliva, kilometry):
    return cena_paliva / kilometry
   



def spocitej_tkm(kilometry, hmotnost):
    return kilometry * hmotnost



def spocitej_trzbu(tkm, sazba):
    return tkm * sazba



def spocitej_marzi_po_palivu(trzba, cena_paliva):
    return trzba - cena_paliva
    

while True:
    print()
    print("======================================")
    print("         KAMIOŇÁKŮV POMOCNÍK")
    print("======================================")

    ujeto = nacti_kladne_cislo("Kolik kilometrů jsi ujel? ")
    natankovano = nacti_kladne_cislo("Kolik litrů jsi natankoval? ")
    cena_nafty = nacti_kladne_cislo("Kolik stojí litr nafty? ")
    hmotnost = nacti_kladne_cislo("Kolik tun váží náklad? ")
    sazba = nacti_kladne_cislo("Jaká je sazba za jednu tkm? ")

    vysledna_spotreba = spocitej_spotrebu(ujeto, natankovano)
    cena_tankovani = spocitej_cenu_paliva(natankovano, cena_nafty)
    cena_paliva_na_km = spocitej_cenu_paliva_na_km(cena_tankovani, ujeto)
    tkm = spocitej_tkm(ujeto, hmotnost)
    trzba = spocitej_trzbu(tkm, sazba)
    marze = spocitej_marzi_po_palivu(trzba, cena_tankovani)
 

    print()
    print("-----------------------------")
    print("          Výsledek")
    print("-----------------------------")
    print(f"Spotřeba je {vysledna_spotreba:.2f} l/100 km")
    print(f"Cena tankování je {cena_tankovani:.2f} Kč")
    print(f"Cena paliva na kilometr je {cena_paliva_na_km:.2f} Kč")
    print(f"Dopravní výkon je {tkm:.2f} tkm")
    print(f"Tržba je {trzba:.2f} Kč")
    print(f"Marže po odečtení paliva je {marze:.2f} Kč")

    odpoved = input("\nChceš provést další vypočet? (ano/ne):  ")
    odpoved = odpoved.strip().lower()

    if odpoved != "ano":
        print("Program končí.")
        break
                    

    

