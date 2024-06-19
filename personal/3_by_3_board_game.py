def get_player_direction():
    while True:
        valid_directions = ["w","a","s","d"]
        direction = input("Enter direction key: ")
        if direction.lower in valid_directions:
            break
        print("ERROR: enter a valid direction key")
        continue
    return direction
        



def main():
    game_map = [
        ["[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]"]
    ]
    player_position = [1,1]

    while True:
        direction = get_player_direction()
        if direction == "w":
            player_position[0] = player_position[0]+1
        
        game_map[player_position[0]][player_position[1]] = "[0]"
        for row in range(len(game_map)):
            to_draw = ""
            for length in range(len(game_map[row])):
                to_draw = to_draw + game_map[row][length]
            print(to_draw)
    
main()