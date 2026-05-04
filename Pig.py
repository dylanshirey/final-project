import random

GOAL = 100


def roll_die():
    return random.randint(1, 6)


def hold_at_20_turn():
    turn_total = 0

    while True:
        roll = roll_die()
        print("Roll:", roll)

        if roll == 1:
            turn_total = 0
            break

        turn_total += roll

        if turn_total >= 20:
            break

    print("Turn total:", turn_total)
    return turn_total


def hold_at_x_turn(hold_value):
    turn_total = 0

    while True:
        roll = roll_die()

        if roll == 1:
            return 0

        turn_total += roll

        if turn_total >= hold_value:
            return turn_total


def hold_at_20_outcomes():
    print("How many Hold-at-20 turn simulations?")
    simulations = int(input())

    counts = {}

    for i in range(simulations):
        score = hold_at_x_turn(20)

        if score in counts:
            counts[score] += 1
        else:
            counts[score] = 1

    print("Score\tEstimated Probability")
    for score in sorted(counts):
        print(str(score) + "\t" + str(counts[score] / simulations))


def hold_at_x_outcomes():
    print("Hold value?")
    hold_value = int(input())

    print("How many turn simulations?")
    simulations = int(input())

    counts = {}

    for i in range(simulations):
        score = hold_at_x_turn(hold_value)

        if score in counts:
            counts[score] += 1
        else:
            counts[score] = 1

    print("Score\tEstimated Probability")
    for score in sorted(counts):
        print(str(score) + "\t" + str(counts[score] / simulations))


def hold_at_20_or_goal_turn(score):
    turn_total = 0

    while True:
        roll = roll_die()
        print("Roll:", roll)

        if roll == 1:
            turn_total = 0
            break

        turn_total += roll

        if turn_total >= 20 or score + turn_total >= GOAL:
            break

    print("Turn total:", turn_total)
    score += turn_total
    print("New score:", score)

    return score


def hold_at_20_or_goal_turn_silent(score):
    turn_total = 0

    while True:
        roll = roll_die()

        if roll == 1:
            return score

        turn_total += roll

        if turn_total >= 20 or score + turn_total >= GOAL:
            return score + turn_total


def one_turn_with_score():
    print("Score?")
    score = int(input())
    hold_at_20_or_goal_turn(score)


def solitaire_game():
    score = 0

    while score < GOAL:
        score = hold_at_20_or_goal_turn(score)


def average_pig_turns():
    print("Games?")
    games = int(input())

    total_turns = 0

    for i in range(games):
        score = 0
        turns = 0

        while score < GOAL:
            score = hold_at_20_or_goal_turn_silent(score)
            turns += 1

        total_turns += turns

    print("Average turns:", total_turns / games)


def two_player_pig():
    player1 = 0
    player2 = 0
    current_player = 1

    while player1 < GOAL and player2 < GOAL:
        print("Player 1 score:", player1)
        print("Player 2 score:", player2)
        print("It is player " + str(current_player) + "'s turn.")

        if current_player == 1:
            player1 = hold_at_20_or_goal_turn(player1)
            current_player = 2
        else:
            player2 = hold_at_20_or_goal_turn(player2)
            current_player = 1


def computer_turn(score):
    turn_total = 0

    while True:
        roll = roll_die()
        print("Roll:", roll)

        if roll == 1:
            turn_total = 0
            break

        turn_total += roll

        if turn_total >= 20 or score + turn_total >= GOAL:
            break

    print("Turn total:", turn_total)
    score += turn_total
    print("New score:", score)

    return score


def human_turn(score):
    turn_total = 0

    while True:
        roll = roll_die()
        print("Roll:", roll)

        if roll == 1:
            turn_total = 0
            break

        turn_total += roll

        choice = input("Turn total: " + str(turn_total) + "\tRoll/Hold? ")

        if choice != "":
            break

    print("Turn total:", turn_total)
    score += turn_total
    print("New score:", score)

    return score


def pig_game():
    human_player = random.randint(1, 2)

    print("You will be player " + str(human_player) + ".")
    print("Enter nothing to roll; enter anything to hold.")

    player1 = 0
    player2 = 0
    current_player = 1

    while player1 < GOAL and player2 < GOAL:
        print("Player 1 score:", player1)
        print("Player 2 score:", player2)
        print("It is player " + str(current_player) + "'s turn.")

        if current_player == human_player:
            if current_player == 1:
                player1 = human_turn(player1)
            else:
                player2 = human_turn(player2)
        else:
            if current_player == 1:
                player1 = computer_turn(player1)
            else:
                player2 = computer_turn(player2)

        if current_player == 1:
            current_player = 2
        else:
            current_player = 1


# Change this number to run a different section:
# 1 = One automated hold-at-20 turn
# 2 = Hold-at-20 outcomes
# 3 = Hold-at-X outcomes
# 4 = Hold-at-20-or-goal turn
# 5 = Solitaire game
# 6 = Average Pig turns
# 7 = Two-player Pig
# 8 = Human vs computer Pig game

MODE = 8

if MODE == 1:
    hold_at_20_turn()
elif MODE == 2:
    hold_at_20_outcomes()
elif MODE == 3:
    hold_at_x_outcomes()
elif MODE == 4:
    one_turn_with_score()
elif MODE == 5:
    solitaire_game()
elif MODE == 6:
    average_pig_turns()
elif MODE == 7:
    two_player_pig()
elif MODE == 8:
    pig_game()
