import random

fichier = open("Questions.txt", "r")
output = open("db.json", "a")

txt = fichier.read()
list_type = txt.split("###\n")

idq = 1
idc = 1

output.write("[\n")
for x in range(len(list_type)):
	group = list_type[x]
	group = group.split("\n")
	for y in group:
		if y != '':
			json = {}
			parts = y.split(" ? ")
			json['text'] = parts[0] + "?"
			json['id'] = "q" + str(idq)
			json['type'] = x
			json['images'] = []
			json['video'] = "null"
			json['status'] = random.randint(0, 2)
			answers = parts[1]
			json['answers'] = answers.split(" / ")
			json['creatorID'] = "c" + str(idc)
			output.write(str(json) + ',\n')

			if random.randint(0,1) == 0:
				idc += 1
			idq += 1
output.write("]")
fichier.close()
output.close()
