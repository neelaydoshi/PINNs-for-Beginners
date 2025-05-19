# PINNs-for-Beginners
Tutorials for understanding PINNs (Physics Informed Neural Networks) by applying them to simple physics problems.

PINNs are used for solving the following types of problems involving partial differential equations (PDEs):
- Forward Problem : Solving a differential equation for the given geometry, initial conditions and boundary condition.
- Inverse Problem : Estimation of unknown parameter(s) of a differential equation using observational/experimental data.

**The tutorials are in the following sequence:**
1. Pendulum Motion
   - Forward Problem  
   - Inverse Problem
2. Heat Transfer
   - 1D Forward Problem (PyTorch implementation)
   - 1D Forward Problem ([DeepXDE](https://github.com/lululxvi/deepxde) implementation)
   - 2D Forward Problem (coming soon)


## Results

### Heat Transfer in 1D Rod

<p align="center">
<img src="images/1D_HT- PINN vs FDM.png" width="70%" />
<img src="images/1D_HT- heat_map.png" width="70%" />
</p>
