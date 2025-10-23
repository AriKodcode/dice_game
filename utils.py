from random import randrange

def roll_two_d6() -> tuple[int, int]:
    dice1 = randrange(1,7)
    dice2 = randrange(1,7)
    dices = tuple([dice1,dice2])
    return dices

def is_bust(score: int) -> bool:
    if score > 100:
        return True
    else:
        return False

def is_exact_100(score: int) -> bool:
    if score == 100:
        return True
    else:
        return False

def closer_to_target(a: int, b: int, target: int = 100) -> int | None:
    if a > b and a < target:
        return 1
    elif b > a and b < target:
        return 2
    elif a == b and a < target:
        return None

def tie_breaker(roller) -> int:
    