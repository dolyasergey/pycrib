'''Helper functions'''

from itertools import combinations

def is_15(combination):
	'''Checks if a pair is a 15
	
	Parameters
	----------
	combination : tuple
		combination of card values

	Returns
	-------
	bool
		is there a 15?
	'''
	combination = list(combination)
	#transform values
	for i, value in enumerate(combination):
		if value == 'A':
			combination[i] = 1
		if value == 'J':
			combination[i] = 10
		if value == 'Q':
			combination[i] = 10
		if value == 'K':
			combination[i] = 10
	#count
	return sum(combination) == 15

def is_run_3(combination):
	'''Checks if a combination is a run of 3
	
	Parameters
	----------
	combination : tuple
		combination of three card values

	Returns
	-------
	bool
		is there a run of 3
	'''
	combination = list(combination)
	#transform values
	for i, value in enumerate(combination):
		if value == 'A':
			combination[i] = 1
		if value == 'J':
			combination[i] = 11
		if value == 'Q':
			combination[i] = 12
		if value == 'K':
			combination[i] = 13

	#sort
	sorted_comb = sorted(combination)
	#check for run
	return sorted_comb[0] + 2 == sorted_comb[1] + 1 == sorted_comb[2]


def is_run_4(combination):
	'''Checks if a combination is a run of 4
	
	Parameters
	----------
	combination : tuple
		combination of four card values

	Returns
	-------
	bool
		is there a run of 4
	'''
	combination = list(combination)
	#transform values
	for i, value in enumerate(combination):
		if value == 'A':
			combination[i] = 1
		if value == 'J':
			combination[i] = 11
		if value == 'Q':
			combination[i] = 12
		if value == 'K':
			combination[i] = 13

	#sort
	sorted_comb = sorted(combination)
	#check for run
	return sorted_comb[0] + 3 == sorted_comb[1] + 2 == sorted_comb[2] + 1 == sorted_comb[3]


def is_run_5(combination):
	'''Checks if a combination is a run of 5
	
	Parameters
	----------
	combination : tuple
		combination of five card values

	Returns
	-------
	bool
		is there a run of 5
	'''
	combination = list(combination)
	#transform values
	for i, value in enumerate(combination):
		if value == 'A':
			combination[i] = 1
		if value == 'J':
			combination[i] = 11
		if value == 'Q':
			combination[i] = 12
		if value == 'K':
			combination[i] = 13

	#sort
	sorted_comb = sorted(combination)
	#check for run
	return (sorted_comb[0] + 4 == sorted_comb[1] + 3 ==
	 sorted_comb[2] + 2 == sorted_comb[3] + 1 == sorted_comb[4])


def hand_value(hand, turnup, is_crib=False):
	'''Calculates a value of a hand
	
	Parameters
	----------
	hand : list
		4 cards in hand

	turnup: tuple
		the turnup

	is_crib: bool
		is hand a crib (default False)

	Returns
	-------
	tuple
		the score of a hand and explanation
	'''

	score = 0
	text = ''

	#check for jack-suited
	for card in hand:
		if (card[0] == 'J') and (card[1] == turnup[1]):
			score += 1
			text += 'Jack suited - 1\n'

	#check for flush
	if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1]:
		score += 4
		if turnup[1] == hand[0][1]:
			score += 1
			text += '5-card flush - 5\n'
		else:
			if is_crib:
				score -= 4
			else:
				text += '4-card flush - 4\n'

	values = [card[0] for card in hand] + [turnup[0]]

	#create combinations
	two_combs = list(combinations(values, 2))
	three_combs = list(combinations(values, 3))
	four_combs = list(combinations(values, 4))
	all_combs = two_combs + three_combs + four_combs + [tuple(values)]

	#check for pairs
	for comb in two_combs:
		if comb[0] == comb[1]:
			score += 2
			text += 'Pair of {} - 2\n'.format(comb[0])

	#check for 15s
	for comb in all_combs:
		if is_15(comb):
			score += 2
			text += '15 with {} - 2\n'.format(','.join(str(value) for value in comb))	

	#check for runs
	if is_run_5(values):
		score += 5
		text += 'Run of {} - 5\n'.format(','.join(str(value) for value in values))
	else:
		four_combo = False
		for comb in four_combs:
			if is_run_4(comb):
				score += 4
				text += 'Run of {} - 4\n'.format(','.join(str(value) for value in comb))
				four_combo = True
		if not four_combo:
			for comb in three_combs:
				if is_run_3(comb):
					score += 3
					text += 'Run of {} - 3\n'.format(','.join(str(value) for value in comb))

	text += f'____________\nFinal score is {score}'

	return score, text


	



	
	




