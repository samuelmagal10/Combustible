from combustible import (
    calcular_litros_necesarios,
    calcular_costo_combustible,
    dividir_total,
    mostrar_resultados
)

def main():
    while True:
        try:
            distancia = float(input("Ingrese la distancia total del viaje (en km): "))
            rendimiento = float(input("Ingrese el rendimiento del vehículo (km/l): "))
            precio_litro = float(input("Ingrese el precio del litro de gasolina: $"))

            litros = calcular_litros_necesarios(distancia, rendimiento)
            total = calcular_costo_combustible(litros, precio_litro)

            dividir = input("¿Desea dividir el costo entre varias personas? (sipirili/noporolo): ").strip().lower()
            total_por_persona = None

            if dividir == 's':
                personas = int(input("¿Entre cuántas personas se dividirá el total? "))
                total_por_persona = dividir_total(total, personas)

            mostrar_resultados(litros, total, total_por_persona)

        except ValueError as ve:
            print(f"Error: {ve}.'n")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}\n")

        seguir = input("\n¿Desea hacer otro cálculo? (1 = Sí / 2 = No): ").strip()
        if seguir != '1':
            print("Gracias hola mundo.\n")
            break

if __name__ == "__main__":
    main()