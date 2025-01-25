import os
import random

# Reads name files and randomly chooses a first and last name, returning them as a string.

def generate_name():
    """Generates a full name by combining a random first and last name."""
    names = load_names()  # Loads names (first and last)
    name = choose_random_name(names)  # Selects a random name
    return name

def load_names():
    """Loads first and last names from the respective files."""
    first_names = load_first_names()
    last_names = load_last_names()
    return (first_names, last_names)

def load_first_names():
    """Loads first names from the 'first_names.txt' file."""
    # TODO: Implement the logic to load names from ../resources/first_names.txt
    # Use file handling (open and read lines)
    # Return a list of names, one name per line
    return None  # Placeholder to make the function callable

def load_last_names():
    """Loads last names from the 'last_names.txt' file."""
    # TODO: Implement the logic to load names from ../resources/last_names.txt
    # Similar to load_first_names
    return None  # Placeholder to make the function callable

def choose_random_name(names):
    """Chooses a random first and last name from the provided tuple of name lists."""
    # TODO: Extract first_names and last_names from the tuple
    # Use random.choice to pick one first name and one last name
    # Return a string in the format "First Last"
    return ""  # Placeholder to make the function callable
