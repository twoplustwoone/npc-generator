import os
import random

# Reads heritage files and randomly selects a heritage, returning it as a string.

def generate_heritage():
    """Generates a random heritage from the available options."""
    heritages = load_heritages()  # Load the list of heritages
    heritage = choose_random_heritage(heritages)  # Select a random heritage
    return heritage

def load_heritages():
    """Loads heritages from the 'heritages.txt' file."""
    # TODO: Implement the logic to load heritages from ../resources/heritages.txt
    # Use file handling (open and read lines)
    # Return a list of heritages, one heritage per line
    return None  # Placeholder to make the function callable

def choose_random_heritage(heritages):
    """Chooses a random heritage from the provided list."""
    # TODO: Use random.choice to pick one heritage
    return ""  # Placeholder to make the function callable
