# Erica
Erica es una herramienta para realizar ataques por diccionario contra diferentes familias de algoritmos hash

# Algoritmos Válidos
* MD5
* SHA (1, 224, 256, 384, 512)
* SHA-3 (224, 256, 384, 512)
* shake (128, 256)
* blake2b & blake2s

# Requerimientos
* Python 3.x
* Colorama (Sólo para Windows)

# Modo de ejecución
```bash
python3 ./erica.py -h
 
  ▓█████  ██▀███   ██▓ ▄████▄   ▄▄▄      
  ▓█   ▀ ▓██ ▒ ██▒▓██▒▒██▀ ▀█  ▒████▄    
  ▒███   ▓██ ░▄█ ▒▒██▒▒▓█    ▄ ▒██  ▀█▄  
  ▒▓█  ▄ ▒██▀▀█▄  ░██░▒▓▓▄ ▄██▒░██▄▄▄▄██ 
  ░▒████▒░██▓ ▒██▒░██░▒ ▓███▀ ░ ▓█   ▓██▒
  ░░ ▒░ ░░ ▒▓ ░▒▓░░▓  ░ ░▒ ▒  ░ ▒▒   ▓▒█░
   ░ ░  ░  ░▒ ░ ▒░ ▒ ░  ░  ▒     ▒   ▒▒ ░
     ░     ░░   ░  ▒ ░░          ░   ▒   
     ░  ░   ░      ░  ░ ░            ░  ░

  Created by: Kirari
 
usage: erica.py [-h] [-l LONG] [-p PROCESS] -H HASH -a ALGORITHM -w WORDLIST

Erica es una herramienta que te permitra crackear muchas familias de
algoritmos con sus respectivas versiones. Entre los cuales se encuentran: MD5,
SHA (1, 224, 256, 384, 512), SHA-3 (224, 256, 384, 512), shake (128, 256),
blake2b & blake2s.

optional arguments:
  Opcionales

  -h, --help            Mostrar la ayuda y salir
  -l LONG, --long LONG  Para el caso de la familia "shake" se debe colocar
                        explicitamente la longitud. Pre-determinado: 2
  -p PROCESS, --process PROCESS
                        Número de procesos en paralelo. ADVERTENCIA: Por favor
                        hagalo bajo su propio cuidado. Pre-determinado: 2

Argumentos principales:
  -H HASH, --hash HASH  El hash para crackear
  -a ALGORITHM, --algorithm ALGORITHM
                        El algoritmo a utilizar
  -w WORDLIST, --wordlist WORDLIST
                        La ruta del diccionario a utilizar
```

**Ejemplo:** python3 ./erica.py -H \<hash\> -a \<Algoritmo\> -w \<Ruta del diccionario\>

# Demostración

[![asciicast](https://asciinema.org/a/290526.svg)](https://asciinema.org/a/290526)
