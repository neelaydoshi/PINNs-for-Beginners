# PINNs-for-Beginners
Tutorials for understanding PINNs (Physics Informed Neural Networks) by applying them to simple physics problems.
Some examples have been solved using [PyTorch](https://pytorch.org/) library and others with [DeepXDE](https://github.com/lululxvi/deepxde) library.

PINNs are used for solving the following types of problems involving partial differential equations (PDEs):
- Forward Problem : Solving a differential equation for the given geometry, initial conditions and boundary condition.
- Inverse Problem : Estimation of unknown parameter(s) of a differential equation using observational/experimental data.

**The tutorials are in the following sequence:**
1. Pendulum Motion
   - [Forward Problem](https://github.com/neelaydoshi/PINNs-for-Beginners/blob/main/T1-%20Pendulum/pendulum_1-%20forward%20problem-%20v1.ipynb)
   - [Inverse Problem](https://github.com/neelaydoshi/PINNs-for-Beginners/blob/main/T1-%20Pendulum/pendulum_2-%20inverse%20problem-%20v1.ipynb)
2. Heat Transfer
   - [1D Forward Problem (PyTorch implementation)](https://github.com/neelaydoshi/PINNs-for-Beginners/blob/main/T2-%20Heat_Transfer/heat_transfer_1-%201D%20rod-%20PyTorch.ipynb)
   - [1D Forward Problem (DeepXDE implementation)](https://github.com/neelaydoshi/PINNs-for-Beginners/blob/main/T2-%20Heat_Transfer/heat_transfer_2-%201D%20rod-%20DeepXDE.ipynb)
   - 2D Forward Problem (coming soon)
3. Cantilever Beam Bending
   - [1D Cantilever Beam](https://github.com/neelaydoshi/PINNs-for-Beginners/blob/main/T3-%20Beam/beam_1-%201D%20cantilever.ipynb)
   - 2D Cantilever Beam (coming soon ...) 

## Results

### Heat Transfer in 1D Rod

<div align="center">
  <img src="images/1D_HT- PINN vs FDM.png" width="40%"/>
  <img src="images/1D_HT- heat_map.png" width="40%"/>
</div>

