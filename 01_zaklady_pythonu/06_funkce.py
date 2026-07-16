def pozdrav1():
    print("Ahoj Vašku!")
    print("Vítej v programu Kamioňákův pomocník.")
    print()



def cara():
    print("============================================")


def pozdrav(jmeno):
    print(f"Ahoj {jmeno}!")

def secti():
    a = float(input("Zadej první číslo: "))
    b = float(input("Zadej druhé číslo: "))
    return a + b

vysledek = secti()




cara() 
print("                Výsledek")
cara()


pozdrav("Vašku")
pozdrav("Petře")
pozdrav("Jano")
pozdrav("Kamioňáku")
pozdrav1()
print(f"Součet je {vysledek}")



