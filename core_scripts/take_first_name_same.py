from os import listdir
from os.path import basename,normpath,isdir


def take_first_name_same(pathFolder):
    """
        Agarra el primer archivo en una carpeta, lo copia fuera de la carpeta y lo renombra con el mismo nombre de la carpeta.
    """
    pathFolder_ = normpath(pathFolder)
    #listar todos los archivos del pathFolder
    filesInFolder = listdir(pathFolder_)
    for file in filesInFolder:
        if isdir(file):
            continue
        firstFileInFolder = file
    print(firstFileInFolder)
    #agarrar el primer archivo y copiarlo
    #pegalo en la ruta donde se encuentra el pathFolder
    #renombrarlo con el nombre del folder del pathFolder

take_first_name_same('C:/Users/worf_/Desktop/test/01')