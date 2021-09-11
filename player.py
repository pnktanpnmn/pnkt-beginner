class Player(object):
    def play_turn(self, warrior):
        current = warrior.health()
        if current < 20 and warrior.feel('backward').is_wall():
            warrior.rest_()
        elif current < 10:
            warrior.walk_('backward')
        elif warrior.feel().is_wall():
            warrior.pivot_()
        elif warrior.feel().is_empty():
            warrior.walk_()
        else:
            warrior.attack_()
        return None  # Your code here