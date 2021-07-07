import os
import json

DIR = "./meta-data/"
DST = "./modules/"
os.mkdir(DST)

for folder in os.listdir(DIR):
    moduleFile = DIR+folder+"/module.txt"
    # check for Module.txt to get infomation about module
    if(os.path.isfile(moduleFile)):
        getModuledata = open(moduleFile, "r")
        readModuleData = getModuledata.read()
        parseData = json.loads(readModuleData)
        moduleName = parseData['id']
        moduleDescription = parseData['description']
        moduleLogo = "defaultBanner.png"
        moduleReadme = DIR+folder+"/README.md"

        os.mkdir(DST+moduleName)
        IndexMd = open(DST+moduleName+"/index.md", "a+")
        IndexMd.write('---\n')
        IndexMd.write('posttype: "module" \n')
        IndexMd.write('title: '+moduleName+'\n')
        IndexMd.write('description: "'+moduleDescription+'"\n')
        
        # check for module logo or cover image
        if(os.path.isfile(moduleLogo)):
            IndexMd.write('cover: "./cover.png"'+'\n')
            sourceImage = open(moduleLogo, "rb")
            readImage = sourceImage.read()
            ImageFile = open(DST+moduleName+"/cover.png", "wb+")
            ImageFile.write(readImage)
            ImageFile.close()
            sourceImage.close()

        # collecting tags
        Tags = []
        if "isGameplay" in parseData:
            if (parseData['isGameplay']):
                Tags.append("Gameplay")

        if "isServerSideOnly" in parseData:
            if(parseData['isServerSideOnly']):
                Tags.append("Server")

        if "isWorld" in parseData:
            if (parseData['isWorld']):
                Tags.append("World")

        if "isAugmentation" in parseData:
            if (parseData['isAugmentation']):
                Tags.append("Augment")

        if "isLibrary" in parseData:
            if(parseData['isLibrary']):
                Tags.append("Library")

        if "isAsset" in parseData:
            if(parseData['isAsset']):
                Tags.append("Asset")

        if "isSpecific" in parseData:
            if(parseData['isSpecific']):
                Tags.append("Specific")

        IndexMd.write("tags: "+"["+','.join(f'"{w}"' for w in Tags)+"]\n")
        IndexMd.write('---\n')

        # check for readmeFile
        if(os.path.isfile(moduleReadme)):
            readmedata = open(moduleReadme, "r")
            IndexMd.write(readmedata.read())
        else:
            IndexMd.write("No info available")