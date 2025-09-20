class Characters():
    def __init__(self,coordinates_x,coordinates_y,score,icon,current_map,health,damage,sword_count,potion_count,wall_count,render_distance,basic_attack_unlocked,advanced_attack_unlocked,armor,basic_shield,advanced_shield,block):
        self.position_1 = coordinates_x
        self.position_2 = coordinates_y
        self.coordinates_x = coordinates_x
        self.coordinates_y = coordinates_y
        self.score = score
        self.icon = icon
        self.position_list = [self.coordinates_y,self.coordinates_x]
        self.current_map = current_map
        self.sword_count = sword_count
        self.potion_count = potion_count
        self.wall_count = wall_count
        self.render_distance = render_distance
        self.health = health
        self.basic_attack_unlocked = basic_attack_unlocked
        self.advanced_attack_unlocked = advanced_attack_unlocked
        self.damage = damage
        self.armor = armor
        self.basic_shield = basic_shield
        self.advanced_shield = advanced_shield
        self.block = block