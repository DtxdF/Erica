# -*- coding: utf-8 -*- 

# Creado por Prudence Suspect


import sys
import time
import hashlib
import argparse
from os import system as s


# password_md5 = (input("\033[1;39m[\033[1;31m-\033[1;39m] Ingrese hash de password:\033[0;39m ")).strip()


def banner():

	cartel = """\033[0;36m


  ▓█████  ██▀███   ██▓ ▄████▄   ▄▄▄          ▄████▄   ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀ 
  ▓█   ▀ ▓██ ▒ ██▒▓██▒▒██▀ ▀█  ▒████▄       ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ 
  ▒███   ▓██ ░▄█ ▒▒██▒▒▓█    ▄ ▒██  ▀█▄     ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░  
  ▒▓█  ▄ ▒██▀▀█▄  ░██░▒▓▓▄ ▄██▒░██▄▄▄▄██    ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
  ░▒████▒░██▓ ▒██▒░██░▒ ▓███▀ ░ ▓█   ▓██▒   ▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
  ░░ ▒░ ░░ ▒▓ ░▒▓░░▓  ░ ░▒ ▒  ░ ▒▒   ▓▒█░   ░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
   ░ ░  ░  ░▒ ░ ▒░ ▒ ░  ░  ▒     ▒   ▒▒ ░     ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
     ░     ░░   ░  ▒ ░░          ░   ▒      ░          ░░   ░   ░   ▒   ░        ░ ░░ ░ 
     ░  ░   ░      ░  ░ ░            ░  ░   ░ ░         ░           ░  ░░ ░      ░  ░   
                      ░                     ░                           ░              

                      		\033[1;33mCreated by: Prudence Suspect


	"""

	print(cartel)


def cracking_hash(password_hash,password_file):

	time_start = time.time()

	word_crack = []
	words = open(password_file, "rb")

	for word in words.readlines():
		hashed = hashlib.md5(word.strip())
		word_hash = str(hashed.hexdigest())

		if(password_hash==word_hash):
			s('clear')
			banner()
			print("\033[0;39m\n\n [\033[0;33m+\033[0;39m] Password encontrada: \033[1;36m" + str(word.decode()) + "\n\n")
			word_crack.append(word)
			break
		else:
			s('clear')
			banner()
			print("\033[1;33m Probando:  \033[0;32m" + str(word.decode()).strip() + " \033[0;32m " + word_hash)
			#time.sleep(0.005)

	if(word_crack==[]):
		s('clear')
		banner()
		print("\033[0;39m\n\n [\033[0;31mx\033[0;39m] No se pudo crackear la password\n\n")

	words.close()

	time_end = time.time()

	final_time = (time_end - time_start) / 60

	print(" \033[0;37mTiempo transcurrido: {} minutos\n\n".format(round(final_time)))



banner()
parser = argparse.ArgumentParser(description="Programa para crackear passwords mediante MD5")
parser.add_argument('-p', '--hash', help="Password Hash MD5", required=True, type=str)
parser.add_argument('-m', '--mode', help="Elegir metodo de crackeo: wordlist, bruteforce.", required=True, type=str)
parser.add_argument('-f', '--file', help="Elegir ruta de archivo de claves", required=True, type=str)
argv = parser.parse_args()

if(len(argv.hash)==32 and argv.mode=="wordlist" and argv.file):
	cracking_hash(argv.hash,argv.file)
else:
	print("[\033[1;31m+\033[0;39m] Dato erroneo")