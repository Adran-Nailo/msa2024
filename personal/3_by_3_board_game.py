import characters
import random_letter
import random
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

player = characters.Characters(1,1,0,"[0]")


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

def player_movement (game_map):
    key = get_player_direction()
    solids = ["[w]","[W]","   "]
    possible_keys = ["w","a","s","d"]
    index_num = [0,1,0,1]
    #the number that is added before checking to see if the new postition is an impassable object
    number_1 = [-1,-1,+1,+1]
    #the number that undoes the other number's effect if the new postion is in an inpassable object
    number_2 = [1,1,-1,-1]
    coordinate_x_or_y = [0,1,0,1]

    for number in range(len(possible_keys)):
        if key == possible_keys[number]:
                player.position_list[index_num[number]] += number_1[number]
                if coordinate_x_or_y[number] == 0:
                    player.coordinates_y += number_1[number]
                elif coordinate_x_or_y[number] == 1:
                    player.coordinates_x += number_1[number]
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

def random_movement (game_map,enemy_list):
    for enemy in enemy_list:
        key = possible_keys[random.randint(0,3)]
        solids = ["[w]","[W]","   "]
        possible_keys = ["w","a","s","d"]
        index_num = [0,1,0,1]
        #the number that is added before checking to see if the new postition is an impassable object
        number_1 = [-1,-1,+1,+1]
        #the number that undoes the other number's effect if the new postion is in an inpassable object
        number_2 = [1,1,-1,-1]
        coordinate_x_or_y = [0,1,0,1]

        for number in range(len(possible_keys)):
            if key == possible_keys[number]:
                    enemy.position_list[index_num[number]] += number_1[number]
                    if coordinate_x_or_y[number] == 0:
                        enemy.coordinates_y += number_1[number]
                    elif coordinate_x_or_y[number] == 1:
                        enemy.coordinates_x += number_1[number]
                    for current_solid in solids:
                        if (game_map[enemy.position_list[0]][player.position_list[1]] == current_solid):
                            enemy.position_list[index_num[number]] += number_2[number]
                            if coordinate_x_or_y[number] == 0:
                                player.coordinates_y += number_2[number]
                            elif coordinate_x_or_y[number] == 1:
                                player.coordinates_x += number_2[number]
                        elif (game_map[player.position_list[0]][player.position_list[1]] == "[c]"):
                            player.score += 1
                            game_map[player.position_list[0]][player.position_list[1]] = "[ ]"


def create_enemies(row,column,score,icon):
    enemy = characters.Characters(row,column,score,icon)
    return enemy



def main():
    
    game_map = [
        ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[t]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[t]","[w]","[w]","[W]","[w]","[w]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[w]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[w]","[c]","[c]","[c]","[w]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[W]","[c]","[c]","[c]","[W]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[w]","[c]","[c]","[c]","[w]","[ ]","[ ]","[ ]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[w]","[w]","[ ]","[w]","[w]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[t]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[c]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[c]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[c]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[c]","[ ]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[t]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","   "],
        ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
    ]
    width = len(game_map[1])
    enemy_list = []

    

    while True:
        solids = ["[w]","[W]","   "]
        player_movement(game_map)
        left_bound = player.coordinates_x -3
        right_bound = player.coordinates_x + 3
        upper_bound = player.coordinates_y -3
        lower_bound = player.coordinates_y +3
        enemy_left_bound = player.coordinates_x -4
        enemy_right_bound = player.coordinates_x + 4
        enemy_upper_bound = player.coordinates_y -4
        enemy_lower_bound = player.coordinates_y +4

        #for number_of_moves in moves
        if enemy_left_bound < 0:
            enemy_left_bound = 0
        if enemy_right_bound >= width:
            enemy_right_bound = width - 1
        if enemy_upper_bound < 0:
            enemy_upper_bound = 0
        if enemy_lower_bound >= len(game_map):
            enemy_lower_bound = len(game_map)-1
        if left_bound < 0:
            left_bound = 0
        if right_bound >= width:
            right_bound = width - 1
        if upper_bound < 0:
            upper_bound = 0
        if lower_bound >= len(game_map):
            lower_bound = len(game_map)-1
        for row in range(enemy_upper_bound,enemy_lower_bound + 1):
            for length in range(enemy_left_bound, enemy_right_bound + 1):
                if game_map[row][length] == "[e]":
                    enemy = create_enemies(row,length,0,random_letter.Random_Letter.get_random_number())
                    enemy_list.append(enemy)
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
                #create enemies
                #Render the rest of the map
                else:
                    to_draw = to_draw + game_map[row][length]
            print(to_draw)
        print(f"Score: {player.score}")
    
main()