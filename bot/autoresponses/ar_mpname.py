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

def auto_mpname(_bot, update):
    if update.message.text.lower() == 'mpname'.lower():
        first = random.choice(words1).capitalize() # capitalizes the first letter of the randomly selected word
        second = random.choice(words2).capitalize() # also capitalizes the first letter of the randomly selected word

        first_letter = first[0] # accesses index 0 (first letter) of the first word
        second_letter = second[0] # accesses index 0 (first letter) of the second word

        full_msg = f'{first_letter}{second_letter}-MP: {first} {second} Multiplayer'
        update.message.reply_text(full_msg)