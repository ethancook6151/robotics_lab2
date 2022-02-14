import math
import numpy as np
import p2_sol as p2

def transform_1():
  Tx = p2.trans_x(2.5)
  Tz = p2.trans_z(0.5)
  Ty = p2.trans_y(-1.5)

  v0 = p2.vec_d(0,1,1,1)

  R = np.matmul(Tx, Tz)
  R = np.matmul(R, Ty)

  v01 = R.dot(v0)
  print('Tranformation 1: \n', v01, '\n')


def transform_2():
  Tz = p2.trans_z(0.5)
  Tx = p2.trans_x(2.5)
  Ty = p2.trans_y(-1.5)

  v0 = p2.vec_d(0,1,1,1)

  R = np.matmul(Tz, Tx)
  R = np.matmul(R, Ty)

  v01 = R.dot(v0)
  print('Tranformation 2: \n', v01, '\n')


def transform_3():
  Tx = p2.trans_x(2.5)
  Tz = p2.trans_z(0.5)
  Ty = p2.trans_y(-1.5)

  v0 = p2.vec_d(0,1,1,1)

  R = np.matmul(Ty, Tz)
  R = np.matmul(R, Tx)

  v01 = R.dot(v0)
  print('Tranformation 3: \n', v01, '\n')


def transform_4():
  Tz = p2.trans_z(0.5)
  Tx = p2.trans_x(2.5)
  Ty = p2.trans_y(-1.5)

  v0 = p2.vec_d(0,1,1,1)

  R = np.matmul(Ty, Tx)
  R = np.matmul(R, Tz)

  v01 = R.dot(v0)
  print('Tranformation 4: \n', v01, '\n')


def transform_5():
  psi = math.pi/2
  phi = -math.pi/2

  Rx = p2.rot_x_d(psi)
  Tx = p2.trans_x(3)
  Tz = p2.trans_z(-3)
  Rz = p2.trans_z(phi)

  v0 = p2.vec_d(0,1,1,1)

  R = np.matmul(Rx, Tx)
  R = np.matmul(R, Tz)
  R = np.matmul(R, Rz)

  v01 = R.dot(v0)
  print('Tranformation 5: \n', v01, '\n')


if __name__ == '__main__':
  np.set_printoptions(precision=2, suppress=True)
  transform_1()
  transform_2()
  transform_3()
  transform_4()
  transform_5()

