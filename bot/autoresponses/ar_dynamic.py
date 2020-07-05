import random

# credits to:
# Southclaws - all the messages below

words1 = [
    "3D Tryg",
	"AFK",
	"ATM Machine System",
	"ATM Machine's",
	"ATM System",
	"ATM's",
	"Admin-Vehicle Lock - for all u lazy ppl!!!",
	"Animations",
	"Backpack",
	"Bash",
	"Bazookas System",
	"Biz",
	"Bomb System",
	"Boobs",
	"Business",
	"Business v1.0",
	"Business v1.0-R1",
	"Business v1.0-R2",
	"Business v1.0-R3",
	"Business v1.0-R3.1",
	"Buy Weapon And Kits",
	"Car Ownership System",
	"Categories",
	"Checkpoints",
	"Circles",
	"Company",
	"Dialog Gang Bang System",
	"Dialog Gang System",
	"Dialog Maker",
	"Dildo System",
	"Door System",
	"EPIC HOUSE",
	"EnEx",
	"Entrance",
	"Fire-Bin",
	"GPS",
	"Gang Bang",
	"Gang",
	"Garage",
	"Garbage Collector",
	"Gate",
	"Gates",
	"Guild System",
	"Guild",
	"Hot Coffee",
	"House System",
	"House Creating!",
	"House",
	"House-Biz System",
	"House-Business System",
	"Ice Cream Creation",
	"IconMaker",
	"Interior",
	"Interiors",
	"Job Creation",
	"Large Arrays",
	"Material Text",
	"Media Dialog",
	"Menus",
	"Milf",
	"Milf Gang Bang",
	"Mom",
	"Mom Gang Bang",
	"Myth Creator",
	"News",
	"Org Creation",
	"PISD",
	"Player Account Data",
	"Player Enumerator",
	"Position save system",
	"PowerShell",
	"Race system",
	"Rules ← Using HTTP!",
	"Semi Dynamic System",
	"Server Signature Generator",
	"Short Arrays",
	"Stingers",
	"Stores",
	"Street w/ sign",
	"System",
	"Teleport",
	"Telnet Client",
	"Telnet Server",
	"Update",
	"VEHICLES",
	"Vehicle & Dealership",
	"Vehicle Creator",
	"Vehicle Spawn Menu",
	"Vehicle System",
	"Vertify",
	"Vibrator System",
	"Weapon control",
	"Weapon shop",
]

tags = [
	" ← USING HTTP!",
	"0.3d Compatible",
	"1 line",
	"3D Label",
	"Can also be used for missions!",
	"DJSON",
	"Draft",
	"Dynamic!",
	"Map icon",
	"MSSQL",
	"MySQL",
	"Object",
	"Pickup",
	"SQL",
	"SQLite",
	"Saves + Loads Through MySQL!",
	"Scripting SpeedArt Video",
	"TextDraw",
	"User Friendly",
	"account vertification",
	"for Roleplay",
	"loading & saving",
	"pisd",
	"semi dynamicness",
	"streamer",
	"with advanced anti db",
	"zcmd",
]

dynamic_styles = [
    "dynamic",
    "Dynamic",
    "DYNAMIC",
    "[DYNAMIC]",
]

system_styles = [
    "system",
    "System",
    "SYSTEM",
]

def auto_dynamic(bot, update):
    if update.message.text.lower() == 'dynamic'.lower():
        tag = []
        num = random.randint(2, 6)

        dynamic = random.choice(dynamic_styles) + " " + random.choice(words1) + " "

        for _ in range(2, num):
            rand_tag = random.choice(tags)

            while rand_tag in tag:
                rand_tag = random.choice(tags)

            tag.append(rand_tag)

        for x in tag:
            dynamic += f'[{x}]' + " "

        dynamic += random.choice(system_styles)

        if random.randint(1, 10000) == 10000:
            dynamic += " with extra turtles!"

        update.message.reply_text(dynamic)