
import re

spisokn = []
spisokw = []

Input = "Hel112o, wor24ld o0f pyt73hon1".split()
for elem in Input:
	spisokn.extend(re.findall('(\d+)', elem))

for elem in Input:
	spisokw.append("".join(re.findall('(\D+)', elem)))

for i in range(len(spisokn)):
	spisokn[i] = int(spisokn[i])

for i in range(len(spisokn)):
	if spisokn[i] != max(spisokn):
		print(pow(spisokn[i], i))
print(spisokn)

for i in range(len(spisokw)):
	spisokw[i] = spisokw[i].title()[0:-1]+spisokw[i][-1].upper()
print(" ".join(spisokw))
