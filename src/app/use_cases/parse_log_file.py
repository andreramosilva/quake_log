import re
from src.app.entities.game import Game

def parse_log_file(file_path):
    games = []
    current_game = None
    
    with open(file_path, 'r') as file:
        game_id = 0
        for line in file:
            if "InitGame" in line:
                if current_game:
                    games.append(current_game)
                current_game = {"total_kills": 0, "players": [], "kills": {}}
            elif "Kill" in line:
                match = re.search(r"Kill: (\d+) (\d+) (\d+): (.+?) killed (.+?) by (.+)", line) #only way i found to be able to look up is using regex
                if match:
                    killer_name = match.group(4)
                    killer_id = match.group(1)
                    killed_player = match.group(5)
                    if killer_id != "1022" or killer_name != "<world>":
                        current_game["total_kills"] += 1
                        current_game["kills"][killer_name] = current_game["kills"].get(killer_name, 0) + 1
                        if killed_player not in current_game["players"]:
                            current_game["players"].extend([killed_player])
                        
                    elif killer_id == "1022" or killer_name == "<world>":
                        current_game["kills"][killed_player] = current_game["kills"].get(killed_player, 0) - 1    
    if len(games)<1 and current_game:
        games.append(current_game)
    return games
    