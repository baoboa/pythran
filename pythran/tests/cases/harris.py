#from parakeet testbed
#runas import numpy as np ; M, N = 4, 6 ; I = np.arange(M*N, dtype=np.float64).reshape(M,N) ; harris(I)
#bench import numpy as np ; M, N = 6000, 4000 ; I = np.arange(M*N, dtype=np.float64).reshape(M,N) ; harris(I)

#pythran export harris(float64[][])
import numpy as np



def harris(I):
  m,n = I.shape
  dx = (I[1:, :] - I[:m-1, :])[:, 1:]
  dy = (I[:, 1:] - I[:, :n-1])[1:, :]

  #
  #   At each point we build a matrix
  #   of derivative products
  #   M =
  #   | A = dx^2     C = dx * dy |
  #   | C = dy * dx  B = dy * dy |
  #
  #   and the score at that point is:
  #      det(M) - k*trace(M)^2
  #
  A = dx * dx
  B = dy * dy
  C = dx * dy
  tr = A + B
  det = A * B - C * C
  k = 0.05
  return det - k * tr * tr
