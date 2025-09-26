from hajar_waraqa_maqs.cli import decide_winner

def test_tie():
    res, msg = decide_winner("rock", "rock")
    assert res == "tie"

def test_win_cases():
    assert decide_winner("rock", "scissors")[0] == "win"
    assert decide_winner("paper", "rock")[0] == "win"
    assert decide_winner("scissors", "paper")[0] == "win"

def test_lose_cases():
    assert decide_winner("rock", "paper")[0] == "lose"
    assert decide_winner("paper", "scissors")[0] == "lose"
    assert decide_winner("scissors", "rock")[0] == "lose"
