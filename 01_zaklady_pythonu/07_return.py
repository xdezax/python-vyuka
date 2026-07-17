def spocitej_spotrebu(kilometry, litry):
    return  litry / kilometry * 100
    



def spocitej_cenu_paliva(litry, cena_za_litr):
    return litry * cena_za_litr
    




def spocitej_cenu_na_km(cena_paliva, kilometry):
    return cena_paliva / kilometry
   



def spocitej_tkm(kilometry, hmotnost):
    return kilometry * hmotnost



def spocitej_trzbu(tkm, sazba):
    return tkm * sazba



def spocitej_marzi_po_palivu(trzba, cena_paliva):
    return trzba - cena_paliva
    




ujeto = float(input("Kolik kilometrů jsi ujel? "))
natankovano = float(input("Kolik litrů jsi natankoval? "))
cena_nafty = float(input("Kolik stojí litr nafty? "))
hmotnost = float(input("Kolik tun váží náklad? "))
sazba = float(input("Jaká je sazba za jednu tkm? "))

vysledna_spotreba = spocitej_spotrebu(ujeto, natankovano)
cena_tankovani = spocitej_cenu_paliva(natankovano, cena_nafty)
cena_paliva_na_km = spocitej_cenu_na_km(cena_tankovani, ujeto)
tkm = spocitej_tkm(ujeto, hmotnost)
trzba = spocitej_trzbu(tkm, sazba)
marze = spocitej_marzi_po_palivu(trzba, cena_tankovani)
 

print()
print("-----------------------------")
print("          Výsledek")
print("-----------------------------")
print(f"Spotřeba je {vysledna_spotreba:.2f} l/100km")
print(f"Cena tankování je {cena_tankovani:.2f} Kč")
print(f"Cena za ujetý kilometr je {cena_paliva_na_km:.2f} Kč")
print(f"Dopravní výkon je {tkm:.2f} tkm")
print(f"Tržba je {trzba:.2f} Kč")
print(f"Marže po odečtení paliva je {marze:.2f} Kč")
    

