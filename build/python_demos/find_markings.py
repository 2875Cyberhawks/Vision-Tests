import pixy
import math
from ctypes import *
from pixy import *

print "Code Start"

pixy.init()

print "Pixy Initialized"

pixy.change_prog("line")

print "Line Program Set"

vects = VectorArray(1)

DEAD = 5

get_resolution()

WIDTH = pixy.frame_width

class Mark:
	MIN_LEN = 10
	MIN_ANG = 20
	
	def __init__(self, vect):
		self.head = (vect.m_x1, vect.m_y1)
		self.tail = (vect.m_x0, vect.m_y0)
	
	def __str__(self):
		return "(" + str(self.length()) + "," + str(self.getAngle()) + ") @ " + str(self.getCent())
		# return "<" + str(self.getX()) + "," + str(self.getY()) + "> @ " + str(self.getCent())

	def length(self):
		return math.hypot(self.getX(), self.getY())

	def isValid(self):
		return self.length() > Mark.MIN_LEN and self.getY() > self.getX()
	
	def getX(self):
		return self.head[0] - self.tail[0]
	
	def getY(self):
		return -self.head[1] + self.tail[1] # Negative b/c of reversed Y direction
	
	def getCent(self):
		return ((self.head[0] + self.tail[0]) / 2, (self.head[1] + self.tail[1]) / 2)
	
	def getAngle(self):
		x, y = self.getX(), self.getY()
		sign = 1
		if (x < 0):
			sign = -1
		return sign * int(math.degrees(math.atan(float(x) / float(y))))
	
	def isStraight(self):
		return abs(self.getAngle()) < Mark.MIN_ANG

while True:
	res = line_get_main_features()
	
	hasVec = line_get_vectors(1, vects) != 0
	
	if not hasVec:
		print "Found no vectors"
		continue
	
	mark = Mark(vects[0])
	
	if not mark.isValid():	
		print "Found no significant vectors"
		continue
		
	angErr = -mark.getAngle()
	posErr = 0
	
