def run():
    # target = int(input("Escoge un numero: "))
    # epsilon = 0.01
    # bajo = 0.0
    # alto = max(1.0, target)
    # respuesta = (alto+bajo)/2

    # while abs(respuesta**2 - target) > epsilon:
    #     print(f"alto = {alto}, bajo={bajo}, respuesta={respuesta}")
    #     if respuesta**2<target:
    #         bajo = respuesta
    #     else:
    #         alto = respuesta
        
    #     respuesta = (alto + bajo)/2
    # print(f"alto = {alto}, bajo={bajo}, respuesta={respuesta}")
    # print(f"la raiz cuadrada de {target} es {respuesta}")


    target = int(input("""Bienvenido a raiz cuadrada,
    dime un numero y te devolveré su raiz cuadrada con un margen de error del 1%: """ ))
    epsilon = 0.01
    low = 0.0
    high = max(1.0, target)
    answer = (high+low) / 2

    while abs(answer**2-target)>epsilon:
        print(f"target:{target}, answer:{answer}")
        if answer**2<target:
            low = answer
        else:
            high = answer

        answer = (high + low)/2    
    print(f"target:{target}, answer:{answer}")
    print(f"La raiz cuadrada de {target} es {answer}")


if __name__=="__main__":
    run()