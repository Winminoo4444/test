import random

"""main function"""
def main(stats):
    display_menu()
    choice = get_user_choice()
    if choice == 1:
        play_game(stats)
        main(stats)
    elif choice == 2:
        showing_stats(stats)
        main(stats)
    elif choice == 3:
        if stats['win'] > stats['loss']:
            print("Farewell champion!") # if user has more win than loss
        else:
            print("Goodbye and better luck next time.") # if the user does not have a winning percentage,

"""displaying main menu"""
def display_menu():
    print("1. Play Game | 2. Show Stats | 3. Quit") # menu options

"""getting user choice"""
def get_user_choice():
    choice = input("Enter your choice: ")  # get user input from menu options
    if choice.isdigit() and int(choice) in [1, 2, 3]:  # menu options
        return int(choice)
    else:
        print("Invalid choice.")
        return get_user_choice()

"""getting number of players input"""
def get_number_of_players():
    number_of_players = input("Enter the number of players in each team: ")
    if number_of_players.isdigit() and 1 <= int(number_of_players) <= 10:
        return int(number_of_players)
    else:
        print("Invalid input. Please enter a number between 1 and 10.")
        return get_number_of_players()

"""getting player names input"""
def get_player_names(number_of_players):
    player_names = []  # get player name user input
    for i in range(number_of_players):
        name = input(f"Enter name for player {i + 1}: ")
        if name:
            player_names.append(name)
        else:
            print("You can't have an empty player name.")
            return get_player_names(number_of_players)
    return player_names

"""loading computer team"""
def get_computer_player_names(number_of_players):
    computer_player_names = ["Alice the Adventurer", "Kiera the Knight", "Ingenious Ingrid", "Great Gadfly", "Dave"] # names given in sample output
    return random.sample(computer_player_names, number_of_players)

"""choosing player"""
def choosing_player(blue_team):
    player_choice = input(f"Choose your player number (1-{len(blue_team)}): ")
    if player_choice.isdigit() and 1 <= int(player_choice) <= len(blue_team):
        return int(player_choice) - 1
    else:
        print(f"Invalid input. Please enter a number between 1 and {len(blue_team)}.")
        return choosing_player(blue_team)

"""play game function"""
def play_game(stats):
    number_of_players = get_number_of_players()
    blue_team = get_player_names(number_of_players)
    red_team = get_computer_player_names(number_of_players)
    print(f"Blue Team: {' '.join(blue_team)}")
    print(f"Red Team: {' '.join(red_team)}")
    while blue_team and red_team:
        print("Who will compete for your team?")
        for i, player in enumerate(blue_team, 1):
            print(f"{i}. {player}")
        blue_choice = choosing_player(blue_team)
        red_choice = random.randint(0, len(red_team) - 1)
        print(f"Red chose {red_team[red_choice]}")
        if random.choice([True, False]):
            print(f"{blue_team[blue_choice]} (Blue) wins!")
            red_team.pop(red_choice)
        else:
            print(f"{red_team[red_choice]} (Red) wins :(")
            blue_team.pop(blue_choice)
    if blue_team:
        print("Blue wins the game :)")
        stats['win'] += 1
    else:
        print("Red wins the game :(")
        stats['loss'] += 1

"""function for displaying stats"""
def showing_stats(stats): # function for showing stats after choosing option 2 during menu
    total_games = stats['win'] + stats['loss']
    win_percentage = (stats['win'] / total_games) * 100 if total_games > 0 else 0
    print(f"Wins: {stats['win']}")
    print(f"Losses: {stats['loss']}")
    print(f"Win %: {win_percentage:.1f}")

"""game start"""
def starting_game():
    stats = {'win': 0, 'loss': 0}
    print("Welcome to Blue v Red")
    main(stats)

starting_game()
