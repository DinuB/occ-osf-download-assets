import os, json, sys

# download assets
def downloadAssets(): 
    os.system('yarn download-assets')

#  files
def listSlots():
    dirname = './packages/apps/core-commerce-reference-store/assets/slots'
    dirfiles = os.listdir(dirname)

    fullpaths = map(lambda name: os.path.join(dirname, name), dirfiles)

    for file in fullpaths:
        if os.path.isdir(file): 
            listFiles(file) 

def listFiles(folder):
    dirname = folder
    dirfiles = os.listdir(dirname)

    fullpaths = map(lambda name: os.path.join(dirname, name), dirfiles)

    for file in fullpaths:
        if os.path.isfile(file): 
            if file.__contains__("structure.json"):
                setFile(file)

def setFile(file):

    file_json = openFile(file)

    if file_json:
        for region in file_json['regions']:
            region['displayName'] = region["resources"]["en"]["displayName"]
    else:
        print("file error: ", file)
        exit()

    saveFile(file, file_json)

def openFile(file):
    try:
        with open(file, 'r') as json_file:
            return json.load(json_file)
    except:
        return False

def saveFile(file, file_json):
    with open(file, 'w') as json_file:
        json.dump(file_json, json_file, indent=2)

if sys.argv[1] and sys.argv[1] == "download":
    downloadAssets()
else:
    if sys.argv[1] and sys.argv[1] == "refresh-assets":
        refresh = "y"
    else:
        print("missing arguments")

refresh = "y" if sys.argv[1] and sys.argv[1] == "refresh-assets" else input("Refresh Assets?(y/n):")

if refresh == "y":
    listSlots()