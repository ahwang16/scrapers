# record_processor.py

import re

read = open("record.txt", "r")
write = open("sites.txt", "w")

for line in read.readlines() :
	if "http://" in line :
		write.write(str(re.search(r"https?://\w*\.?([a-zA-Z0-9])\.", line)))


read.close()
write.close()
