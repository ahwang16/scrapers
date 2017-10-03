# Processes saved files of Reddit threads and counts for links to external
# webpages

import re

f = input("Highest file number ")

record = open("record.txt", "w") 

x = 0

while (x < f) :
	infile = open(str(x) + ".txt", "r")

	content = infile.read()

	split = re.split(" ", content)

	count = 0
	websites = []
	for word in split :
		if "http" in word and "reddit" not in word :
			count += 1
			websites.append(word)

	infile.close()

	if count > 0 :
		record.write(str(count) + " websites referenced in " + str(x) + ".txt.\n")
		for site in websites : 
			record.write(site + "\n")



	# webnames = []
	# for site in websites :
	# 	m = re.match("\w+:\/\/(w{3})?\.?(\w+)\.\S+", str(site))
	# 	name = m.group(1)
	# 	webnames.append(name)
	# print webnames

	x += 1

record.close()

