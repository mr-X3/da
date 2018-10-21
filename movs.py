of = open("ratings_tiny.csv","w")
cntr = 0
with open("ratings.csv","r") as f:
	for line in f:
		of.write(line)

		cntr+=1
		if cntr == 500:
			break