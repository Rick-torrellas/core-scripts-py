from os.path import splitext

#TODO: crear una funcion opuesta. remove_format_file
def extract_format_file(filePath,options = {
    "noDot": False
}):
    """
    Extrae el formato de un archivo dado, (opcional noDot) elimina el punto de la extencion. 
    """
    fileFormat = splitext(filePath)[1]
    if (options["noDot"]):
        return fileFormat.partition(".")[2]
    return fileFormat