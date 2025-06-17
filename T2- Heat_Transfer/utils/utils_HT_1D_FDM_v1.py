# import libraries
import numpy as np

# function definition
def heat_transfer_1D_FDM(T_wall, T_inf, k, h, L, w, dx=0.01):

    # Number of nodes (including boundaries)
    # N => no. of cells
    N = int(L/dx)       # 100 intervals => 101 nodes, indexed 0 to 100
    num_nodes = N + 1

    # Create the x-coordinate array
    x = np.linspace(0, L, num_nodes)

    # Coefficient for interior nodes
    coeff_cond      = k*w/dx   # conduction term coefficient
    coeff_conv_1    = h*dx
    coeff_conv_2    = h*w

    # Initialize coefficient matrix and right-hand side vector
    A_mat = np.zeros((num_nodes, num_nodes))
    b = np.zeros(num_nodes)

    # Left boundary (Dirichlet)
    A_mat[0, 0] = 1.0
    b[0] = T_wall

    # Interior nodes: i = 1, ... , N-1 (i.e. 1 to 99)
    for i in range(1, N):
        A_mat[i, i-1] = coeff_cond
        A_mat[i, i]   = -2*(coeff_cond + coeff_conv_1)
        A_mat[i, i+1] = coeff_cond
        b[i] = -2*coeff_conv_1*T_inf

    # Right boundary (node N) with convection from the end face and lateral surface
    A_mat[N, N-1] = coeff_cond
    A_mat[N, N]   = - (coeff_cond + coeff_conv_1 + coeff_conv_2)
    b[N] = - (coeff_conv_1 + coeff_conv_2) * T_inf

    # Solve the linear system
    T = np.linalg.solve(A_mat, b) # np.matmul(np.linalg.inv(A_mat), b)

    return (x, T)

