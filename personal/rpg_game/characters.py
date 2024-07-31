class Characters():
    def __init__(self,position_1,position_2,score,icon,current_map):
        self.position_1 = position_1
        self.position_2 = position_2
        self.coordinates_x = position_1
        self.coordinates_y = position_2
        self.score = score
        self.icon = icon
        self.position_list = [self.coordinates_y,self.coordinates_x]
        self.current_map = current_map
        self.sword_count = 0
        self.potion_count = 0
        self.wall_count = 0
        self.render_distance = 3