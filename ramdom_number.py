import random
from rich.console import Console

# Inicializar la consola Rich
console = Console()

def jugar():
    # Generar el número secreto
    numero_secreto = random.randint(1, 100)
    
    # Inicializar listas para las suposiciones
    suposiciones_jugador = []
    suposiciones_ordenador = []
    
    console.print("¡Bienvenido al juego de Adivina el Número!", style="bold green")
    console.print("Estoy pensando en un número entre 1 y 100. ¡Intenta adivinarlo!", style="dim")
    
    while True:
        # Suposición del jugador
        while True:
            try:
                suposicion_jugador = int(input("Tu suposición: "))
                if 1 <= suposicion_jugador <= 100:
                    break
                else:
                    console.print("Por favor, ingresa un número entre 1 y 100.", style="bold red")
            except ValueError:
                console.print("Entrada no válida. Por favor ingresa un número entero.", style="bold red")
        
        suposiciones_jugador.append(suposicion_jugador)
        
        if suposicion_jugador == numero_secreto:
            console.print(f"¡Felicidades! Adivinaste el número {numero_secreto}.", style="bold green")
            break
        elif suposicion_jugador < numero_secreto:
            console.print("El número secreto es mayor. Intenta de nuevo.", style="bold yellow")
        else:
            console.print("El número secreto es menor. Intenta de nuevo.", style="bold yellow")
        
        # Suposición del ordenador
        suposicion_ordenador = random.randint(1, 100)
        suposiciones_ordenador.append(suposicion_ordenador)
        console.print(f"El ordenador adivina: {suposicion_ordenador}")
        
        if suposicion_ordenador == numero_secreto:
            console.print(f"El ordenador ha adivinado el número {numero_secreto}.", style="bold red")
            break
    
    # Mostrar todas las suposiciones
    console.print("\nResumen del juego:", style="bold blue")
    console.print(f"Suposiciones del jugador: {', '.join(map(str, suposiciones_jugador))}", style="dim")
    console.print(f"Suposiciones del ordenador: {', '.join(map(str, suposiciones_ordenador))}", style="dim")

def main():
    while True:
        jugar()
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").strip().lower()
        if jugar_de_nuevo != 's':
            console.print("¡Gracias por jugar! Hasta luego.", style="bold green")
            break

if __name__ == "__main__":
    main()
