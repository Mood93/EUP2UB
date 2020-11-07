# input file handling
fname = "wardrobe.ini"
try:
    inHand = open(fname, 'r')
except:
    print('File cannot be opened:', fname)
    exit()

# output file handling
outputName = "UB_ped_xml.txt"
try:
    outHand = open(outputName, 'w')
except:
    print('File cannot be opened:', outputName)
    exit()

#vars
wardrobeName = ""
wardrobeDict = dict()
allWardrobes = dict()
pedName = ""

# xref of input keys to output keys
xref = dict()
xref = {
"Hat": ("prop_hats", "tex_hats"),
"Glasses": ("prop_glasses", "tex_glasses"),
"Ear": ("prop_ears", "tex_ears"),
"Watch": ("prop_watches", "tex_watches"),
"Top": ("comp_shirtoverlay", "tex_shirtoverlay"),
"UpperSkin": ("comp_shirt", "tex_shirt"),
"Decal": ("comp_decals", "tex_decals"),
"UnderCoat": ("comp_accessories", "tex_accessories"),
"Pants": ("comp_pants", "tex_pants"),
"Shoes": ("comp_shoes", "tex_shoes"),
"Accessories": ("comp_eyes", "tex_eyes"),
"Armor": ("comp_tasks", "tex_tasks")
}

# consume wardrobe.ini
for line in inHand:
    line = line.rstrip()
    if line.startswith("[") : #find start of individual wardrobe and save/print name
        wardrobeName = line.strip('[]')
        wardrobeDict = dict() #clear wardrobe on new wardrobe. otherwise wardrobes get overwritten
        #print(wardrobeName)
    
    if not line.startswith("[") : #for each comp, process into dict
        compValues = line.split("=")
        #print(compValues)

        if compValues[0] == "Gender" :
            if compValues[1] == "Male" : wardrobeDict[compValues[0]] = ("Male",)
            elif compValues[1] == "Female" : wardrobeDict[compValues[0]] = ("Female",)

        if compValues[0] in xref :
            #print(compValues[1])
            numbersList = compValues[1].split(":")

            wardrobeDict[compValues[0]] = (numbersList[0], numbersList[1])
            #print(numbersList)
            #print(wardrobeDict)
    
            allWardrobes[wardrobeName] = wardrobeDict

#print(xref, "\n\n")
#print(allWardrobes, "\n\n")

#use dict.get to pull xref and create output 
#loop through data structure and output 
for wardrobe in allWardrobes :
    #print(wardrobe)
    outHand.write(wardrobe + "\n")
    #print(allWardrobes[wardrobe])
    output = "<Ped"
    for comp in allWardrobes[wardrobe] :
        
        if comp == "Gender" : 
            if allWardrobes[wardrobe][comp][0] == "Male" : 
                pedName = "MP_M_FREEMODE_01"
                continue
            elif allWardrobes[wardrobe][comp][0] == "Female" : 
                pedName = "MP_F_FREEMODE_01"
                continue

        compName = str(xref.get(comp)[0])
        compValue = int(allWardrobes[wardrobe][comp][0])
        textureName = str(xref.get(comp)[1])
        textureValue = int(allWardrobes[wardrobe][comp][1])

        if compValue > 1 or textureValue > 1 : #if the comp is not default or has a nondefault texture : print comp
            output += " {0}=\"{1}\"".format(compName, compValue)
            if textureValue > 1 : #if texture is not default : print texture
                output += " {0}=\"{1}\"".format(textureName, textureValue)

        #print(allWardrobes[wardrobe][comp])

    output += ">{}</Ped>\n\n".format(pedName)
    #print(output)
    outHand.write(output)

inHand.close()
outHand.close()