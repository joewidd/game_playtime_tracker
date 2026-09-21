"""
Game Playtime Tracker
Joe Widdifield
This will be the main program file
9-11-2026
"""

GAMES = ("Hades", "Stardew Valley", "Elden Ring", "Deadlock", "Monster Hunter", "Resident Evil", "Kingdom Hearts", "Bloodborne", "Pokemon", "Persona", "Overwatch", "Tekken", "Gex")

def get_game_playtime():
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
                    print(f"\nYou've selected {game}")
                    break

        hours = input(hours_prompt)
        if hours == 'quit' or hours == 'q':
            break
        else:
            print(f"\n{hours} hours played in {game}")
            break

get_game_playtime()