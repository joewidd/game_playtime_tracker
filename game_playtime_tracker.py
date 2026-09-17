"""
Game Playtime Tracker
Joe Widdifield
This will be the main program file
9-11-2026
"""

GAMES = ("Hades", "Stardew Valley", "Elden Ring", "Deadlock", "Monster Hunter", "Resident Evil", "Kingdom Hearts", "Bloodborne", "Pokemon", "Persona", "Overwatch", "Tekken", "Gex")
##username = input("Please enter your username: ")

def collect_user_input():
    game_prompt = "\nTell me the game you played from the games listed"
    game_prompt += f"\n{GAMES}"
    game_prompt += "\nEnter 'quit' or 'q' to end the program: "
    hours_prompt = "\nTell me how many hours you played"
    hours_prompt += "\nEnter 'quit' or 'q' to end the program: "
    game = ""
    hours = ""
    while True:

        game = input(game_prompt)
        if game == 'quit' or game == 'q':
            break
        else:
            for i in GAMES:
                if game == i:
                    print(f"\n{game}")
                    break

        hours = input(hours_prompt)
        if hours == 'quit' or hours == 'q':
            break
        else:
            print(f"\n{hours} hours played")
            break

collect_user_input()