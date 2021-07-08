import re
# оголошення масивів
spisokn = []
spisokw = []
# рядок на вході (можна змінити в самому коді)
Input = "Hel112o, wor24ld o0f pyt73hon1".split()
# цикл для обробки цифр
for elem in Input:
	spisokn.extend(re.findall('(\d+)', elem))
# цикл для обробки слів
for elem in Input:
	spisokw.append("".join(re.findall('(\D+)', elem)))

for i in range(len(spisokn)):
	spisokn[i] = int(spisokn[i])
# цикл для піднесення по степеню 
for i in range(len(spisokn)):
	if spisokn[i] != max(spisokn):
		print(pow(spisokn[i], i))
print(spisokn)
# цикл для 'HellO' (перша і остання буква великі)
for i in range(len(spisokw)):
	spisokw[i] = spisokw[i].title()[0:-1]+spisokw[i][-1].upper()
print(" ".join(spisokw))
