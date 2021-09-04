class Player(object):
    prev_health = 20
    def play_turn(self, warrior):
        if warrior.feel().is_captive():
            warrior.rescue_()
        elif warrior.feel().is_empty():
            if warrior.health() == 20 or self.prev_health > warrior.health():
                warrior.walk_() 
            else:
                warrior.rest_()
        else:
            warrior.attack_()
        self.prev_health = warrior.health()
        return None  # Your code here