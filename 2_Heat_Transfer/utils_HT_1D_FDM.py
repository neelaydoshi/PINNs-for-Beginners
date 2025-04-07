import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


def HT_1D_FDM(L, side, dx=0.01):

    # Given parameters
    T_wall  = 100.0      # left boundary temperature [deg C]
    T_inf   = 10.0       # ambient temperature [deg C]
    k = 400.0           # thermal conductivity [W/m.K]
    h = 10.0            # convective heat transfer coefficient [W/m^2.K]

    # Cross-sectional properties (square: 0.01 m x 0.01 m)
    A = side**2     # cross-sectional area [m^2]
    P = 4*side      # perimeter [m]

    # Number of nodes (including boundaries)
    # nly: N => no. of cells
    N = int(L/dx)       # 100 intervals => 101 nodes, indexed 0 to 100
    num_nodes = N + 1

    # Create the x-coordinate array
    x = np.linspace(0, L, num_nodes)


    # Coefficient for interior nodes
    coef_cond = k * A / dx   # conduction term coefficient

    # Initialize coefficient matrix and right-hand side vector
    A_mat = np.zeros((num_nodes, num_nodes))
    b = np.zeros(num_nodes)

    # Left boundary (Dirichlet)
    A_mat[0, 0] = 1.0
    b[0] = T_wall

    # Interior nodes: i = 1, ... , N-1 (i.e. 1 to 99)
    for i in range(1, N):
        A_mat[i, i-1] = coef_cond
        A_mat[i, i]   = -2 * coef_cond - h * P * dx
        A_mat[i, i+1] = coef_cond
        b[i] = - h * P * dx * T_inf

    # Right boundary (node N = 100) with convection from the end face and lateral surface
    # Equation: (kA/dx)*(T[99]-T[100]) = [hA + hP*(dx/2)]*(T[100]-T_inf)
    A_mat[N, N-1] = coef_cond
    A_mat[N, N]   = - (coef_cond + h*A + h*P*dx/2)
    b[N] = - (h*A + h*P*dx/2) * T_inf

    # Solve the linear system
    T = np.linalg.solve(A_mat, b)

    # # nly: above is equal to taking inverse of "A_mat" and multiplying with "b"
    # T = np.matmul(np.linalg.inv(A_mat), b)

    return (x, T)
