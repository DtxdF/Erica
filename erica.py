#!/usr/bin/env python3

import signal
import argparse
import sys
import multiprocessing

from inspect import isgenerator, isbuiltin
from os import name as whoami
from os.path import isfile
from _io import TextIOWrapper
from hashlib import algorithms_available
from hashlib import (
                        md5,
                        # Sha family
                        sha1,
                        sha224,
                        sha256,
                        sha384,
                        sha512,
                        # Sha-3 family
                        sha3_224,
                        sha3_256,
                        sha3_384,
                        sha3_512,
                        # shake family
                        shake_128,
                        shake_256,
                        # Blake family
                        blake2b,
                        blake2s

                        )

class HashNotFound(Exception):
    """Llamado cuando el hash no existe"""

class colors(object):
    if (whoami != 'nt'):
        GREEN = '\033[1;32m'
        RED = '\033[1;31m'
        BLUE = '\033[1;34m'
        YELLOW = '\033[1;33m'
        CYAN = '\033[1;36m'
        WHITE = '\033[0;37m'
        RESET = '\033[0m'

    else:
        import colorama
        colorama.init()

        GREEN = colorama.Fore.GREEN
        RED = colorama.Fore.RED
        BLUE = colorama.Fore.BLUE
        YELLOW = colorama.Fore.YELLOW
        CYAN = colorama.Fore.CYAN
        WHITE = colorama.Fore.WHITE
        RESET = colorama.Style.RESET_ALL

def printI(string):
    print('{}[{}*{}] - '.format(
        colors.WHITE, colors.BLUE, colors.WHITE), string, flush=True)
    print(colors.RESET, flush=True, end='')

def printS(string):
    print('{}[{}*{}] - '.format(
        colors.WHITE, colors.GREEN, colors.WHITE), string, flush=True)
    print(colors.RESET, flush=True, end='')

def printE(string):
    print('{}[{}-{}] - '.format(
        colors.WHITE, colors.RED, colors.WHITE), string, flush=True)
    print(colors.RESET, flush=True, end='')

def protect(signum, frame):
    sys.exit(0)

def banner():
    print(colors.CYAN, '''
  ▓█████  ██▀███   ██▓ ▄████▄   ▄▄▄      
  ▓█   ▀ ▓██ ▒ ██▒▓██▒▒██▀ ▀█  ▒████▄    
  ▒███   ▓██ ░▄█ ▒▒██▒▒▓█    ▄ ▒██  ▀█▄  
  ▒▓█  ▄ ▒██▀▀█▄  ░██░▒▓▓▄ ▄██▒░██▄▄▄▄██ 
  ░▒████▒░██▓ ▒██▒░██░▒ ▓███▀ ░ ▓█   ▓██▒
  ░░ ▒░ ░░ ▒▓ ░▒▓░░▓  ░ ░▒ ▒  ░ ▒▒   ▓▒█░
   ░ ░  ░  ░▒ ░ ▒░ ▒ ░  ░  ▒     ▒   ▒▒ ░
     ░     ░░   ░  ▒ ░░          ░   ▒   
     ░  ░   ░      ░  ░ ░            ░  ░

''', colors.YELLOW, 'Created by: Kirari\n', colors.RESET)

def crack(args):
    (password_hash, wordfile, hash_func, longcode) = args

    with open(wordfile, 'rt') as wordlist:
        if not (isinstance(wordlist, list)) \
                and not (isgenerator(wordlist)) \
                and not (isinstance(wordlist, TextIOWrapper)):
            raise TypeError('El tipo de dato de la lista de hashes no es correcto')

        if not (hash_func in algorithms_available):
            raise HashNotFound('El hash no existe')

        else:
            hash_ = globals()[hash_func]
            if not (isbuiltin(hash_)) and not (isinstance(hash_, type)):
                raise ValueError('{}, no es un dato correcto para ser una función hash'.format(hash_func))

        for _ in wordlist:
            _ = _.strip()
            string_to_hash = hash_(_.encode())
            string_to_hash = string_to_hash.hexdigest(longcode) \
                    if (hash_func.startswith('shake_')) else string_to_hash.hexdigest()

            printI('Probando -> {}{} {}?= {}{}: {}{}'.format(
                colors.YELLOW, string_to_hash, colors.BLUE, 
                colors.YELLOW, password_hash, colors.GREEN, _))

            if (string_to_hash == password_hash):
                printS('Crackeado -> {} = {}'.format(
                    _, string_to_hash))
                return(True)

        printE('No hubo resultados satisfactorios...', flush=True)
        return(False)

def main():
    banner()

    DEFAULT_LONG = 2
    DEFAULT_PROCESS = 2

    parser = argparse.ArgumentParser()
    parser.description = 'Erica es una herramienta que te permitra crackear muchas familias de algoritmos con sus respectivas versiones. Entre los cuales se encuentran: MD5, SHA (1, 224, 256, 384, 512), SHA-3 (224, 256, 384, 512), shake (128, 256), blake2b & blake2s.'
    parser._optionals.description = 'Opcionales'
    parser._actions[0].help = 'Mostrar la ayuda y salir'

    parser.add_argument('-l', '--long', help='Para el caso de la familia "shake" se debe colocar explicitamente la longitud. Pre-determinado: {}'.format(DEFAULT_LONG), type=int, default=DEFAULT_LONG)
    parser.add_argument('-p', '--process', help='Número de procesos en paralelo. ADVERTENCIA: Por favor hagalo bajo su propio cuidado. Pre-determinado: {}'.format(DEFAULT_PROCESS), type=int, default=DEFAULT_PROCESS)

    primary = parser.add_argument_group('Argumentos principales')
    primary.add_argument('-H', '--hash', help='El hash para crackear', required=True)
    primary.add_argument('-a', '--algorithm', help='El algoritmo a utilizar', required=True)
    primary.add_argument('-w', '--wordlist', help='La ruta del diccionario a utilizar', required=True)

    args = parser.parse_args()

    if not (isfile(args.wordlist)):
        printE('¡El diccionario no existe!')
        sys.exit(1)

    try:
        pool = multiprocessing.Pool(args.process)
        pool.map(crack, [(args.hash, args.wordlist,
                args.algorithm, args.long)])

    except Exception as Except:
        printE('Error: {}'.format(Except))
        sys.exit(1)

if __name__ == '__main__':
    signals = [
            
                signal.SIGINT,
                signal.SIGTERM
                ]

    if (whoami != 'nt'):
        signals.extend([
            
            signal.SIGQUIT,
            signal.SIGUSR1,
            signal.SIGUSR2
            
        ])

    for _ in signals:
        signal.signal(_, protect)

    main()
