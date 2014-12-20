from threading import Thread

# GameLogic Class
# Constructor Parameters: player, game_id, command
# -player: Player currently executing a move
# -game_id: Valid game id
# -command: AGN of a chess move.
#

class GameLogic(Thread):
	def __init__(self, game_id, player, command):
		self.game_id = game_id
		self.player = player #Black or White
		self.command_str = command
	def __load_game(game_id):
		#TODO: Loads game configuration from a database of wonders.
		# for now, use dummy data. We are effectivly 'storing' as in
		# PGN format - we turn this into usable data.
		dummy_moves = "1. e4 e5 2. Nf3 Nc6 3. Bb5 a6"
		#TODO: Need to rebuild move list in a workable game object.
		return 0
	def run(self):
		game_state = self.__load_game(self.game_id)
		#TODO: Use game state object to determine if user command is valid.
		# if so, update the game state, and then turn it back into AGN.

	
