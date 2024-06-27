import characters
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
    underline = '\033[4m'

player = characters.Characters(1,1,0,"[0]")


def get_player_direction(valid_key_list):
    while True:
        valid_directions = valid_key_list
        direction = input("Enter key: ")
        
        
        #all_moves = direction.split("")
        #for move_number in all_moves:
        if direction in valid_directions:
            break
        else:
            print("ERROR: enter a valid key")
            continue
                
    
    return direction

def place_item(game_map,tile):
    game_map[player.coordinates_y][player.coordinates_x] = tile

def interaction_decision_maker():
    pass

#function to add points to the player's score when they open a container
def container(container_string):
    #container names    
    container_name = ["c01","c02"]
    #the amount of points added when the player opens the container
    container_loot = [5,15]
    for number in range(len(container_name)):
        if container_string == container_name[number]:
            player.score += container_loot[number]

#function to run the interaction with objects
def interact(game_map):
    skip_map = False
    left_bound = player.coordinates_x -1
    right_bound = player.coordinates_x + 1
    upper_bound = player.coordinates_y -1
    lower_bound = player.coordinates_y +1
    #list of object keys found on the game map that you can interact with
    interactable_objects = ["s01","c01","c02"]
    #messages that coincide with the same index number in the interactable_objects list
    messages = ["Home\nSweet\nHome","container","container"]

    for row in range(upper_bound,lower_bound + 1):
            for length in range(left_bound, right_bound + 1): 
                if game_map[row][length] in interactable_objects:
                    current_interactable_object = game_map[row][length]
                    index_number = interactable_objects.index(current_interactable_object)
                    if messages[index_number] == "conversation":
                        interaction_decision_maker()
                        skip_map = True
                    elif messages[index_number] == "container":
                        container(interactable_objects[index_number])
                        game_map[row][length] = "[C]"
                    elif current_interactable_object == interactable_objects[index_number]:
                        print(f"{color.yellow}{messages[index_number]}{color.default}")
                        skip_map = True
    return skip_map



def player_movement (game_map):
    skip_map = False
    possible_keys = ["w","a","s","d","p","h","e"]
    key = get_player_direction(possible_keys)
    solids = ["[w]","[W]","   ","H2O"]
    hazards = ["   ", "H2O","[f]"]
    #"[w]" = wall
    #"[W]" = window
    #"   " = border
    #"H2O" = water
    index_num = [0,1,0,1]
    #the number that is added before checking to see if the new postition is an impassable object
    number_1 = [-1,-1,+1,+1]
    #the number that undoes the other number's effect if the new postion is in an inpassable object
    number_2 = [1,1,-1,-1]
    coordinate_x_or_y = [0,1,0,1]
    items = ["[w]","   "]
    for number in range(0,4):
        if key == possible_keys[number]:
                player.position_list[index_num[number]] += number_1[number]
                if coordinate_x_or_y[number] == 0:
                    player.coordinates_y += number_1[number]
                elif coordinate_x_or_y[number] == 1:
                    player.coordinates_x += number_1[number]
                for current_hazard in hazards:
                    if (game_map[player.position_list[0]][player.position_list[1]] == current_hazard):
                        player.score -= 1
                for current_solid in solids:
                    if (game_map[player.position_list[0]][player.position_list[1]] == current_solid):
                        player.position_list[index_num[number]] += number_2[number]
                        if coordinate_x_or_y[number] == 0:
                            player.coordinates_y += number_2[number]
                        elif coordinate_x_or_y[number] == 1:
                            player.coordinates_x += number_2[number]
                    elif (game_map[player.position_list[0]][player.position_list[1]] == "[c]"):
                        player.score += 1
                        game_map[player.position_list[0]][player.position_list[1]] = "[ ]"
    for number in range(4, len(possible_keys)):
        if key == possible_keys[number]:
            skip_map = interact(game_map)
            
        elif key == possible_keys[number]:
            place_item(game_map,items[number-4])

    return skip_map,game_map



def create_enemies(row,column,score,icon):
    enemy = characters.Characters(row,column,score,icon)
    return enemy



def main():
    
    game_map = [
        ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","c01","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[t]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[t]","[w]","[w]","[W]","[w]","[w]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[w]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[w]","c01","[c]","[c]","[w]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[W]","[c]","[c]","[c]","[W]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[w]","[c]","[c]","[c]","[w]","[ ]","[ ]","[ ]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","H2O","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[w]","[w]","[ ]","[w]","[w]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[t]","[ ]","[ ]","[ ]","H2O","   "],
        ["   ","[c]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","s01","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","H2O","   "],
        ["   ","[ ]","[ ]","[ ]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","H2O","H2O","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","H2O","H2O","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[c]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","H2O","H2O","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","H2O","H2O","H2O","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","H2O","H2O","H2O","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","H2O","H2O","H2O","   "],
        ["   ","[ ]","[ ]","[ ]","[c]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","H2O","H2O","H2O","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","H2O","H2O","H2O","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[b]","[b]","H2O","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[b]","[b]","[b]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[t]","[ ]","[ ]","[ ]","H2O","H2O","[b]","[ ]","[ ]","   "],
        ["   ","[ ]","[c]","[ ]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","H2O","H2O","H2O","[ ]","[ ]","   "],
        ["   ","[t]","[t]","[t]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","H2O","H2O","H2O","[ ]","[ ]","[ ]","   "],
        ["   ","[t]","[t]","[t]","[t]","[t]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","H2O","H2O","H2O","[ ]","[ ]","[ ]","   "],
        ["   ","[t]","[t]","[t]","[t]","[t]","[t]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[f]","[f]","[ ]","[ ]","[ ]","[ ]","[t]","[ ]","H2O","H2O","H2O","[ ]","[ ]","[ ]","   "],
        ["   ","[t]","[t]","[t]","[t]","[t]","[t]","[t]","[t]","[ ]","[ ]","[ ]","[ ]","[f]","[f]","[f]","[f]","[ ]","[ ]","[ ]","[ ]","H2O","H2O","H2O","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[t]","[t]","[t]","[t]","[t]","[t]","[t]","[t]","[ ]","[ ]","[ ]","[f]","[f]","[f]","[f]","[f]","[f]","[ ]","[ ]","[ ]","H2O","H2O","H2O","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[c]","[t]","[t]","[t]","[t]","[t]","[t]","[t]","[ ]","[ ]","[ ]","[f]","[f]","[f]","[f]","[f]","[f]","[ ]","[ ]","[ ]","H2O","H2O","H2O","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","c02","[c]","[t]","[t]","[t]","[t]","[t]","[ ]","[ ]","[ ]","[f]","[f]","[f]","[f]","[f]","[f]","[f]","[ ]","H2O","H2O","H2O","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
    ]
    width = len(game_map[1])
    enemy_list = []

    

    while True:
        solids = ["[w]","[W]","   "]
        skip_map, game_map = player_movement(game_map)
        left_bound = player.coordinates_x -3
        right_bound = player.coordinates_x + 3
        upper_bound = player.coordinates_y -3
        lower_bound = player.coordinates_y +3
        signs = ["s01"]
        containers = ["c01","c02"]

        #for number_of_moves in moves
        if left_bound < 0:
            left_bound = 0
        if right_bound >= width:
            right_bound = width - 1
        if upper_bound < 0:
            upper_bound = 0
        if lower_bound >= len(game_map):
            lower_bound = len(game_map)-1
        
        if skip_map == False:
            for row in range(upper_bound,lower_bound + 1):
                to_draw = ""
                for length in range(left_bound, right_bound + 1):
                    
                    #Render and color player
                    if row == player.coordinates_y and length == player.coordinates_x:
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
                    #color water
                    elif game_map[row][length] == "H2O":
                        to_draw += f"{color.blue}[W]{color.clear}"
                    #format bridges
                    elif game_map[row][length] == "[b]":
                        to_draw += f"{color.bold}{color.underline}[ ]{color.clear}"
                    #color and render signs
                    elif game_map[row][length] in signs:
                        to_draw += f"[{color.yellow}S{color.clear}]"
                    #color and render unopened containers
                    elif game_map[row][length] in containers:
                        to_draw += f"[{color.purple}c{color.clear}]"
                    #color and render opened containers
                    elif game_map[row][length] == "[C]":
                        to_draw += f"[{color.cyan}c{color.clear}]"
                    elif game_map[row][length] == "[f]":
                        to_draw += f"[{color.red}f{color.clear}]"
                    else:
                        to_draw = to_draw + game_map[row][length]
                print(to_draw)
            print(f"Score: {player.score}")
    
main()