from PIL import Image, ImageFont, ImageDraw
import json

# Stats Helper
def writeStats(modifier,stat,type,coord):
    if int(stat) > 0 and int(stat) <= 30:
        modifier[type] = (int(stat) // 2) - 5
        modifier[type] = ["","+"][modifier[type] > 0] + str(modifier[type])
        if len(stat) == 2:
            write.text((79, coord), stat,fill=(0, 0, 0),font=font)
        else:
            write.text((83, coord), stat,fill=(0, 0, 0),font=font)

# Modifier Helper
def writeModifier(mod,coord):
    if len(mod) == 1:
        write.text((78, coord), mod,fill=(0, 0, 0),font=font)
    elif mod[0] == '-':
        write.text((72, coord), mod,fill=(0, 0, 0),font=font)
    elif len(mod) == 2:
        write.text((67, coord), mod,fill=(0, 0, 0),font=font)
    else:
        write.text((60, coord), mod,fill=(0, 0, 0),font=font)


while 1:
    ################
    ## INITIALIZE ##
    ################

    # Initialize Image
    sheet = Image.open("characterSheet.png")
    write = ImageDraw.Draw(sheet)

    # Get Character
    character = {}
    json_char = ""
    file = open(r"getSheet.txt","r+")
    while json_char == "":
        json_char = file.readline()
    file.truncate(0)
    if json_char:
        character = json.loads(json_char)


    ######################
    ## POPULATE TOP BAR ##
    ######################

    ## NAME ##

    # Name
    if "name" in character:
        font = ImageFont.truetype("arial.ttf", 23)
        length = len(character["name"])
        write.text((80, 95), character["name"],fill=(0, 0, 0),font=font)


    ## TOP INFO BAR ##

    font = ImageFont.truetype("arial.ttf", 18)

    # Class
    if "class" in character:
        write.text((410, 75), character["class"]+" "+character["level"],fill=(0, 0, 0),font=font)

    # Background
    if "background" in character:
        write.text((560, 75), character["background"],fill=(0, 0, 0),font=font)

    # Player Name
    if "player" in character:
        write.text((725, 75), character["player"],fill=(0, 0, 0),font=font)

    # Race
    if "race" in character:
        write.text((410, 115), character["race"],fill=(0, 0, 0),font=font)

    # Alignment
    if "align" in character:
        write.text((560, 115), character["align"],fill=(0, 0, 0),font=font)

    # Experience
    if "xp" in character:
        write.text((725, 115), character["xp"],fill=(0, 0, 0),font=font)


    ####################
    ## POPULATE STATS ##
    ####################

    ## STATS ##

    modifier = {}
    font = ImageFont.truetype("arial.ttf", 15)

    # Strength
    if "str" in character:
        writeStats(modifier,character["str"],"str",284)

    # Dexterity
    if "dex" in character:
        writeStats(modifier,character["dex"],"dex",394)

    # Constitution
    if "con" in character:
        writeStats(modifier,character["con"],"con",502)

    # Intelligence
    if "int" in character:
        writeStats(modifier,character["int"],"int",611)

    # Wisdom
    if "wis" in character:
        writeStats(modifier,character["wis"],"wis",719)

    # Charisma
    if "cha" in character:
        writeStats(modifier,character["cha"],"cha",827)


    ## MODIFIERS ##

    font = ImageFont.truetype("arial.ttf", 32)

    # Strength
    if "str" in modifier:
        writeModifier(modifier["str"],238)

    # Dexterity
    if "dex" in modifier:
        writeModifier(modifier["dex"],348)

    # Constitution
    if "con" in modifier:
        writeModifier(modifier["con"],455)

    # Intelligence
    if "int" in modifier:
        writeModifier(modifier["int"],564)

    # Wisdom
    if "wis" in modifier:
        writeModifier(modifier["wis"],672)

    # Charisma
    if "cha" in modifier:
        writeModifier(modifier["cha"],780)


    ## BIG THREE ##

    # AC
    if "ac" in character:
        font = ImageFont.truetype("arial.ttf", 32)
        write.text((356, 217), character["ac"],fill=(0, 0, 0),font=font)

    # Initiative
    if "init" in character:
        font = ImageFont.truetype("arial.ttf", 40)
        write.text((436, 217), "+"+character["init"],fill=(0, 0, 0),font=font)

    # Speed
    if "speed" in character:
        font = ImageFont.truetype("arial.ttf", 30)
        write.text((520, 223), character["speed"]+"ft.",fill=(0, 0, 0),font=font)


    ################
    ## SAVE IMAGE ##
    ################

    # Save Image
    sheet.save("newSheet.png")


    ####################
    ## RETURN MESSAGE ##
    ####################

    file.write("Sheet created successfully")
    file.truncate(0)
    file.close()
