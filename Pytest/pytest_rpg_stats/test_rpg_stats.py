from rpg_stats import generate_strength
def test_initial_strength():
    assert generate_strength()==5

from rpg_stats import is_stat_valid
# def test_valid_stat_middle():
#     assert is_stat_valid(5)==True
# def test_valid_stat_lower_bound():
#     assert is_stat_valid(1)==True
# def test_valid_stat_upper_bound():
#     assert is_stat_valid(10)==True
# def test_invalid_stat_too_low():
#     assert is_stat_valid(0)==False
# def test_invalid_stat_too_high():
#     assert is_stat_valid(11)==False
    

import pytest
@pytest.mark.parametrize(
    "input_value,expected_result",
    [
        (5, True), 
        (1, True), 
        (10, True), 
        (0, False), 
        (11,False),
    ]
)
def test_stat_validation(input_value,expected_result):
    assert is_stat_valid(input_value)==expected_result
    

@pytest.fixture
def average_character_stats():
    return {'strength':5, 'dexterity': 6}

def test_average_strength(average_character_stats):
    assert average_character_stats['strength']==5
    
    
from rpg_stats import Character
# def test_character_creation():
#     character=Character(strength=8,intelligence=7)
#     assert character.strength == 8
#     assert character.intelligence == 7

def test_character_combat_readiness():
    character = Character(strength=6, dexterity=8, intelligence=5)
    assert character.get_combat_readiness() == 14