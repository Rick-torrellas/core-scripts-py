#cSpell:disable
from os import listdir
from os.path import isfile,join,normpath
from extract_format_file import extract_format_file
def group_similar_files_folder(files_path = "E:\\static\\porn\\DiaDgl\\Diana Douglas\\",files_format = "jpg",sequence_startup = 1,differences_number = 4):
    """
        Group similar files and put them in a numeric sequency of folders.
    """
        #TODO: refactorizar los argumentos
    # * optener los archivos del path
    #   * Solo los archivos y solo los que tengan el files_format
    files = listdir(files_path)
    files_with_path = []
    only_desired_files = []
    for file in files:
        # TODO: Esta podria ser una funcion aparte, join_files_path
        files_with_path.append(join(files_path,file))
    for file in files_with_path:
        # TODO: Esta podria ser una funcion aparte
        file_format = extract_format_file(file,options={"noDot": True})
        if (isfile(file) and file_format == files_format):
            # TODO: crear una operacion en caso de que files_format sea un array.
            only_desired_files.append(file)
    
    print(only_desired_files)
    # * organizarlos
    # * pegarles el path a los archivos
    # * agruparlos
    
    # * crear la carpeta y colocar los archivos en ella.
    pass

group_similar_files_folder()