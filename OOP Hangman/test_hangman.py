import pytest
from unittest.mock import patch, mock_open
from hangman import Game

@pytest.fixture
@patch('builtins.open', new_callable=mock_open, read_data="aaaaa")
def game_word_is_a(mock_file):
    return Game(5)

@pytest.fixture
@patch('builtins.open', new_callable=mock_open, read_data="testword")
def game_word_is_testword(mock_file):
    return Game(5)


def test_turns(game_word_is_a):
    assert game_word_is_a.turns == 5

def test_play_one_round_a(game_word_is_a):
    with patch('builtins.input', side_effect=["a"]) as mock_input:
        assert game_word_is_a.play_one_round() is True
        assert game_word_is_a.turns == 4
        assert mock_input.call_count == 1
    
    with patch('builtins.input', side_effect=["", "", "", "", "", "", "a", "b"]) as mock_input:
        assert game_word_is_a.play_one_round() is True
        assert game_word_is_a.turns == 3
        assert mock_input.call_count == 8
    
def test_play_one_round_aa(game_word_is_a):
    with patch('builtins.input', return_value="aa"):
        assert game_word_is_a.play_one_round() is False
        assert game_word_is_a.turns == 4

def test_play_one_round_check(game_word_is_testword):
    with patch('builtins.input', return_value="TESTWORD"):
        assert game_word_is_testword.play_one_round() is True
