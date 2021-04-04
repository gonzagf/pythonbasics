def enumeracion_exhaustiva():
    target = int(input("Dime un número: "))
    answer = 0
    while answer**2 != target and answer<target:
        answer += 1
    if answer**2==target:
        print(f"La raiz cuadrada de {target} es {answer}")
    else:
        print(f"{target} no tiene raiz cuadrada exacta")

def aproximacion():
    target = int(input("Dime un número: "))
    epsilon = 0.01
    paso = epsilon**2
    answer = 0.0

    while abs(answer**2-target)>=epsilon and answer<=target:
        answer += paso
    if abs(answer**2-target)>epsilon:
        print(f"{target} no tiene raiz cuadrada")
    else:
        print(f"la raiz cuadrada de {target} es {answer}")


def busqueda_binaria():
    target = int(input("Dime un número: "))
    high = max(target, 1.0)
    low = 0.0
    answer = (high+low)/2
    epsilon = 0.01

    while abs(answer**2 - target)>epsilon:
        if answer**2 < target:
            low = answer
        else:
            high = answer
        answer = (high+low)/2
    answer = round(answer, 2)
    print(f"La raiz cuadrada de {target} es {answer}")

def run():
    chosen_option = int(input(""""Hola! Soy Búsqueda de la raíz cuadrada
    Te voy a ayudar a encontrar la raiz cuadrada del numero que elijas
    Tengo tres formas de realizarlo, elige una:
    1-Enumeración exhaustiva
    2-Aproximacion
    3-Búsqueda binaria
    """))
    if chosen_option==1:
        enumeracion_exhaustiva()
    elif chosen_option == 2:
        aproximacion()
    elif chosen_option==3:
        busqueda_binaria()
    else:
        chosen_option = input("Tienes que elegir un numero: 1, 2 o 3:")

if __name__=="__main__":
    run()