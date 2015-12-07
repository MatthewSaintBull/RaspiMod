########################################################################
#Modulo personalizzato per l'utilizzo delle gpio                       #
#di raspberry, in quanto il modulo rpio.gpio non                       #
#lo trovavo molto efficace.                                            #
#Il seguente modulo utilizzera' il subprocess , andando cosi           #
#a richiamare una nuova shell per il controllo delle                   #
#directory '/sys/devices/gpio' e compagnia bella                       #
#controllando cosi' i pin gpio del raspberry senza dover               #
#andare a sbattere la testa sulle relative directory                   #
#per utilizzarlo basta lanciare lo script da root con il comando sudo  #
########################################################################

import subprocess
import os  
import sys  
  
"""if not os.access('/', os.W_OK):  
    sys.stderr.write('This program requires permission to write in the root directory.\n')  
    sys.exit(1)  """
    

class rpio:
	def __init__(pin,n,v):
		#sudo sh -c 'echo 27 > /sys/class/gpio/export' <--- crea la cartella col relativo gpio
		#sudo sh -c 'echo high > /sys/class/gpio/gpio17/direction' <-- cambia il valore del pin
		#4,17,21,27,22,18,23,24,25 <--- le porte gpio
		pin.numero = n
		pin.valore = v
		cambio = "sudo sh -c 'echo " 
		cambio2 = "> /sys/class/gpio/gpio"
		cambio3 = "/direction'"
		lista = [4,17,18,21,22,23,24,25,27]
		lista_v = ["HIGH","LOW"]
		if pin.numero not in lista:
			print "ERRORE , PIN NON ESISTENTE"
		else : 
			if pin.valore not in lista_v:
				print "ERRORE , NON ESISTE TALE VALORE PER IL PIN"
			else: 
				subprocess.call(cambio + pin.valore + cambio2 + str(pin.numero) + cambio3 ,shell = True)
class create_rpio:
	def __init__(pin,nr):
		pin.numero = nr
		stringa = "sudo sh -c 'echo "
		stringa2 = " > /sys/class/gpio/export'"
		lista = [4,17,18,21,22,23,24,25,27]
		if pin.numero not in lista:
			print "ERRORE , PIN NON ESISTENTE"
		else : 
			subprocess.call(stringa + str(pin.numero) + stringa2 , shell = True)