#!/usr/bin/python
# Filename: 

class Robot:
	'''Represents a robot, wiht a name.'''

	population = 0

	def __init__(self, name):
		''' Initializes the data.'''
		self.name = name
		print('Initializing {0}'.format(self.name))
		Robot.population += 1
	def __del__(self):
		'''I am dying.'''
		print('{0} is being destroyed!'.format(self.name))
		Robot.population -= 1
		
		if Robot.population == 0:
			print('{0} was the last one.'.format(self.name))
		else:
			print('There are still {0:d} robots working.'.\
			format(Robot.population))

	def sayHi(self):
		'''Greeting by the robot.
		
		Yeah, they can do that.'''
		print('Greetings, my masters call me {0}.'.format(self.name))

	def howMany():
		'''Prints the current population.'''
		print('We have {0:d} robots.'.format(Robot.population))
	howmany = staticmethod(howMany)

droid1 = Robot('Zhangpeiling')
droid1.sayHi()
Robot.howMany()

droid2 = Robot('Wangjianqin')
droid2.sayHi()
Robot.howMany()

print('\nRobots can do some work here.\n')

print("Robots have finished their work. So let't destroy them.")

del droid1
del droid2

Robot.howMany()
