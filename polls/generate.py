import random
import json

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
			json_dict = {}
			parts = y.split(" ? ")
			json_dict['text'] = parts[0] + "?"
			json_dict['id'] = "q" + str(idq)
			json_dict['type'] = x
			json_dict['images'] = []
			json_dict['video'] = "null"
			json_dict['status'] = random.randint(0, 2)
			answers = parts[1]
			json_dict['answers'] = answers.split(" / ")
			json_dict['creatorID'] = "c" + str(idc)
			output.write(json.dumps(json_dict) + ',\n')

			if random.randint(0,1) == 0:
				idc += 1
			idq += 1
output.write("]")
fichier.close()
output.close()
