import random
import art
print(art.logo)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
    return score

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a Draw!"
    elif computer_score == 0:
        return "Computer has Blackjack! You lose 😢"
    elif user_score == 0:
        return "You have Blackjack! You win 😎"
    elif user_score > 21:
        return "You went over 21. You lose 😢"
    elif computer_score > 21:
        return "Computer went over 21. You win 😎"
    elif user_score > computer_score:
        return "You win 😎"
    else:
        return "Computer wins 😢"

def play_game():
    user_cards = []
    computer_cards = []
    game_end = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_end:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_end = True
        else:
            get = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if get == "y":
                user_cards.append(deal_card())
            else:
                game_end = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no: ").lower() == "y":
    play_game()
