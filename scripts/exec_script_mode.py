def exec_script_mode(name):
    """
    Verifica si el script fue ejecutado localmente o fue importado.
    """
    if name == "__main__":
        return True
    return False