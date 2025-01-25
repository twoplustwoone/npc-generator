from src.name import generate_name
from src.heritage import generate_heritage

# Combines different attributes (name, heritage, etc.) to generate a full NPC.

def generate_npc():
    """Generates a complete NPC with a name and heritage."""
    # TODO: Generate a name and heritage for the NPC
    name = generate_name()  # Use the generate_name function
    heritage = generate_heritage()  # Use the generate_heritage function
    return {
        "name": name,
        "heritage": heritage
    }  # Placeholder to make the function callable
