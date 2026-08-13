def pedirNum(msg):
    num = int(input(msg))
    return(num)

def esFibonacci(numero):
    a = 0
    b = 1
    esFib = 0
    while a <= numero:
        if a == numero:
            esFib = 1
        temp = a + b
        a = b
        b = temp
    return(esFib)

def esPrimo(numero):
    primo = 1
    if numero < 2:
        primo = 0
    else:
        i = 2
        while i < numero:
            if numero % i == 0:
                primo = 0
            i = i + 1
    return(primo)

def evaluarNumero(numero):
    if esFibonacci(numero) == 1:
        print("Es un numero FIBONACCI")
    if esPrimo(numero) == 1:
        print("Es un numero primo")
    if numero > 0:
        print("El numero es positivo")
    else:
        if numero < 0:
            print("El numero es negativo")
        else:
            print("El numero es cero")

def calcularIntermedios(num1, num2):
    if num1 < num2:
        inicio = num1
        fin = num2
    else:
        inicio = num2
        fin = num1

    if num1 > 0 and num2 > 0:
        resultado = 0
        i = inicio
        while i <= fin:
            resultado = resultado + i
            i = i + 1
        print("Ambos positivos. La suma de los intermedios (incluyendo inicial y final) es:", resultado)
    else:
        if num1 < 0 and num2 < 0:
            resultado = 1
            i = inicio
            while i <= fin:
                resultado = resultado * i
                i = i + 1
            print("Ambos negativos. La multiplicacion de los intermedios (incluyendo inicial y final) es:", resultado)
        else:
            resultado = 0
            i = inicio
            while i <= fin:
                resultado = resultado + i
                i = i + 1
            print("Uno positivo y uno negativo. La suma de los intermedios (incluyendo inicial y final) es:", resultado)

def intermediosPorDigitos(numero):
    texto = str(numero)
    print("  Analizando parejas de digitos de", numero)
    i = 0
    while i + 1 < len(texto):
        d1 = int(texto[i])
        d2 = int(texto[i + 1])

        if d1 < d2:
            inicio = d1
            fin = d2
        else:
            inicio = d2
            fin = d1

        if d1 > 0 and d2 > 0:
            resultado = 0
            j = inicio
            while j <= fin:
                resultado = resultado + j
                j = j + 1
            print("  Digitos", d1, "y", d2, "-> Ambos positivos. Suma de los intermedios:", resultado)
        else:
            if d1 < 0 and d2 < 0:
                resultado = 1
                j = inicio
                while j <= fin:
                    resultado = resultado * j
                    j = j + 1
                print("  Digitos", d1, "y", d2, "-> Ambos negativos. Multiplicacion de los intermedios:", resultado)
            else:
                resultado = 0
                j = inicio
                while j <= fin:
                    resultado = resultado + j
                    j = j + 1
                print("  Digitos", d1, "y", d2, "-> Suma de los intermedios:", resultado)
        i = i + 2

    if i < len(texto):
        print("  Digito sobrante sin pareja:", texto[i])

def esVocal(letra):
    vocal = 0
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        vocal = 1
    return(vocal)

def posicionAbecedario(letra):
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    posicion = 0
    i = 0
    while i < len(abecedario):
        if abecedario[i] == letra:
            posicion = i + 1
        i = i + 1
    return(posicion)

def analizarPalabra(palabra):
    i = 0
    while i < len(palabra):
        letra = palabra[i]
        if esVocal(letra) == 1:
            print("La letra", letra, "es VOCAL y ocupa la posicion", posicionAbecedario(letra), "en el abecedario")
        else:
            print("La letra", letra, "es CONSONANTE y ocupa la posicion", posicionAbecedario(letra), "en el abecedario")
        i = i + 1

def main():
    numero1 = pedirNum("Ingrese el primer numero: ")
    numero2 = pedirNum("Ingrese el segundo numero: ")

    print("--- Resultados numero1 ---")
    evaluarNumero(numero1)

    print("--- Resultados numero2 ---")
    evaluarNumero(numero2)

    calcularIntermedios(numero1, numero2)

    print("")
    codigo = pedirNum("Ingrese su codigo de estudiante: ")
    print("--- Resultados codigo de estudiante ---")
    evaluarNumero(codigo)
    intermediosPorDigitos(codigo)

    print("")
    fecha = input("Ingrese su fecha de nacimiento (ej: 24 octubre 2008): ")
    partes = fecha.split()
    dia = int(partes[0])
    mes = partes[1]
    anio = int(partes[2])

    print("--- Resultados dia (", dia, ") ---")
    evaluarNumero(dia)
    intermediosPorDigitos(dia)

    print("--- Resultados anio (", anio, ") ---")
    evaluarNumero(anio)
    intermediosPorDigitos(anio)

    calcularIntermedios(dia, anio)

    print("")
    print("=== ANALISIS DEL MES:", mes, "===")
    analizarPalabra(mes)

main()
