from src.npc import generate_npc

def main():
    """Main function to generate and display an NPC."""
    print("Welcome to the NPC Generator!")
    print("Generating a random NPC...\n")

    try:
        npc = generate_npc()  # Generates the NPC with name and heritage
        print("Here is your NPC:")
        print(f"Name: {npc['name']}")
        print(f"Heritage: {npc['heritage']}")
    except Exception as e:
        print("An error occurred while generating the NPC.")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
