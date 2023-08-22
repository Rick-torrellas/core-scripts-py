from os import listdir
from os.path import normpath,isdir,join

def take_first_file_folder(pathFolder):
    """
    Agarra solo el primer archivo de una carpeta.
    """
    pathFolder_ = normpath(pathFolder)
    filesInFolder = listdir(pathFolder_)
    orderedFilesInFolder = ""
    for file in orderedFilesInFolder:
        fileInFolder = join(pathFolder_,file)
        if isdir(fileInFolder):
            continue
        firstFileInFolder = fileInFolder
        break
    return firstFileInFolder

l = take_first_file_folder('C:/Users/worf_/Desktop/test/01')

print(l)