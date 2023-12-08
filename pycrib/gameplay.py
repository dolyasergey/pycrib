from pycrib.utils import * 
from random import choices

class Deck():
	'''
	A class used to represent a card deck

	Attributes
	----------
	cards : list
		list of cards

	'''

	def __init__(self, cards=[]):
		'''
		Parameters
		----------
		cards: list
			list of cards which make up a deck
		'''
		self.cards = cards
		if cards == []:
			suits = ['C', 'D', 'S', 'H']
			values = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
			for suit in suits:
				for value in values:
					self.cards.append((value, suit))

	def draw(self, n=6):
		'''
		A function to draw n cards from a deck

		Parameters
		----------
		n : int
			number of cards to draw

		Returns
		-------
		list
			a draw of n cards
		'''
		return choices(self.cards, k=n)

	def remaining(self, excluded):
		'''
		A function to check the remaining cards

		Parameters
		----------
		excluded : list
			list of cards to exlude

		Returns
		-------
		Deck
			a Deck with only cards left
		'''
		return Deck([card for card in self.cards if card not in excluded])

	def __str__ (self):
		return 'Deck of cards'
	def __repr__(self):
		return 'Deck of cards'

class Game():
	'''
	A class used to represent a game

	Attributes
	----------
	player1 : string
		name of player 1

	player2 : string
		name of player 2

	target_score : int
		target score of a game (default 121)

	p1_score: int
		a score of Player 1

	p2_score: int
		a score of Player 2

	dealer: int
		[0,1] is Player 1 or Player 2 a dealer

	'''
	def __init__(self, player1='Player 1', player2='Player 2', target_score=121):
		'''
		Parameters
		----------
		player1 : string
			name of player 1

		player2 : string
			name of player 2

		target_score : int
			target score of a game (default 121)

		'''
		self.player1 = player1
		self.player2 = player2
		self.target_score = target_score
		self.p1_score = 0
		self.p2_score = 0
		self.dealer = 0


class Turn():
	'''
	A class used to represent a turn

	Attributes
	----------
	dealer: int
		[0,1] is Player 1 or Player 2 a dealer

	player1 : string
		name of player 1

	player2 : string
		name of player 2

	deck: Deck
		deck of cards used for a turn

	'''
	def __init__(self, dealer, player1='Player 1', player2='Player 2'):
		'''
		Parameters
		----------
		dealer: int
			[0,1] is Player 1 or Player 2 a dealer

		player1 : string
			name of player 1

		player2 : string
			name of player 2
		'''
		self.dealer = dealer
		self.player1 = player1
		self.player2 = player2

		self.deck = Deck()
		self.p1_draw = self.deck.draw()
		self.p2_draw = self.deck.remaining(self.p1_draw).draw()
		self.turnup = self.deck.remaining(self.p1_draw + self.p2_draw).draw(1)[0]
