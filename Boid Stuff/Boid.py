class Boid:
# == Class Start
	def __init__(self, v, p, s, d):
		self.velocity = v
		self.position = p
		self.speed = s
		self.direction = d
#################################################
	# Print Statements
	def printVelocity(self):
		print('Velocity: \t', self.velocity)
	def printPosition(self):
		print('Position: \t', self.position)
	def printDirection(self):
		print('Direction: \t', self.direction)
	def printSpeed(self):
		print('Speed: \t\t', self.speed)
#################################################
	# Getters / Setters
	def getVelocity(self):
		return self.velocity
	def setVelocity(a):
		self.velocity = a
#####
	def getPosition(self):
		return self.position
	def setPosition(a):
		self.position = a
#####
	def getDirection(self):
		return self.direction
	def setDirection(a):
		self.direction = a
#####
	def getSpeed(self):
		return self.speed
	def setSpeed(a):
		self.speed = a
#################################################



# == Class End