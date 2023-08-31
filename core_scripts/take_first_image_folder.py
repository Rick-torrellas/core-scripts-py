from take_first_file_folder import take_first_file_folder
from os.path import splitext

def take_first_image_folder_list_(firstFile,imageFormat):
    firstFileExtencion = splitext(firstFile)

def take_first_image_folder_string_(firstFile,imageFormat):
    imagenExtencionPath = splitext(firstFile)
    imageExtencion = imagenExtencionPath[1].partition(".")[2]
    if(imageFormat == imageExtencion):
        return firstFile
    return False

def take_first_image_folder(pathFolder,imageFormat = False):
    " Agarra la primera imagen de una carpeta"
    firstFile = take_first_file_folder(pathFolder)
    firstImageFolder = ""
    if (isinstance(imageFormat,list)):
        firstImageFolder = take_first_image_folder_list_(firstFile,imageFormat)
    else:
        firstImageFolder = take_first_image_folder_string_(firstFile,imageFormat)
    return firstImageFolder


a = take_first_image_folder("C:/Users/worf_/Desktop/test/01","png")

print(a)