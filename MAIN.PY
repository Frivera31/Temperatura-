def obtener_temperaturas():
    """Solicita al usuario que ingrese las temperaturas de 7 días y las valida."""
    temperaturas = []
    for i in range(7):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {i + 1} (°C): "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Error: Por favor, ingrese un número real válido.")
    return temperaturas

def calcular_promedio(lista):
    """Calcula el promedio de una lista de temperaturas."""
    return sum(lista) / len(lista)

def encontrar_max_min(lista):
    """Encuentra la temperatura máxima y mínima y sus respectivos días."""
    max_temp = max(lista)
    min_temp = min(lista)
    max_dia = lista.index(max_temp) + 1
    min_dia = lista.index(min_temp) + 1
    return (max_temp, max_dia, min_temp, min_dia)

def mostrar_alertas(lista):
    """Genera alertas si hay temperaturas extremas."""
    alertas = []
    for i, temp in enumerate(lista):
        if temp > 40:
            alertas.append(f"Alerta: Día {i + 1} - Temperatura de {temp}°C supera los 40°C.")
        elif temp < 0:
            alertas.append(f"Alerta: Día {i + 1} - Temperatura de {temp}°C está por debajo de 0°C.")
    return alertas

def main():
    """Función principal que coordina la ejecución del programa."""
    print("Bienvenido al sistema de registro de temperaturas.")
    
    # Obtener temperaturas
    temperaturas = obtener_temperaturas()
    
    # Encontrar max y min
    max_temp, max_dia, min_temp, min_dia = encontrar_max_min(temperaturas)
    
    # Calcular promedio
    promedio = calcular_promedio(temperaturas)
    
    # Mostrar resultados
    print("\nResultados:")
    print(f"La temperatura máxima fue de {max_temp}°C en el día {max_dia}.")
    print(f"La temperatura mínima fue de {min_temp}°C en el día {min_dia}.")
    print(f"El promedio semanal de temperaturas es de {promedio:.2f}°C.")
    
    # Días por encima del promedio
    print("Días con temperaturas por encima del promedio:")
    dias_por_encima = [i + 1 for i, temp in enumerate(temperaturas) if temp > promedio]
    if dias_por_encima:
        for dia in dias_por_encima:
            print(f"Día {dia}: {temperaturas[dia - 1]}°C")
    else:
        print("No hubo días con temperaturas por encima del promedio.")
    
    # Mostrar alertas
    alertas = mostrar_alertas(temperaturas)
    if alertas:
        print("\nAlertas:")
        for alerta in alertas:
            print(alerta)
    else:
        print("No hay alertas de temperatura.")

if __name__ == "__main__":
    main()