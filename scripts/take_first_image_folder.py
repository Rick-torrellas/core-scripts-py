from take_first_file_folder import take_first_file_folder
from check_format_file import check_format_file
from formatFiles import image

def take_first_image_folder(pathFolder,imageFormat = image):
    " Agarra la primera imagen de una carpeta"
    firstFile = take_first_file_folder(pathFolder)
    if (check_format_file(firstFile,imageFormat)):
        return firstFile
    return False