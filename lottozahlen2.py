#lottozahlen2.py

import random
random.seed()
tipp =input("Bitte geben sie die Zahlen ein")
tipps =tipp.split(", ")
tipps =[int(i) for i in tipps]
tipps.sort()
lottogezogen=[]
counter=0
while tipps!=lottogezogen:
	lottogezogen=[]
	lottozahlen = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
	for i in range (1,7):
		i = random.randint(0, len(lottozahlen)-1)
		x = lottozahlen.pop(i)
		lottogezogen.append(x)
	lottogezogen.sort()
	print (lottogezogen)
	if (lottogezogen!=tipps):
		counter=counter+1
	if(lottogezogen==tipps):
		print("Es hat",counter,"durchläufe gebraucht")
		break

	

print(lottogezogen)