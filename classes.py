### GapSim v0.1 - A Perfect Car Parking Simulator ###

from __future__ import print_function
import random

class Street(object):
	"""
	single empty street object
	"""

	def __init__(self, space):
		self.space = space
		self.s_taken = 0

	def get_space(self):
		return self.space

	def get_s_taken(self):
		return self.s_taken

	def update_s_taken(self, space):
		self.s_taken += space
		print(str(space)+' meters have been taken')




class Car(object):
	"""
	basic car object with defined length
	"""

	def __init__(self, length):
		self.length = length

	def get_length(self):
		return self.length

class Car_random(object):
	"""
	basic car object with random length
	"""

	def __init__(self):
		self.length = 3+3*random.random()

	def get_length(self):
		return self.length

