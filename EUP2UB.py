# file handling
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "wardrobe.ini"
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

#vars
wardrobeName = ""
wardrobeDict = dict()
allWardrobes = dict()

# xref of input keys to output keys
xref = dict()
xref = {
"Hat": (0, "prop_hats", "tex_hats"),
"Glasses": (1, "prop_glasses", "tex_glasses"),
"Ear": (2, "prop_ears", "tex_ears"),
"Watches": (3, "prop_watches", "tex_watches"),
"Top": (4, "comp_shirt", "tex_shirt")
}

# consume wardrobe.ini
for line in fhand:
    line = line.rstrip()
    if line.startswith("[") : #find start of individual wardrobe and save/print name
        wardrobeName = line.strip('[]')
        wardrobeDict = dict()
        #print(wardrobeName)
    
    if not line.startswith("[") : #for each prop, process into dict
        propValues = line.split("=")
        #print(propValues)
        if propValues[0] in xref :
            #print(propValues[1])
            numbersList = propValues[1].split(":")
            wardrobeDict[propValues[0]] = (numbersList[0], numbersList[1])
            #print(numbersList)
            #print(wardrobeDict)
    
            allWardrobes[wardrobeName] = wardrobeDict

# print(xref, "\n\n")
# print(allWardrobes, "\n\n")

#use dict.get to pull xref and create output 

for wardrobe in allWardrobes :
    print(wardrobe)
    #print(allWardrobes[wardrobe])
    output = "<Ped "
    for prop in allWardrobes[wardrobe] :
        output += "{0}=\"{1}\" ".format(xref.get(prop)[1], allWardrobes[wardrobe][prop][0])

        #print(allWardrobes[wardrobe][prop])
        print(output)
