def calcular_billetes(monto):
    total = 0

    print(f"\nMonto: ${monto}")

    # Billetes de 500
    b500 = monto // 500
    monto = monto - (b500 * 500)
    total += b500
    print(f"Billetes de $500: {b500}")

    # Billetes de 200
    b200 = monto // 200
    monto = monto - (b200 * 200)
    total += b200
    print(f"Billetes de $200: {b200}")

    # Billetes de 100
    b100 = monto // 100
    monto = monto - (b100 * 100)
    total += b100
    print(f"Billetes de $100: {b100}")

    # Billetes de 50
    b50 = monto // 50
    monto = monto - (b50 * 50)
    total += b50
    print(f"Billetes de $50: {b50}")

    print(f"Total de billetes: {total}")
    print("-" * 30)


# 🔹 Programa principal
while True:
    entrada = input("Ingresa un monto (o escribe 'salir'): ")

    if entrada.lower() == "salir":
        print("Programa terminado.")
        break

    if entrada.isdigit():
        monto = int(entrada)
        calcular_billetes(monto)
    else:
        print("Por favor ingresa un número válido.")