
#class definition for an n-sided die
#import packages
import random

class MSdie:
	#Current die value
	value = None
	nos = 6
	#constructor here
	def __init__(self):	
		return
	#define classmethod 'roll' to roll the MSdie
	@classmethod
	def roll(cls):
		cls.n_value = random.randint(1, cls.nos)
		return cls.n_value

    #define classmethod 'getValue' to return the current value of the MSdie
	@classmethod
	def getValue(cls):
		return cls.value

	#define classmethod 'setValue' to set the die to a particular value
	@classmethod
	def setValue(cls):
		n_val = cls.roll()
		return n_val
die = MSdie().setValue()
print(die)