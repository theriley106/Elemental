import alexaHelper
import random
import re
import json

ELEMENTLIST = json.load(open('elements.json'))["elements"]

SKILLNAME = "Elemental"
INITIALSPEECH = "Thanks for checking out Elemental!  You can ask me for information on all 118 elements on the Periodic Table"
REPEATSPEECH = "Start by asking, tell me about Helium!"

def lambda_handler(event, context):
	appID = event['session']['application']['applicationId']
	print str(event)
	if event["request"]["type"] == "LaunchRequest":
		return alexaHelper.get_welcome_response(SKILLNAME, INITIALSPEECH, REPEATSPEECH)
	elif event["request"]["type"] == "IntentRequest":
		return on_intent(event["request"], event["session"])
		

def getAllInfo(element):
	for val in json.load(open('elements.json'))['elements']:
		if val['name'] == element.title():
			return val

def genHipResponse(element):
	response = ""
	response = response + genIntro(element)
	response = response + genAtomicMass(element)
	print response
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

def genAppearance(element):
	return "The appearance of {} is {}".format(element, getAllInfo(element)["appearance"])

def genAtomicMass(element):
	response = ""
	randomNumber = random.randint(1, 3)
	color = getAllInfo(element)["appearance"]
	if randomNumber == 1:
		response = "{} the appearance is {}.  ".format(element, color)
	if randomNumber == 2:
		response = "{} the appearance appears to be {}.  ".format(element, color)
	if randomNumber == 3:
		response = "If you looked at {} it is {}.  ".format(element, color)
	return response

def genSummary(element):
	return str(getAllInfo(element)["summary"]).replace(getAllInfo(element)["symbol"], ' '.join(list(str(getAllInfo(element)["symbol"]).upper())))

def genTemp(element):
	return "the boiling point of {} is {} kelvins".format(element, getAllInfo(element)["boil"])

def genAtomicDensity(element):
	return "the density of {} is {} kilograms per meter cubed".format(element, getAllInfo(element)['density'])

def genAtomicMass(element):
	return "the atomic mass of {} is {} grams".format(element, getAllInfo(element)["atomic_mass"])

def genSymbol(element):
	return "the symbol for {} is {}".format(element, ' '.join(list(str(getAllInfo(element)["symbol"]).upper())))

def genPhase(element):
	return "the phase of {} is {}".format(element, getAllInfo(element)["phase"])

def genCategory(element):
	return "{} is in the {} category".format(element, getAllInfo(element)["category"])

def genFounder(element):
	return "{} was discovered by {}".format(element, getAllInfo(element)["discovered_by"])

def on_intent(intent_request, session):
	intent = intent_request["intent"]
	intent_name = intent_request["intent"]["name"]
	if intent_name == 'quizMe':
		element = random.choice(ELEMENTLIST)
		print element
		print element['name']
		print element['symbol']
	elif intent_name == 'tellMeAboutElements':
		element = intent['slots']['ListOfElements']['value']
		return alexaHelper.returnSpeech(genSummary(element))

	elif intent_name == 'getAppearance':
		element = intent['slots']['ListOfElements']['value']
		return alexaHelper.returnSpeech(genAppearance(element))

	elif intent_name == 'getTemp':
		element = intent['slots']['ListOfElements']['value']
		return alexaHelper.returnSpeech(genTemp(element))

	elif intent_name == 'getAtomicDensity':
		element = intent['slots']['ListOfElements']['value']
		return alexaHelper.returnSpeech(genAtomicDensity(element))

	elif intent_name == 'getAtomicMass':
		element = intent['slots']['ListOfElements']['value']
		return alexaHelper.returnSpeech(genAtomicMass(element))

	elif intent_name == 'getSymbol':
		element = intent['slots']['ListOfElements']['value']
		return alexaHelper.returnSpeech(genSymbol(element))

	elif intent_name == 'getPhase':
		element = intent['slots']['ListOfElements']['value']
		return alexaHelper.returnSpeech(genPhase(element))

	elif intent_name == 'getCategory':
		element = intent['slots']['ListOfElements']['value']
		return alexaHelper.returnSpeech(genCategory(element))

	elif intent_name == 'getFinder':
		element = intent['slots']['ListOfElements']['value']
		return alexaHelper.returnSpeech(genFounder(element))

	elif intent_name == 'aboutDev':
		return alexaHelper.devInfo()
	elif intent_name == "AMAZON.HelpIntent":
		return alexaHelper.get_help_response(REPEATSPEECH)
	elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
		return alexaHelper.handle_session_end_request()