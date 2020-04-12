import math

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

def determine_enemy_speed_range(SCREEN_WIDTH):
    x = SCREEN_WIDTH / 666
    y = SCREEN_WIDTH / 400
    return x, y