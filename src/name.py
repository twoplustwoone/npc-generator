# Reads name files and randomly chooses a first and last name, and returns them as a string.

def generate_name():
    names = load_names()
    name = choose_random_name(names)
    return name

def load_names():
    first_names = load_first_names()
    last_names = load_last_names()
    return (first_names, last_names)

def load_first_names():
    # TODO load first names from ../resources/first_names.txt
    return null

def load_last_names():
    # TODO load last names from ../resources/last_names.txt
    return null

def choose_random_name(names):
    # Read first names from tuple
    # Choose a random first name
    # Read last names from tuple
    # Choose a random last name
    return ""
