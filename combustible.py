def calcular_litros_necesarios(distancia: float, rendimiento: float) -> float:
    if distancia <= 0:
        raise ValueError("La distancia debe ser mayor que cero.\n")
    if rendimiento <= 0:
        raise ValueError("El rendimiento del vehículo debe ser mayor que cero.\n")
    return round(distancia / rendimiento, 2)


def calcular_costo_combustible(litros: float, precio_litro: float) -> float:
    if litros < 0 or precio_litro < 0:
        raise ValueError("Los litros y el precio por litro deben ser valores positivos.\n")
    return round(litros * precio_litro, 2)


def dividir_total(total: float, personas: int) -> float:
    if personas <= 0:
        raise ValueError("El número de personas debe ser mayor que cero.\n")
    return round(total / personas, 2)


def mostrar_resultados(litros: float, total: float, total_persona: float = None) -> None:
    print("\n--- Resultados ---")
    print(f"Litros necesarios: {litros:.2f} L")
    print(f"Costo total del combustible: ${total:.2f}")
    if total_persona is not None:
        print(f"Cada persona paga: ${total_persona:.2f}.\n")