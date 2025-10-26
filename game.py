from utils import roll_two_d6,is_bust,is_exact_100,closer_to_target,tie_breaker,turn_decision

def play_game():
    player_1_score = 0
    player_2_score = 0
    player_1_win = ""
    player_2_win = ""
    while player_1_score < 100 or player_2_score < 100:
        counter_pass = 0
        player_1 = True
        player_2 = False
        while player_1:
            print("score = " ,player_1_score)
            player_1_in = turn_decision()
            if player_1_in == "r":
                counter_pass = 0
                player_1 = roll_two_d6()
                print(player_1)
                player_1_score += sum(player_1)
                check1 = is_bust(player_1_score)
                if check1:
                    player_2_win += "win"
                    break
                check2 = is_exact_100(player_1_score)
                if check2:
                    player_1_win += "win"
                    break
            elif player_1_in == "p":
                if counter_pass == 2:
                    break
                counter_pass += 1
                player_1 = False
                player_2 = True

        while player_2:
            print("score = " ,player_2_score)
            player_2_in = turn_decision()
            if player_2_in == "r":
                counter_pass = 0
                player_2 = roll_two_d6()
                print(player_2)
                player_2_score += sum(player_1)
                check1 = is_bust(player_1_score)
                if check1:
                    player_1_win += "win"
                    break
                check2 = is_exact_100(player_2_score)
                if check2:
                    player_2_win += "win"
                    break
            elif player_2_in == "p":
                if counter_pass == 2:
                    break
                counter_pass += 1
                player_2 = False
                player_1 = True







        if counter_pass == 2:
            if player_1_score == player_2_score:
                tie_check = tie_breaker()
                if tie_check == 1:
                    player_1_win += "win"
                elif tie_check == 2:
                    player_2_win += "win"
            else:
                closer_check = closer_to_target(player_1_score,player_2_score)
                if closer_check == 1:
                    player_1_win += "win"
                elif closer_check == 2:
                    player_2_win += "win"

        if player_1_win == "win":
            return "player 1 win!"
        if player_2_win == "win":
            return "player 2 win!"



