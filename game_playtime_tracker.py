"""
Game Playtime Tracker
Joe Widdifield
This will be the program file
tbd: 'any info about starter code/resources used'
9-11-2026
"""

GAMES = ("Hades", "Stardew Valley", "Elden Ring", "Deadlock", "Monster Hunter", "Resident Evil", "Kingdom Hearts", "Bloodborne", "Pokemon", "Persona", "Overwatch", "Tekken", "Gex")
##username = input("Please enter your username: ")


active = True
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' or 'q' to end the program. "
message = ""
while active:
    message = input(prompt)
    if message == 'quit' or message == 'q':
        active = False
    else:
        print(message)