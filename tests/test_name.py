from src.name import load_first_names, load_last_names, choose_random_name, generate_name

def test_load_first_names():
    names = load_first_names()
    assert isinstance(names, list)  # Should return a list
    assert len(names) > 0  # Should not be empty

def test_load_last_names():
    names = load_last_names()
    assert isinstance(names, list)  # Should return a list
    assert len(names) > 0  # Should not be empty

def test_choose_random_name():
    first_names = ["Liam", "Aria"]
    last_names = ["Brightwood", "Duskwind"]
    full_name = choose_random_name((first_names, last_names))
    assert isinstance(full_name, str)  # Should return a string
    assert " " in full_name  # Should contain a space between first and last names

def test_generate_name():
    name = generate_name()
    assert isinstance(name, str)  # Should return a string
    assert len(name.split()) == 2  # Should have exactly two words (First Last)
