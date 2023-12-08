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

