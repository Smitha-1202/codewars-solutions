wins = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif wins[p1] == p2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"