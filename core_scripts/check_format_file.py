from os.path import splitext

def check_format_file_list_(fileExtencion,fileFormat):
    for extencion in fileFormat:
        if(extencion == fileExtencion):
            return True
    return False
    

def check_format_file_string_(fileExtencion,fileFormat):
    if (fileFormat == fileExtencion):
        return True
    return False

def check_format_file(file,fileFormat):
    """
        Verificara el formato de un archivo. Devuelve True si el file coincide con el fileFormat
    """
    # TODO: usar extract_format_file
    fileExtencion = splitext(file)[1].partition(".")[2]
    if (isinstance(fileFormat,list)):
        return check_format_file_list_(fileExtencion,fileFormat)
    return check_format_file_string_(fileExtencion,fileFormat)