def contLletra(nomFitxer):
    lletresAnts = {}
    with open(nomFitxer, "r") as fitxer:
        for linia in fitxer:
            for lletra in linia:
                if lletra.isalpha():
                    lletra = lletra.lower()
                    if lletra in lletresAnts:
                        lletresAnts[lletra] += 1
                    else:
                        lletresAnts[lletra] = 1

    for lletra, cont in sorted(lletresAnts.items()):
        print(f"La letra: {lletra} se ha repetido: {cont}")

def contpalabras(nomFitxer):
    simbolos = ['¿','?','.','.',';',':','¡','!']
    numpalabras = 0
    dpalabras = dict()
    with open(nomFitxer,'r') as fichero:
        for linea in fichero:
            for simbolo in simbolos:
                linea = linea.replace(simbolo,' ')
            palabras = linea.split()
            for palabra in palabras:
                numpalabras += 1
                dpalabras[palabra] = dpalabras.get(palabra , 0) + 1
    print('El texto contiene %s palabras' %numpalabras)
    print('Las palabras se han repetido de la siguiente forma:')
    for palabra in dpalabras:
        veces = 'veces'
        if dpalabras[palabra] == 1:
            veces = 'vez'
        print('La palabra "%s" se ha repetido %s %s' %(palabra, dpalabras[palabra], veces))


while True:
    print("1. Contar las letras")
    print("2. Contar las palabras")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nomFitxer = input("Introduce el nombre del archivo: ")
        contLletra(nomFitxer)
    elif opcion == "2":
        nomFitxer = input("Introduce el nombre del archivo: ")
        contpalabras(nomFitxer)
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
