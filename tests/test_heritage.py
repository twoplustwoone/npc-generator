from src.heritage import load_heritages, choose_random_heritage, generate_heritage

def test_load_heritages():
    heritages = load_heritages()
    assert isinstance(heritages, list)  # Should return a list
    assert len(heritages) > 0  # Should not be empty

def test_choose_random_heritage():
    heritages = ["Mountain Dwarf", "High Elf", "Tiefling"]
    heritage = choose_random_heritage(heritages)
    assert isinstance(heritage, str)  # Should return a string
    assert heritage in heritages  # Should be one of the options

def test_generate_heritage():
    heritage = generate_heritage()
    assert isinstance(heritage, str)  # Should return a string
    assert len(heritage) > 0  # Should not be empty
