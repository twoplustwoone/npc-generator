from src.npc import generate_npc

def test_generate_npc():
    npc = generate_npc()
    assert isinstance(npc, dict)  # Should return a dictionary
    assert "name" in npc  # Should include a name
    assert "heritage" in npc  # Should include a heritage
    assert isinstance(npc["name"], str)
    assert isinstance(npc["heritage"], str)
