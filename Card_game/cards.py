import random


def generate_deck_of_card(n_deck=1):
    shape = ["♦️", "♥️", "♠️", "♣️"]
    number = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    full_deck = [f"{s} {n}" for s in shape for n in number]
    return full_deck * n_deck


def distribute_card_for_flash(totalplayer):
    card_list = generate_deck_of_card()
    random.shuffle(card_list)
    players_with_card = []
    for i in range(totalplayer):
        player_cards = []

        for j in range(3):
            player_cards.append(card_list.pop())
        players_with_card.append({"Name": player_names[i], "Cards": player_cards})
    return players_with_card


player_names = input("Enter player name separated by comma: ").split(",")
total_number_of_players = len(player_names)

while True:
    result = distribute_card_for_flash(total_number_of_players)
    for i in result:
        print(f"{i['Name']} : {i['Cards']}")
    print()
    replay_chk = input("Do you want to continue? ")
    if replay_chk[0].lower() == "n":
        break

print("Thanks for playing")
