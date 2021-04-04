def aproximacion():
    objetivo = int(input("Escoge un numero: "))
    epsilon = 0.02
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2-objetivo ) >= epsilon and respuesta <=objetivo:
        print(respuesta**2, respuesta**2-objetivo, respuesta)
        respuesta += paso
    if abs(respuesta**2-objetivo)>=epsilon:
        print(f"{objetivo} no tiene raiz cuadrada")
    else:
        print(f"la raiz cuadrada de {objetivo} es {respuesta}")


def run():
    aproximacion()


if __name__=="__main__":
    run()