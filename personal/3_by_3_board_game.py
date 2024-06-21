class color():
    default = "\033[0m"
    green = "\033[32m"
    purple = "\033[95m"
    blue = '\033[94m'
    cyan = '\033[96m'
    yellow = '\033[93m'
    red = '\033[91m'
    clear = '\033[0m'
    bold = '\033[1m'
    underrline = '\033[4m'

def get_player_direction():
    while True:
        valid_directions = ["w","a","s","d"]
        direction = input("Enter direction key: ")
        
        
        #all_moves = direction.split("")
        #for move_number in all_moves:
        if direction in valid_directions:
            break
        else:
            print("ERROR: enter a valid direction key")
            continue
                
    
    return direction
        



def main():
    game_map = [
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[t]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[t]","[w]","[w]","[W]","[w]","[w]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[w]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[w]","[c]","[c]","[c]","[w]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[W]","[c]","[c]","[c]","[W]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[w]","[c]","[c]","[c]","[w]","[ ]","[ ]","[ ]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[w]","[w]","[ ]","[w]","[w]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[t]","[ ]","[ ]","[ ]","[ ]"],
        ["[c]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[c]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[c]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[c]","[ ]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"]
    ]
    player_position = [1,1]
    player_coordinates_x = 1
    player_coordinates_y = 1
    width = len(game_map[1])
    score = 0

    

    while True:
        solids = ["[w]","[W]"]
        direction = get_player_direction()
        check_solid=0
        if direction == "w":
            player_position[0] = player_position[0] - 1
            player_coordinates_y -= 1
            for current_solid in solids:
                if (game_map[player_position[0]][player_position[1]] == current_solid):
                    player_position[0] = player_position[0] + 1
                    player_coordinates_y += 1
                elif (game_map[player_position[0]][player_position[1]] == "[c]"):
                    score += 1
                    game_map[player_position[0]][player_position[1]] = "[ ]"

        elif direction == "a":
            player_position[1] = player_position[1] - 1
            player_coordinates_x -= 1
            for current_solid in solids:
                if (game_map[player_position[0]][player_position[1]] == current_solid):
                    player_position[1] += 1
                    player_coordinates_x += 1
                elif (game_map[player_position[0]][player_position[1]] == "[c]"):
                    score += 1
                    game_map[player_position[0]][player_position[1]] = "[ ]"
                
        elif direction == "s":
            player_position[0] = player_position[0] + 1
            player_coordinates_y += 1
            for current_solid in solids:
                if (game_map[player_position[0]][player_position[1]] == current_solid):
                    player_position[0] -= 1
                    player_coordinates_y -= 1
                elif (game_map[player_position[0]][player_position[1]] == "[c]"):
                    score += 1
                    game_map[player_position[0]][player_position[1]] = "[ ]"
        elif direction == "d":
            player_position[1] = player_position[1] + 1
            player_coordinates_x += 1
            for current_solid in solids:
                if (game_map[player_position[0]][player_position[1]] == current_solid):
                    player_position[1] -= 1
                    player_coordinates_x -= 1
                elif (game_map[player_position[0]][player_position[1]] == "[c]"):
                    score += 1
                    game_map[player_position[0]][player_position[1]] = "[ ]"
        left_bound = player_coordinates_x -3
        right_bound = player_coordinates_x + 3
        upper_bound = player_coordinates_y -3
        lower_bound = player_coordinates_y +3
        #for number_of_moves in moves
        if left_bound < 0:
            left_bound = 0
        if right_bound >= width:
            right_bound = width - 1
        if upper_bound < 0:
            upper_bound = 0
        if lower_bound >= len(game_map):
            lower_bound = len(game_map)-1
        for row in range(upper_bound,lower_bound + 1):
            to_draw = ""
            for length in range(left_bound, right_bound + 1):
                
                #Render and color player
                if row == player_coordinates_y and length == player_coordinates_x:
                    to_draw = to_draw + f"[{color.bold}0{color.clear}]"
                #Render and color trees
                elif game_map[row][length] == "[t]":
                    to_draw = to_draw + f"[{color.green}T{color.clear}]"
                #Render and color walls
                elif game_map[row][length] == "[w]":
                    to_draw = to_draw + f"{color.red}[W]{color.clear}"
                #Render and color windows
                elif game_map[row][length] == "[W]":
                    to_draw = to_draw + f"{color.red}[{color.cyan}W{color.red}]{color.clear}"
                #Render and color coins
                elif game_map[row][length] == "[c]":
                    to_draw = to_draw + f"[{color.yellow}c{color.default}]"
                #Render the rest of the map
                else:
                    to_draw = to_draw + game_map[row][length]
            print(to_draw)
        print(f"Score: {score}")
    
main()