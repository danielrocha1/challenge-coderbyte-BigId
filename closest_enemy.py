scene = [2,0,0,2,0,1,0]

def game(scene):
	game = scene
	move = int
	player = 1
	enemy = 2
	player_location = int
	enemy_location = []
	pos = int
	for enemy in game:
		pos = game.index(enemy)
		enemy_location.append(pos)
	for player in game:
		player_location = game.index(player)
	for location in enemy_location:
		if location < player_location:
			move = location - player_location  
		else:
		 	move = player_location - location
	return move	 	
	  		
		
		