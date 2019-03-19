import random

# credits to:
# Southclaws - all the messages below

words1 = [
	"CJ",
	"O.G.",
	"SAMP",
	"bay",
	"bone",
	"bulgarian",
	"capital",
	"carl",
	"evolve",
	"gay",
	"german",
	"god",
	"godfather",
	"grand",
	"halal",
	"infinity",
	"las",
	"leaked",
	"los",
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
	"larceny",
	"life",
	"one",
	"parrot",
	"pisd",
	"play",
	"survive",
	"turtle",
	"world",
]

def auto_rpname(bot, update):
    if update.message.text.lower() == 'rpname'.lower():
        first = random.choice(words1).capitalize()
        second = random.choice(words2).capitalize()

        first_letter = first[0]
        second_letter = second[0]

        full_msg = f'{first_letter}{second_letter}RP: {first} {second}'

        update.message.reply_text(full_msg)