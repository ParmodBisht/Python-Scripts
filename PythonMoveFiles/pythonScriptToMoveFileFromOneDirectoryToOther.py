import shutil
import os

def moveFiles(dst):   
    destination =dst
    #print dst
    filTobeSearched=os.path.basename(os.path.normpath(dst))
    #print filTobeSearched
    for root, dirs, files in os.walk(r"F:\SourceFiles"):
        for file in files:
            if file.endswith(filTobeSearched+".xlsx"):
                 shutil.copy(os.path.join(root, file),destination)
                


for root, dirs, files in os.walk(r"F:\Source"):
    destinationPath=root.replace('\\','/')
    moveFiles(destinationPath)
    
