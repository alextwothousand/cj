import random

# credits to:
# Southclaws - all the messages below

words1 = [
    "CJ",
	"O.G.",
	"SAMP",
	"adorable",
	"bay",
	"bone",
	"bulgarian",
	"capital",
	"carl",
	"evolve",
	"gay",
	"god",
	"godfather",
	"halal",
	"infinity",
	"las",
	"leaked",
	"mom",
	"next",
	"one",
	"payday",
	"pisd",
	"pure",
	"red",
	"role",
	"san",
	"scavenge",
	"sexy",
	"texas",
]

words2 = [
	"SAMP",
	"andreas",
	"area",
	"christian",
	"cops",
	"county",
	"day",
	"game",
	"gangstas",
	"ginger",
	"halal",
	"johnson",
	"life",
	"one",
	"parrot",
	"pisd",
	"play",
	"survive",
	"turtle",
	"world",
]

mapname_styles = [
    "map",
    "Map",
    "MAP",
    "[MAP]"
]

def auto_mapname(bot, update):
    if update.message.text.lower() == 'mapname'.lower():
        if random.randint(0, 1) == 0: first = random.choice(words1).capitalize()
        else: first = random.choice(words1)

        if random.randint(0, 1) == 0: second = random.choice(words2).capitalize()
        else: second = random.choice(words1)

        mapname = first + " " + second + " " + random.choice(mapname_styles)

        if random.randint(1, 10000) == 10000:
            mapname +=  " with extra turtles!"

        update.message.reply_text(mapname)


