scene = [2, 0, 0, 1, 0, 0, 0, 2]

def game(scene):
    game = scene
    move = int
    player = 1
    enemy = 2
    player_location = int
    enemy_location = []
    final = []
    maior = len(game)
    for ind, num in enumerate(game):
        if num == enemy:
         enemy_location.append(ind)
    for indi, num_p in enumerate(game):
        if num_p == player:
         player_location = indi
    for move in enemy_location:
        if move < player_location:
            res = player_location - move
            result = res - 1
            final.append(result)
        if move > player_location:
            resu = move - player_location
            result = resu -1
            final.append(result)

    return min(final)





