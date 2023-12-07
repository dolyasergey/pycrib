'''Helper functions'''

def rate_to_odd(rate):
	'''Converts probability from rate format into odd format
	
	Parameters
	----------
	rate : float
		the probability of an event in rate format

	Returns
	-------
	float
		the probability of an event in odd format
	'''
	return (rate/(1 - rate))



