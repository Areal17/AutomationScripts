import re
# TODO: Test schreiben für beide Funktionen
camel_cased_names = ["firstFile.txt", "adressFile.txt", "bugReport.txt"]


def camel_to_snake(camel_cased_names):
	snake_cased_names = []
	pattern = r"[A-Z]"
	for name in camel_cased_names:
		founded_group = re.search(pattern, name)
		if founded_group is not None:
			new_char = "_" + str(founded_group.group()).lower()
			new_name = name.replace(founded_group.group(), new_char)
			snake_cased_names.append(new_name)
	return snake_cased_names
	

def snake_to_camel(snake_case_names):
	camle_case_names = []
	pattern = r"_[\w]"
	for name in snake_case_names:
		# TODO: founded_group in foundedGroup umbenennen
		founded_group = re.search(pattern,name)
		new_char = str(founded_group.group()).replace("_","").upper()
		new_name = name.replace(founded_group.group(),new_char)
		camle_case_names.append(new_name)
	return camle_case_names
	
snakes = camel_to_snake(camel_cased_names)
camels = snake_to_camel(snakes)

# print(snakes)
# print(camels)
