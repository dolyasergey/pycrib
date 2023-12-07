from pycrib.utils import * 






	
	


class Deck_():
	'''
	A class used to represent a card deck

	Attributes
	----------
	team_id : str
		id of a team (three letters)

	name : str
		full name of a team

	lineup : dict
		team's batting order with Hitter objects

	rotation : list
		team's pitching rotation with Pitcher objects

	bullpen : tuple
		list with relief pitchers and a list of bullpen pitchers' stats

	babip : float
		batting average on balls in play (represents the level of defence)
	'''

	def __init__(self, team_id, name, lineup, rotation, bullpen_stats, bullpen_names, babip):
		'''
		Parameters
		----------
		team_id : str
			id of a team (three letters)

		name : str
			full name of a team

		lineup : dict
			team's batting order with Hitter objects

		rotation : list
			team's pitching rotation with Pitcher objects

		bullpen_stats : list
			list with stats of a bullpen

		bullpen_names : list
			list with relief pitchers' names

		babip : float
			batting average on balls in play (represents the level of defence)
		'''
		self.team_id = team_id
		self.name = name
		self.lineup = lineup
		self.rotation = rotation
		self.bullpen = (bullpen_names, bullpen_stats)
		self.babip = babip

	def __str__ (self):
		return 'Team({})'.format(self.name)
	def __repr__(self):
		return 'Team({})'.format(self.name)

