rolls = {
    "Pikachu Roll": 4500,
    "Otaku Roll": 5000,
    "Pulpo Venenoso Roll": 5200,
    "Anguila Eléctrica Roll": 4800
}

def mostrar_menu():
    print("Menu:")
    for i, (roll, precio) in enumerate(rolls.items(), 1):
        print(f"{i}. {roll} - ${precio}")


def tomar_pedido():
    pedido = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione un roll (1-4), o presione 'X' para terminar el pedido: ")
        if opcion.lower() == 'x':
            break
        elif opcion.isdigit() and 1 <= int(opcion) <= 4:
            roll_elegido = list(rolls.keys())[int(opcion) - 1]
            pedido.append(roll_elegido)
        else:
            print("Opción no válida, por favor ingrese un número del 1 al 4 o 'X' para terminar el pedido.")
    return pedido


def aplicar_descuento(total):
    codigo = input("Ingrese el código de descuento (o 'X' para salir): ")
    if codigo.lower() == "soyotaku":
        descuento = total * 0.1
        total -= descuento
        print(f"Descuento aplicado: -${descuento}")
    elif codigo.lower() == "x":
        return None
    else:
        print("Código no válido")
        aplicar_descuento(total)
    return total

def main():
    while True:
        print("\nBienvenido al delivery de Sushi!")
        pedido = tomar_pedido()
        if not pedido:
            print("¡Gracias por su visita!")
            break
        total = sum(rolls[roll] for roll in pedido)
        print("\nDetalle del pedido:")
        for roll in set(pedido):
            cantidad = pedido.count(roll)
            print(f"{cantidad}x {roll}")
        print(f"Total a pagar: ${total}")
        total_con_descuento = aplicar_descuento(total)
        if total_con_descuento is not None:
            print(f"Total a pagar con descuento: ${total_con_descuento}")
        else:
            break
        opcion = input("¿Desea realizar otro pedido? (s/n): ")
        if opcion.lower() != "s":
            print("¡Gracias por su visita!")
            break

if __name__ == "__main__":
    main()