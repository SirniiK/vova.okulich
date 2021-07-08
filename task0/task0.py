from random import randint

spisok = []
for i in range(30):
    spisok.append(randint(-100, 100))
print (spisok)
max = spisok[0] 
for i in spisok:
  if i>max:
    max=i
		
index = spisok.index(max)
print ("Max number in list:", max, "Index: ", index)
for i in range(len(spisok)):
	if i < len(spisok)-1:
		if spisok[i] < 0 and spisok[i+1] < 0:
			print(spisok[i],spisok[i+1])
