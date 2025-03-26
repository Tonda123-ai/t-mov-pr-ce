opakovat = "ano"

while(opakovat=="ano"):
    cislo1 = float(input("Zadejte první číslo: "))
    cislo2 = float(input("zadejte druhé číslo:"))
    print("Jakou početní operaci chcete použít?")
    print("součet")
    print("rozdíl")
    print("součin")
    print("podíl")
    operace = input()
    if operace == "součet":
        soucet = cislo1 + cislo2
        print(f"součet: {soucet}")
    if operace == "rozdíl":
        rozdil = cislo1 - cislo2
        print(f"rozdíl: {rozdil}")
    if operace == "součin":
        soucin = cislo1 * cislo2
        print(f"součin: {soucin}")
    if operace == "podíl":
        podil = cislo1 / cislo2
        print(f"podíl: {podil}")
    opakovat = input("CHcete pokračovat? ano nebo ne ")
