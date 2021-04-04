def calculo_raiz(n_usuario):
    respuesta = 0
    while respuesta**2 < n_usuario:
        respuesta += 1
    if respuesta**2 == n_usuario:
        print(f"la raiz cuadrada de {n_usuario} es: {respuesta}")
    else:
        print(f"{n_usuario} no tiene raiz cuadrada")



def run():
    n_usuario = int(input("""Voy a decirte si tu numero tiene raiz cuadrada
Elige un numero entero:  """))
    calculo_raiz(n_usuario)


if __name__=="__main__":
    run()