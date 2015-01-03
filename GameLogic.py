from threading import Thread

def an_to_num(cord):
	return (ord(cord[1]) - ord('1'), ord(cord[0]) - ord('a'))
def num_to_an(row,col):
	return "{}{}".format(chr(col + ord('a')), row + 1)

#GamePiece class
class GamePiece:
	def __init__(self, typ, team, position):
		self.team = team
		self.position = position
		self.typ = typ
		self.victims = []
		self.killer = None
	def get_kills():
		return self.victims
	def get_killer():
		return self.killer
	def __is_teamKill(pieces, move):
		for cur in pieces:
			if cur is self:
				continue
			if (cur.team == self.team) and (cur.position == move)
				return True
		return False
	def get_valid_moves(pieces):
			moves = []
			row,col = an_to_num(self.position)
			if self.typ == "P":
				if self.team == 'W':
					if ((row + 1) < 8) and not (self.__is_teamKill(num_to_an(row + 1, col))):
						moves.append(num_to_an(row + 1, col))
						if (row == 1) and ((row + 2) < 8):
							if not self.__is_teamKill(num_to_an(row + 2, col)):
								moves.append(num_to_an(row + 2, col))
				else
					if ((row - 1) >= 0) and not (self.__is_teamKill(num_to_an(row - 1, col))):
						moves.append(num_to_an(row - 1, col))
						if (row == 6) and ((row - 2) >= 0):
							if not self.__is_teamKill(num_to_an(row - 2, col)):
								moves.append(num_to_an(row - 2, col))
				#TODO: Still need to do captures, and en-passante (lol spelling)
				# also don't forget promotions.
			elif self.typ == "K":
				for i in range(row - 1, row + 1 + 1):
					if (i < 0) or (i > 7):
						continue
					for j in range(col - 1, col + 1 + 1):
						if (j < 0) or (j < 7):
							continue
						if (i == row) and (j == col):
							continue
						if self.__is_teamKill(pieces, num_to_an(i,j)):
							continue
						#FIXME: Putting the king into check ISN'T VALID. Need to enforce this.
						moves.append(num_to_an(i, j))
			elif self.typ == "Q":
				pass
			elif self.typ == "B":
				pass
			elif self.typ == "N":
				pass
			elif self.typ == "R":
				pass

			return moves
# GameState class
class GameState:
	def __init__(self):
		# List of all pieces currently in play.
		self.pieces = []
		# List of all captured pieces (with their point of capture)
		self.captured = []
		self.current_move = 'W'
		
		# Create the pawns
		for i in range(16):
			pos = "{}{}".format(chr(ord('a') + (i % 8) ), (2 if i < 8 else 7))
			cursor = GamePiece('P', ('W' if i < 8 else 'B'), pos)
			self.pieces.append(cursor)
		# Kings
		self.pieces.append(GamePiece('K', 'W', "e1"))
		self.pieces.append(GamePiece('K', 'B', "e8"))
		# Queens
		self.pieces.append(GamePiece('Q', 'W', "d1"))
		self.pieces.append(GamePiece('Q', 'B', "d8"))
		# Bishops
		self.pieces.append(GamePiece('B', 'W', "c1"))
		self.pieces.append(GamePiece('B', 'W', "f1"))
		self.pieces.append(GamePiece('B', 'B', "c8"))
		self.pieces.append(GamePiece('B', 'B', "f8"))
		# Knights
		self.pieces.append(GamePiece('N', 'W', "b1"))
		self.pieces.append(GamePiece('N', 'W', "g1"))
		self.pieces.append(GamePiece('N', 'B', "b8"))
		self.pieces.append(GamePiece('N', 'B', "g8"))
		# Rooks
		self.pieces.append(GamePiece('R', 'W', "a1"))
		self.pieces.append(GamePiece('R', 'W', "h1"))
		self.pieces.append(GamePiece('R', 'B', "a8"))
		self.pieces.append(GamePiece('R', 'B', "h8"))

	def __parse_game(moves_string):
		move_list = re.split("[0-9]+[.]", moves_string)
		del move_list[0] # First element will always be empty after split.

		# Iterate through the elements of the move string.
		for movestr in move_list:
			Wmove,Bmove = movestr.strip().split(' ')

			# Process white move
			match = re.search('[KQBNR]', Wmove)
			if match:
				piece = match.group()[0]
			elif Wmove[0] == 'O':
				#TODO: Either right/left castling.
				pass
			else:
				piece = 'P'
				#FIXME: Need to look for promotion

			start,dest = re.split("[-x]", Wmove.lstrip(piece))

			for cursor in self.pieces:
				if cursor.position == start:
					if cursor.typ != piece:
						#FIXME: (EEKAHN) Pass for now, but this would be bad.
						pass
					self.__move_piece(cursor, dest)
					# TODO: For promotion, may want to check if the piece was
					# promoted here.
			
	def __move_piece(piece, dest):
		#FIXME: (EEKAHN) Resume here.
		temp_state = list(self.pieces)
		if piece.typ == 'K':
			pass
		elif piece.typ == 'Q':
			pass
		elif piece.typ == 'B':
			pass
	def __do_castle(team, side):
		# team = 'W' or 'B'
		# side = 'K' or 'Q' (Kingside/queenside)
		pass
	def __str__(self):
		return "Oh....hi...didn't think you were gonna look here ''':|"

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
		dummy_moves = "1. e2-e4 e7-e5 2. Ng1-f3 Nb8-c6 3. Bf1-b5 a7-a6"
		#TODO: Need to rebuild move list in a workable game object.
		return 0
	def run(self):
		game_state = self.__load_game(self.game_id)
		#TODO: Use game state object to determine if user command is valid.
		# if so, update the game state, and then turn it back into AGN.

	
