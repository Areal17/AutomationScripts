import os

cwd = os.getcwd()
print("Current: " + cwd)

textFolder = os.path.join(cwd, 'textFolder')
if os.path.exists(textFolder) == False:
    os.makedirs(textFolder)
    print("new dir")
# os.remove(textFolder)
basename = os.path.basename(textFolder)
print("FolderName: " + basename)

pathToFile = os.path.join(cwd, 'regex.py')
if os.path.exists(pathToFile) == True:
    pyFile = open(pathToFile)


def findingMayer():
    cwd = os.getcwd()
    textFolderPath = os.path.join(cwd, "textFolder")
    if os.path.exists(textFolderPath) == True:
        # wenn textfile vorhanden öffenen, sonst 
        print("Yeahh")
    else:
        os.makedir("textFolder")
    
    # Pfad für Textdatei ermitteln.
    # Textdatei in textFolder kopieren
    # Textdatei öffnen
    # Textdatei lesen
    
    print("Kein Mayer gefunden")
    
def isEven(number):
    # if number % 2 == 0:
#         return True
#     return False
    return number % 2 == 0

print(isEven(42))


