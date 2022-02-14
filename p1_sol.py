import rbm
import math 
import numpy as np 

if __name__ == '__main__':
  np.set_printoptions(precision=2, suppress=True)

  psi = math.pi/2
  theta = math.pi/2
  phi = math.pi/2 

  # Test vector 
  v0 = rbm.vec(0,1,1)

  Rx = rbm.rot_x(psi)
  Ry = rbm.rot_y(theta)
  Rz = rbm.rot_z(phi)

# Fixed Frame: 
# Rotation z ,Rotation y ,Rotation x
  R = np.matmul(Rz, Ry)
  R = np.matmul(R, Rx)
  v01 = R.dot(v0)
  print('Fixed: \n', v01)
