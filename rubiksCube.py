# Rubiks cube object
# Contains moves you can make and data of where each square is.
class rubiksCube:
# All possible cube moves
	def left_cw():
		pass
	def left_ccw():
		pass
	def right_cw():
		pass
	def right_ccw():
		pass
	def up_cw():
		copyCube[] = cube
		for face in range(2, 6):
			for index in range(3):
				if face-1 >= 2:
					copyCube[face-1][index] = cube[face][index]
				else:
					copyCube[face+3][index] = cube[face][index]
		copyCube[1] = rotation_cw(1)
		cube = copyCube[]
	def up_ccw():
		copyCube[] = cube
		for face in range(2, 6):
			for index in range(3):
				if face+1 <= 5:
					copyCube[face+1][index] = cube[face][index]
				else:
					copyCube[face-3][index] = cube[face][index]
		copyCube[1] = rotation_ccw(1)
		cube = copyCube[]
	def down_cw():
		copyCube[] = cube
		for face in range(2, 6):
			for index in range(5,8):
				if face+1 <= 5:
					copyCube[face+1][index] = cube[face][index]
				else:
					copyCube[face-3][index] = cube[face][index]
		copyCube[0] = rotation_cw(0)
		cube = copyCube[]
	def down_ccw():
		copyCube[] = cube
		for face in range(2, 6):
			for index in range(5,8):
				if face-1 >= 2:
					copyCube[face-1][index] = cube[face][index]
				else:
					copyCube[face+3][index] = cube[face][index]
		copyCube[0] = rotation_ccw(0)
		cube = copyCube[]
	def forward_cw():
		pass
	def forward_ccw():
		pass
	def back_cw():
		pass
	def back_ccw():
		pass
# Returns the state of the cube
	def listCube():
		return(cube)
# Private data variables and functions
	private:
		def rotation_cw(face):
    		copyFace = []
    		for square in [5,3,0,6,1,7,4,2]:
        		copyFace.append(face[square])
			return copyFace
		def rotation_ccw(face):
			copyFace = []
			for square in [5,3,0,6,1,7,4,2]:
				copyFace.append(face[square])
			return copyFace
# 0 = white, 1 = yellow, 2 = red, 3 = green, 4 = orange, 5 = blue
# The cube list index represents the centre square of each side of the cube
# The elements of the side lists are indexed as so:
# [0 1 2]
# [3 i 4]
# [5 6 7]
		cube = [[0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2],[3,3,3,3,3,3,3,3],[4,4,4,4,4,4,4,4],[5,5,5,5,5,5,5,5]]
