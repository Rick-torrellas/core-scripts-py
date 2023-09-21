# cSpell:disable
from natsort import natsorted 
from os import listdir
from os.path import normpath,join
from difflib import ndiff
from jellyfish import damerau_levenshtein_distance


def find_sequence_number_pattern(strings,diferences_number):
    """
        Va a encontrar strings similares y las va a agrupar dentro de una lista de listas.
    """
    strings_list = []
    first_string = ""
    string_list_index = 0
    for string in strings:
        index = strings.index(string)
        if (index == 0):
            first_string = string
            strings_list.append([])
            strings_list[0].append(string)
            continue
        diferences_strings = damerau_levenshtein_distance(first_string,string)
        if (diferences_strings < diferences_number):
            strings_list[string_list_index].append(string)
        else:
            first_string = string
            strings_list.append([])
            string_list_index = string_list_index + 1
            strings_list[string_list_index].append(string)
            continue

    
    """
        Encontrara patrones de secuencias numéricas en strings, creara una lista de listas, con los patrones que encuentre ordenados numéricamente. 
    """
    #TODO: se podría colocar una opción que indique si se quiere ordenar decrecientemente.
    # primero se ordenara todos los valores de la lista con natsort | cSpell:disable-line
    # el proceso sera un array definitivo que contenga los arrays resultantes.
    # el truco es ir colocando los valores, para ir comparándolos con la lista.
    # entonces se va a comprar para determinar cual es la parte que cambia, y al determinarla se eliminan de ambas lista para comparar, una vez que se encuentre otra diferencia que llegue a 10 se elimina ahora ese ahora que llegue a 100 y se elimina, hasta que llegue a un nuevo patron, en ese caso se determinara, si encuentra mas de 1 diferencia es que es otro patron, entonces se terminara esa lista, y se agregara una nueva en la lista total.
