import discord
import os
import requests
import json
# from replit import db
from all_open import all_open


client = discord.Client()

theKEY = os.environ['KEY']

def getActivity():
	ActivityResponse = requests.get("https://www.boredapi.com/api/activity")
	jsonActivity = json.loads(ActivityResponse.text)
	return jsonActivity["activity"] + " (" + jsonActivity["type"] + ")"

def getFact():
	FactResponse = requests.get("https://useless-facts.sameerkumar.website/api")
	jsonFact = json.loads(FactResponse.text)
	return jsonFact["data"]

def getNews():
	NewsResponse = requests.get("https://newsapi.org/v2/top-headlines?country=ca&apiKey=" + theKEY)
	jsonNews = json.loads(NewsResponse.text)
	articleTitle = (jsonNews['articles'][0]['title'])
	articleContent = (jsonNews['articles'][0]['content'])
	articleURL = (jsonNews['articles'][0]['url'])
	return articleTitle + "\n\n" + articleContent + "\n" + articleURL
	
def getHelp():
	return ("Command List\nCommand:    Description:\n$I'm bored    Displays an activity\n$fact               Displays a random fact\n$enlighten     Displays current world news")

@client.event
async def on_ready():
	print("We have logged in")

@client.event
async def on_message(message):
	if(message.content.startswith("$help")):
		hel = getHelp()
		await message.channel.send(hel)
		
	if(message.content.startswith("$I'm bored")):
		activity = getActivity()
		await message.channel.send(activity)
  
	if(message.content.startswith("$fact")):
		fact = getFact()
		await message.channel.send(fact)

	if(message.content.startswith("$enlighten")):
		article = getNews()
		await message.channel.send(article)

# @client.event
all_open()
client.run(os.getenv('bot-secret'))