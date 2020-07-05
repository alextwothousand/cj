import random

# credits to:
# Southclaws - all the messages below

words1 = [
	"advanced",
	"amazeballs",
	"amazing",
	"amk",
	"edit",
	"elite",
	"exiting",
	"extr3m3",
	"extreme",
	"fucking",
	"fusion",
	"gold",
	"haram",
	"infusion",
	"l33t",
	"mega",
	"mom",
	"pisd",
	"platinum",
	"pro",
	"profesional",
	"reloaded",
	"sa-mp server",
	"ultra",
	"wow",
	"xd",
	"xtreme",
	"you're",
]

words2 = [
    "abyss",
	"barp-leak",
	"black",
	"clan",
	"community",
	"español",
	"gaming",
	"gang",
	"ginger",
	"group",
	"hackers",
	"killaz",
	"krisk",
	"mom",
	"motherfuckers",
	"parkour",
	"pisd",
	"profesionals",
	"pros",
	"rcrp-leak",
	"revolution",
	"scripters",
	"white",
]

gm = [
    "deathmatch",
	"derby",
	"dm",
	"freeroam",
	"game",
	"gangbang",
	"gangwars",
	"minigames",
	"pisd",
	"race",
	"racing",
	"roleplay",
	"rp",
	"rpg",
	"sex",
	"tdm",
	"war",
]

tags = [
    "0.3.DL",
	"0.3e+",
	"25.000 LINES",
	"ABYSS",
	"BASIC",
	"BEST",
	"BETA",
	"C++",
	"CUSTOM OBJECTS",
	"DYNAMIC",
	"GF EDIT",
	"GO",
	"GODFATHER",
	"HALAL",
	"HARAM",
	"HIRING",
	"IMPROVED",
	"LAGSHOT",
	"LUA",
	"MOMS",
	"MYSQL",
	"NGG",
	"NGRP",
	"OFFICIAL",
	"PAWN",
	"PAWNO",
	"PISD",
	"RAKNET",
	"RCRP",
	"REDIS",
	"REFUNDING",
	"ROLEYPLAY",
	"ROLLERPLAYERS ONLY",
	"RUS",
	"SAMPCTL",
	"SCRATCH",
	"SOUTHCLAWS",
	"SSCANF",
	"STRCMP",
	"STRCMP2",
	"STRTOK",
	"STRTOK2",
	"TELNET",
	"UCP",
	"UNIQUE",
	"YLESS",
	"Y_INI",
	"ZCMD",
	"ZOMBIES",
]

def auto_gmname(bot, update):
    if update.message.text.lower() == 'gmname'.lower():
        tag = []
        num = random.randint(1, 4)

        gamemode = random.choice(words1) + " " + random.choice(words2) + " " + random.choice(gm) + " "

        for _ in range(1, num):
            rand_tag = random.choice(tags)

            while rand_tag in tag:
                rand_tag = random.choice(tags)

            tag.append(rand_tag)

        for x in tag:
            gamemode += f'[{x}]' + " "

        update.message.reply_text(gamemode)

    