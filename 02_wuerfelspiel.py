#02_wuerfelspiel.py
anzahl= input("Wie oft soll gewürfelet werden")
anzahl = int(anzahl)
schaetzung= input("Welche zahl gweinnt?")
schaetzung=int(schaetzung)
for zahl in range (0,anzahl):
	import random
	random.seed()
	zahl=random.randint(1,6)
	print (zahl)
	counter=0
	if (counter=schaetzng):
		counter+1
		print(counter)
	else:
		print("Verloren")
		
	

