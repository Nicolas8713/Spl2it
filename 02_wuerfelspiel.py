#02_wuerfelspiel.py
anzahl= input("Wie oft soll gewürfelet werden")
anzahl = int(anzahl)
schaetzung= input("Welche zahl gweinnt?")
schaetzung=int(schaetzung)
counter=0
for zahl in range (0,anzahl):
	import random
	random.seed()
	zahl=random.randint(1,6)
	print (zahl)
	
	if (zahl==schaetzung):
		counter=counter +1
		print("Gewonnen!!Die Zahl", schaetzung , "kommt" ,counter, "mal vor")
	else:
		print("Verloren")
		
	

