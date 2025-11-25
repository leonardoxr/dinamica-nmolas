# Dinâmica N-Molas (N-Springs Dynamics)

> **⚠️ Academic Project Notice**: This was a college project for computational physics. It's a simple implementation meant for educational purposes, so don't take it too seriously! The code works but isn't production-grade.

## 📖 Overview

This project implements numerical simulations of mass-spring systems using the **Verlet integration method** to solve the equations of motion for coupled harmonic oscillators. It was created as part of a computational physics course to demonstrate numerical methods for solving differential equations.

## 🎯 What Does It Do?

The repository contains two C programs that simulate different spring-mass configurations:

### 1. **dinamica_molas.c** - Two-Mass System
Simulates two masses connected by springs:
- Two masses connected in series
- Spring constants and masses can be configured
- Outputs position and velocity data over time
- Uses Verlet integration for numerical stability

### 2. **dinamica_nmolas.c** - N-Mass Chain System
Simulates a chain of N masses (default: 10) connected by springs:
- Creates a 1D chain of coupled oscillators
- All masses have fixed endpoints
- Initial displacement can be set at any position
- Demonstrates wave propagation through the system

## 🔬 Physics Background

Both programs solve the classical mechanics problem of coupled harmonic oscillators using Newton's second law:

```
F = ma
F = -k(x_i - x_j)  (Hooke's Law for springs)
```

The acceleration for each mass is calculated based on the forces from neighboring springs, and positions/velocities are updated using the **Verlet algorithm**, which is:
- Time-reversible
- Symplectic (conserves energy well)
- Second-order accurate

## 🚀 Getting Started

### Prerequisites
- GCC compiler (or any C compiler)
- Linux/Unix environment (or Windows with MinGW/Cygwin)

### Compilation

```bash
# Compile the 2-mass system
gcc -o dinamica_molas dinamica_molas.c -lm

# Compile the N-mass chain system
gcc -o dinamica_nmolas dinamica_nmolas.c -lm
```

**Note**: The `-lm` flag links the math library (required for `pow()` function).

### Running the Simulations

```bash
# Run 2-mass system
./dinamica_molas

# Run N-mass chain system
./dinamica_nmolas
```

### Output

Each program generates a text file with simulation data:
- **dinamica_molas.c** → `dinamica_mola.txt`
- **dinamica_nmolas.c** → `dinamica_n_molas.txt`

Output format:
```
time    x1    x2    x3    ...
0.00    0.0   0.1   0.0   ...
0.01    0.0   0.09  0.01  ...
...
```

## 📊 Visualizing Results

You can plot the results using Python, MATLAB, or any plotting tool. Example with Python:

```python
import numpy as np
import matplotlib.pyplot as plt

# Load data
data = np.loadtxt('dinamica_n_molas.txt')
time = data[:, 0]
positions = data[:, 1:]

# Plot position vs time for each mass
for i in range(positions.shape[1]):
    plt.plot(time, positions[:, i], label=f'Mass {i}')

plt.xlabel('Time')
plt.ylabel('Position')
plt.legend()
plt.title('N-Mass Spring System Dynamics')
plt.show()
```

## ⚙️ Configuration

You can modify simulation parameters by editing the source code:

### In `dinamica_nmolas.c`:
```c
NMAX = 10;      // Number of masses
k = 1;          // Spring constant
m = 1;          // Mass value
tmax = 1000;    // Simulation time
dt = 0.01;      // Time step
x[5] = 0.1;     // Initial displacement (mass 5 displaced by 0.1)
```

### In `dinamica_molas.c`:
```c
m1 = 1;         // Mass 1
m2 = 1;         // Mass 2
k1 = 1;         // Spring constant 1
k2 = 1;         // Spring constant 2
tmax = 100;     // Simulation time
dt = 0.01;      // Time step
```

## 📁 Project Structure

```
dinamica-nmolas/
├── README.md                  # This file
├── LICENSE                    # GPL-3.0 License
├── dinamica_molas.c          # 2-mass spring system
├── dinamica_nmolas.c         # N-mass chain system
└── .gitignore                # Git ignore file
```

## 🎓 Educational Value

This project demonstrates:
- Numerical integration methods (Verlet algorithm)
- Solving coupled differential equations
- Modeling physical systems in C
- File I/O for simulation data
- Basic computational physics workflow

## ⚠️ Known Limitations

Since this is a college project, there are several limitations:
- No input validation
- Hard-coded parameters (requires recompilation to change)
- No error handling for file operations
- Fixed array sizes (no dynamic allocation)
- Basic text file output (no binary format for efficiency)
- No command-line arguments support
- Code could use better organization and comments

These limitations are acceptable for an educational project but would need addressing for real-world applications.

## 📝 License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Since this is an archived academic project, contributions aren't actively sought. However, if you're a student learning computational physics and want to improve this code as a learning exercise, feel free to fork it!

## 📚 References

For those interested in the physics and numerical methods:
- Verlet integration: https://en.wikipedia.org/wiki/Verlet_integration
- Harmonic oscillator: https://en.wikipedia.org/wiki/Harmonic_oscillator
- Coupled oscillators: https://en.wikipedia.org/wiki/Coupled_oscillators

## 👨‍🎓 Author

Created as a college/university computational physics project.

---

**Remember**: This is educational code from a college course. It works and demonstrates the concepts, but it's not meant to be production-quality software. Use it to learn, experiment, and maybe improve upon as an exercise! 🎓
