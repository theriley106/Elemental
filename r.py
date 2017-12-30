
def getAllInfo(element):
	for val in json.load(open('elements.json'))['elements']:
		if val['name'] == element.title():
			return val

def genHipResponse(element):
	response = ""
	response = response + genIntro(element)
	response = response + genAtomicMass(element)
	return response
	
def genIntro(element):
	response = ""
	randomNumber = random.randint(1, 3)
	if randomNumber == 1:
		response = response + "Ah, you asked me about {}.  ".format(element)
	elif randomNumber == 2:
		response = response + "Oh, {}.  One of my favorites.  ".format(element)
	elif randomNumber == 3:
		response = response + "{}.  One of the most awesome elements in the periodic table.  ".format(element)
	return response

def genAtomicMass(element):
	response = ""
	randomNumber = random.randint(1, 3)
	color = getAllInfo[element]["appearance"]
	if randomNumber == 1:
		response = "{} actually looks {}.  ".format(element, color)
	if randomNumber == 2:
		response = "{} looks kind of like a {}.  ".format(element, color)
	if randomNumber == 3:
		response = "If you looked at {} you would see a {}.  ".format(element, color)
	return response

