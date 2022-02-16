import math
import numpy as np

# Translate on the x axis
def trans_x(a):
  trans = np.array([[1.0, 0.0, 0.0, a],
				            [0.0, 1.0, 0.0, 0.0],
					          [0.0, 0.0, 1.0, 0.0],
                    [0.0, 0.0, 0.0, 1.0]])
  return trans


# Translate on the y axis
def trans_y(b):
  trans = np.array([[1.0, 0.0, 0.0, 0.0],
				            [0.0, 1.0, 0.0, b],
					          [0.0, 0.0, 1.0, 0.0],
                    [0.0, 0.0, 0.0, 1.0]])
  return trans


# Translate on the z axis
def trans_z(c):
  trans = np.array([[1.0, 0.0, 0.0, 0.0],
				            [0.0, 1.0, 0.0, 0.0],
					          [0.0, 0.0, 1.0, c],
                    [0.0, 0.0, 0.0, 1.0]])
  return trans


# Rotate on the x axis
def rot_x_d(theta):
	rot = np.array([[1.0,  0.0, 0.0, 0.0],
				          [0.0, math.cos(theta), -math.sin(theta), 0.0],
					        [0.0, math.sin(theta), math.cos(theta), 0.0],
                  [0.0, 0.0, 0.0, 1.0]])
	return rot
	
	

# Rotate on the y axis
def rot_y_d(theta):
	rot = np.array([[math.cos(theta), 0.0, math.sin(theta), 0.0],
				          [0.0, 1.0, 0.0, 0.0],
					        [-math.sin(theta), 0.0, math.cos(theta), 0.0],
                  [0.0, 0.0, 0.0, 1.0]])
	return rot



# Rotate on the z axis
def rot_z_d(theta):
	rot = np.array([[math.cos(theta),  -math.sin(theta), 0.0, 0.0],
					        [math.sin(theta),   math.cos(theta), 0.0, 0.0],
				          [0.0, 0.0, 1.0, 0.0],
                  [0.0, 0.0, 0.0, 1.0]])
	return rot
	
	
	
def vec_d(x,y,z,d):
#	Define a vector as an numpy and transpose it to a column vector.
	vec = np.array([[x, y, z, d]]).T 
	return vec
