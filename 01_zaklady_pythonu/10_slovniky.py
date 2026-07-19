jizda = {}

jizda["nakladka"] = input("Místo nakládky: ")
jizda["vykladka"] = input("Místo vykládky: ")
jizda["kilometry"] = float(input("Počet kilometrů: ").replace(",", "."))
jizda["hmotnost"] = float(input("Hmotnost nákladu v tunách: ").replace(",","."))

tkm = jizda["kilometry"] * jizda["hmotnost"]

print()
print("    Přehled jízd")
print("======================")
print(f"Nakládka: {jizda['nakladka']}")
print(f"Vykládka: {jizda['vykladka']}")
print(f"Kilometry: {jizda['kilometry']:.2f} km")
print(f"Hmotnost: {jizda['hmotnost']:.2f} t")
print(f"Dopravní výkon: {tkm:.2f} tkm")