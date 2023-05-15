import os
import msvcrt
from colorama import Fore, Back, Style

def contLletra(nomFitxer):
    lletresAnts = {}
    numLletra = 0
    with open(noufitxer, 'w') as f:
        f.write('')
        f.close()
    with open(nomFitxer, "r") as fitxer:
        for linia in fitxer:
            for lletra in linia:
                if lletra.isalpha():
                    lletra = lletra.lower()
                    numLletra+=1
                    if lletra in lletresAnts:
                        lletresAnts[lletra] += 1
                    else:
                        lletresAnts[lletra] = 1
    print('\tEl texto contiene %s letras.' %numLletra)
    with open(noufitxer, 'a') as f:
        f.write('El texto contiene %s letras\n' %numLletra)
    for lletra, cont in sorted(lletresAnts.items()):
        with open(noufitxer, 'a') as f:
            f.write(f"La letra: {lletra} se ha repetido: {cont}\n")
        print(f"\tLa letra: {lletra} se ha repetido: {cont}")
    char = msvcrt.getch()

def contpalabras(nomFitxer):
    simbolos = ['¿','?','.','.',';',':','¡','!']
    numpalabras = 0
    dpalabras = dict()
    with open('contpalabras.txt', 'w') as f:
        f.write('')
        f.close()
    with open(nomFitxer,'r') as fichero:
        for linea in fichero:
            for simbolo in simbolos:
                linea = linea.replace(simbolo,' ')
            palabras = linea.split()
            for palabra in palabras:
                numpalabras += 1
                dpalabras[palabra] = dpalabras.get(palabra , 0) + 1
    
    with open(noufitxer, 'a') as f:
                f.write('El texto contiene %s palabras\n' %numpalabras)
    print('\tEl texto contiene %s palabras' %numpalabras)
    print('\tLas palabras se han repetido de la siguiente forma:')
    for palabra in dpalabras:
        veces = 'veces'
        if dpalabras[palabra] == 1:
            veces = 'vez'
        print('\tLa palabra "%s" se ha repetido %s %s' %(palabra, dpalabras[palabra], veces))
        with open(noufitxer, 'a') as f:
                f.write('La palabra "%s" se ha repetido %s %s\n' %(palabra, dpalabras[palabra], veces))
    char = msvcrt.getch()



while True:
    os.system('cls')
    print(Fore.RED + Style.BRIGHT +""" 
                                ,_.
                            ./  |                                          _-
                            ./    |                                       _-'/
        ______.,         ./      /                                     .'  (
    _---'___._.  '----___/       (                                    ./  /`'
    (,----,_  G \                  \_.                               ./   :
    \___   "--_                      "--._,                       ./    /
    /^^^^^-__          ,,,,,               "-._       /|         /     /
    `,       -        /////                    "`--__/ (_,    ,_/    ./
    "-_,           ''''' __,                            `--'      /
        "-_,             \\ `-_                                  (
            "-_.          \\   \.                                 \_
            /    "--__,      \\   \.                       ____.     "-._,
            /        ./ `---____\\   \.______________,---\ (     \,        "-.,
            |       ./             \\   \        /\  |     \|       `--______---`
            |     ./                 \\  \      /_/\_!
            |   ./                     \\ \
        \n            |  /                        
            |_/
    """)

    print(Fore.RED + "")
    print("""      ________  ___  ________           ___       ___  _____ ______   ___  _________  _______   ________           ________  ___  ___  ________  ________  ___  __       
    |\   ____\|\  \|\   ___  \        |\  \     |\  \|\   _ \  _   \|\  \|\___   ___\\  ___ \ |\   ____\         |\   ____\|\  \|\  \|\   __  \|\   __  \|\  \|\  \     
    \ \  \___|\ \  \ \  \\ \  \       \ \  \    \ \  \ \  \\\__\ \  \ \  \|___ \  \_\ \   __/|\ \  \___|_        \ \  \___|\ \  \\\  \ \  \|\  \ \  \|\  \ \  \/  /|_   
     \ \_____  \ \  \ \  \\ \  \       \ \  \    \ \  \ \  \\|__| \  \ \  \   \ \  \ \ \  \_|/_\ \_____  \        \ \_____  \ \   __  \ \   __  \ \   _  _\ \   ___  \  
      \|____|\  \ \  \ \  \\ \  \       \ \  \____\ \  \ \  \    \ \  \ \  \   \ \  \ \ \  \_|\ \|____|\  \        \|____|\  \ \  \ \  \ \  \ \  \ \  \\  \\ \  \\ \  \ 
        ____\_\  \ \__\ \__\\ \__\       \ \_______\ \__\ \__\    \ \__\ \__\   \ \__\ \ \_______\____\_\  \         ____\_\  \ \__\ \__\ \__\ \__\ \__\\ _\\ \__\\ \__\
\n      |\_________\|__|\|__| \|__|        \|_______|\|__|\|__|     \|__|\|__|    \|__|  \|_______|\_________\       |\_________\|__|\|__|\|__|\|__|\|__|\|__|\|__| \|__|
       \|_________|                                                                              \|_________|       \|_________|      """)


    print(Style.RESET_ALL + "\n\n     1. Contar las letras")
    print("     2. Contar las palabras")
    print("     3. Salir")
    opcion = input("     Seleccione una opción: ")

    if opcion == "1":
        nomFitxer = input("\tIntroduce el nombre del archivo: ")
        noufitxer = input("\tIntroduce el nombre del archivo que quieres crear: ")
        contLletra(nomFitxer)
    elif opcion == "2":
        nomFitxer = input("\tIntroduce el nombre del archivo: ")
        noufitxer = input("\tIntroduce el nombre del archivo que quieres crear: ")
        contpalabras(nomFitxer)
    elif opcion == "3":
        break
    else:
        print("\tOpción inválida. Por favor, seleccione una opción válida.")