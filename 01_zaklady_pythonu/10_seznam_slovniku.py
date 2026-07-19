jizdy = []

while True:
    nakladka = input("Místo nakládky nebo konec: ").strip()

    if nakladka.lower() == "konec":
        break

    vykladka = input("Místo vykládky: ").strip()

    try:
        kilometry = float(input("Počet kilometrů: ").replace(",", "."))

        hmotnost = float(input("Hmotnost nákladu v tunách: ").replace(",", "."))

        if kilometry <= 0 or hmotnost <= 0:
            print("Kilometry i hmotnost musí být větší než nula.")
            continue

    except ValueError:
        print("Zadej platná čísla.")
        continue    

    jizda = {
        "nakladka": nakladka,
        "vykladka": vykladka,
        "kilometry": kilometry,
        "hmotnost": hmotnost,
        
    }

    jizdy.append(jizda)


print()
print("    Výpis jízd")
print("=====================")

for poradi, jizda in enumerate(jizdy, start=1):
    tkm = jizda["kilometry"] * jizda["hmotnost"]

    print(f"{poradi}. jízda")
    print(f"Trasa: {jizda['nakladka']} <===> {jizda['vykladka']}")
    print(f"Kilometry: {jizda['kilometry']:.2f} km")
    print(f"Hmotnost: {jizda['hmotnost']:.2f} t")
    print(f"              Dopravní výkon: {tkm:.2f} tkm")
    print("__________________________________________________")


if jizdy:
    celkem_km = 0
    celkem_tkm = 0

    for jizda in jizdy:
        celkem_km += jizda["kilometry"]
        celkem_tkm += jizda["kilometry"] * jizda["hmotnost"]

    print(f"Celkem kilometrů: {celkem_km:.2f} km")
    print(f"Celkový dopravní výkon: {celkem_tkm:.2f} tkm")
    print(f"Počet jízd: {len(jizdy)}")

else:
    print("Nebyla zadána žádná jízda.")
