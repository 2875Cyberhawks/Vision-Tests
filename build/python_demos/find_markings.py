import pixy
import math
from ctypes import *
from pixy import *
from networktables import NetworkTables
from time import sleep

print "Starting networktables"

NetworkTables.initialize(server='roboRIO-2875-FRC.local') # USB: 172.22.11.2
sd = NetworkTables.getTable("data")

print "Starting pixy"

pixy.init()

print "Changing program"

pixy.change_prog("line")

vects = VectorArray(1)

print "Loop begin"


while True:
	res = line_get_main_features()
	
	hasVec = line_get_vectors(1, vects) == 1

	sd.putBoolean("FD", hasVec)

	if hasVec:
		print "Found vector (" + str(vects[0].m_x1) + ", " + str(vects[0].m_y1) + ") -> (" + str(vects[0].m_x0) + ", " + str(vects[0].m_x1) + ")"
		sd.putNumber("HX", vects[0].m_x1)
		sd.putNumber("HY", vects[0].m_y1)
		sd.putNumber("TX", vects[0].m_x0)
		sd.putNumber("TY", vects[0].m_y0)
	else:
		print "Found no vector"
		sd.putNumber("HX", -1)
		sd.putNumber("HY", -1)
		sd.putNumber("TX", -1)
		sd.putNumber("TY", -1)
