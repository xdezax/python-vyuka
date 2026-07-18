#funkce


def secti(a, b):
    print(a+b)

secti(5, 8)
secti(100, 350)


def secti1(a, b):
    return (a + b)


vysledek = secti1(5, 8)

print(f"Součet je {vysledek}")
print(f"Dvojnásobek výsledku je {vysledek * 2}")
 

#seznamy

jizdy_km = [] 

jizdy_km.append(520)
jizdy_km.append(680)
jizdy_km.append(430)

print(jizdy_km)

for kilometry in jizdy_km:
    print(f"Jízda měla {kilometry} km")