# NPC Generator

A Python-based tool to generate random NPCs for tabletop role-playing games like Dungeons & Dragons. Create unique characters with names and heritages at the click of a button!

---

## Setup Instructions

Follow these steps to set up the project on your local machine.

### Prerequisites

1. Install **Python 3.8+**:
   - [Download Python](https://www.python.org/downloads/)
   - Ensure Python is added to your system's PATH during installation.

2. Install **pip** (Python's package manager, included with most Python installations).

3. Install **git** to clone the repository (optional if files are shared directly).

---

### Installation

1. Clone the Repository:

   ```bash
   git clone git@github.com:twoplustwoone/npc-generator.git
   cd npc-generator
   ```

2. Set Up a Virtual Environment (Recommended):

   ```bash
   python -m venv venv
   ```

   - **Windows**: Activate the virtual environment:

     ```cmd
     .\venv\Scripts\activate
     ```

   - **Mac/Linux**: Activate the virtual environment:

     ```bash
     source venv/bin/activate
     ```

3. Install Dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

### Running the Project

1. Run the NPC Generator:

   ```bash
   python main.py
   ```

   - This will generate and display an NPC with a random name and heritage.

2. Run Tests:
   - To ensure the code works as expected:

     ```bash
     python run_tests.py
     ```

---

### Folder Structure

```plaintext
npc-generator/
├── resources/                # Static data files
│   ├── first_names.txt       # First names list
│   ├── last_names.txt        # Last names list
│   ├── heritages.txt         # Heritages list
├── src/                      # Core Python scripts
│   ├── __init__.py           # Makes src a module
│   ├── name.py               # Handles name generation
│   ├── heritage.py           # Handles heritage generation
│   ├── npc.py                # Combines attributes to create an NPC
├── tests/                    # Test cases for all functions
│   ├── test_name.py          # Tests for name generation
│   ├── test_heritage.py      # Tests for heritage generation
│   ├── test_npc.py           # Tests for NPC generation
├── main.py                   # Entry point for the generator
├── run_tests.py              # Script to run all tests
├── requirements.txt          # List of Python dependencies
├── .gitignore                # Ignore unnecessary files
└── README.md                 # Project documentation
```

---

### Troubleshooting

- **Issue**: `ModuleNotFoundError: No module named 'src'`
  - Solution: Ensure you're running commands from the root of the project directory.

- **Issue**: `FileNotFoundError` for `.txt` files
  - Solution: Confirm the `resources` folder exists and contains `first_names.txt`, `last_names.txt`, and `heritages.txt`.

- **Windows-Specific Issues**:
  - Use the `cmd` shell or PowerShell to run commands (avoid using Unix-style commands like `source`).

---

### Contributing

If you want to contribute, implement the `TODO` sections in the code and ensure all tests pass using:

```bash
python run_tests.py
```
