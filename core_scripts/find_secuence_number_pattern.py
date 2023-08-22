def find_secuence_number_pattern():
    """
        Encontrara patrones de secuencias numericas en strings, creara una lista de listas, con los patrones que encuentre ordenados numericamente.
    """
    #TODO: se podria colocar una opcion que indique si se quiere ordenar decrecientemente.
    # primero se ordenara todos los valores de la lista con natsort
    # el proceso sera un array definitivo que contenga los arrays resultantes.
    # el truco es ir colocando los valores, para ir comparandolos con la lista.
    # entonces se va a comprar para determinar cual es la parte que cambia, y al determinarla se eliminan de ambas lista para comparar, una vez que se encuentre otra diferencia que llege a 10 se elimina ahora ese ahora que llege a 100 y se elimina, hasta que llegue a un nuevo patron, en ese caso se detterminara, si encuentra mas de 1 diferencia es que es otro patron, entonces se terminara esa lista, y se agregara una nueva en la lista total.
    pass