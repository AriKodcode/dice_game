from random import randrange

def roll_two_d6() -> tuple[int, int]:
    """
    פונקצייה שמחזירה הטלת קוביות בטאפל
    :return:
    """
    dice1 = randrange(1,7)
    dice2 = randrange(1,7)
    dices = tuple([dice1,dice2])
    return dices


def is_bust(score: int) -> bool:
    """
    פונקצייה שבודקת אם הניקוד גדול מ100 או לא
    :param score:
    :return:
    """
    if score > 100:
        return True
    else:
        return False

def is_exact_100(score: int) -> bool:
    """
    פונקצייה שבודקת אם הניקוד שווה ל100 בדיוק או לא
    :param score:
    :return:
    """
    if score == 100:
        return True
    else:
        return False

def closer_to_target(a: int, b: int, target: int = 100) -> int | None:
    """
    לאחר שהונכס שני pass הפונקציה בודקת מי מהשחקנים יותר קרוב ל100
    :param a:
    :param b:
    :param target:
    :return:
    """
    if a > b and a < target:
        return 1
    elif b > a and b < target:
        return 2
    elif a == b and a < target:
        return None

def tie_breaker() -> int:
    """
    הפונקציה פועלת במקרה של של שני pass ושני השחקנים בשוויון נקודות יש על כל אחד להטיל קוביה והופקציה מחזירה מי מנצח
    :return:
    """
    while True:
        input("player 1 press Enter")
        player_1_dice = sum(roll_two_d6())
        print(player_1_dice)
        input("player 2 press Enter")
        player_2_dice = sum(roll_two_d6())
        print(player_2_dice)
        if player_1_dice > player_2_dice:
            return 1
        if player_2_dice > player_1_dice:
            return 2

print(tie_breaker())
def turn_decision() -> str:
    """
    פונקציה שקוראת מהמשתמש אם הוא הכניס R או P
    :param input_fn:
    :return:
    """
    print("input r (roll) or p (pass)")
    input_fn = input("")
    while True:
        if input_fn == "r":
            return "roll"
        elif input_fn == "p":
            return "pass"
        else:
            print("Error: No P or R entered.")






