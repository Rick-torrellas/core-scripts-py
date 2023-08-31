from os import listdir
from os.path import normpath,isdir,join
from natsort import natsorted

def take_first_file_folder(pathFolder):
    """
    Agarra solo el primer archivo de una carpeta.
    """
    pathFolder_ = normpath(pathFolder)
    filesInFolder = listdir(pathFolder_)
    orderedFilesInFolder = natsorted(filesInFolder)
    orderedFilesInFolderWithPath = []
    for file in orderedFilesInFolder:
        orderedFilesInFolderWithPath = join(pathFolder_,file)
        if isdir(orderedFilesInFolderWithPath):
            continue
        firstFileInFolder = orderedFilesInFolderWithPath
        break
    return firstFileInFolder