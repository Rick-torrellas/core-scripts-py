from yaml import dump

def create_yaml(pathfile,data):
    with open(pathfile,"x") as file:
        return dump(data)
