# Examples and Visualization

This directory contains example scripts for visualizing and analyzing the simulation results.

## 📊 Visualization Script

### Prerequisites

Install Python dependencies:
```bash
pip install numpy matplotlib
```

Or using conda:
```bash
conda install numpy matplotlib
```

### Usage

1. **Run a simulation** first:
```bash
cd ..
make run-nmass   # or make run-2mass
```

2. **Visualize the results**:
```bash
cd examples
python visualize.py
```

Or specify a file:
```bash
python visualize.py ../dinamica_n_molas.txt
```

### What You'll See

#### N-Mass System
- **Line plot**: Position vs time for all masses
- **Heatmap**: Wave propagation visualization

#### 2-Mass System
- **Position plot**: Both masses' positions over time
- **Velocity plot**: Both masses' velocities over time
- **Phase space plots**: Position vs velocity (shows oscillation patterns)

## 🔬 What to Look For

### Energy Conservation
The total energy should remain approximately constant. Small variations indicate numerical error accumulation.

### Wave Propagation (N-mass)
- Initial disturbance spreads outward
- Waves reflect at boundaries
- Complex interference patterns emerge

### Beating Pattern (2-mass)
- Energy transfers between masses
- Periodic envelope modulation
- Normal mode frequencies visible

## 💡 Exercises

1. **Change initial conditions** in the C code and observe how patterns change
2. **Measure the period** of oscillation from the plots
3. **Calculate energy** at different time steps
4. **Compare different parameters** (k, m, dt)

## 📝 Creating Your Own Analysis

You can use the visualization script as a template for your own analysis:

```python
import numpy as np

# Load data
data = np.loadtxt('dinamica_n_molas.txt')
time = data[:, 0]
positions = data[:, 1:]

# Calculate velocities (numerical derivative)
dt = time[1] - time[0]
velocities = np.diff(positions, axis=0) / dt

# Calculate kinetic energy
m = 1.0  # mass
KE = 0.5 * m * np.sum(velocities**2, axis=1)

# Calculate potential energy
k = 1.0  # spring constant
PE = 0.5 * k * np.sum((positions[1:, 1:] - positions[1:, :-1])**2, axis=1)

# Total energy
E_total = KE + PE

# Plot energy conservation
import matplotlib.pyplot as plt
plt.plot(time[1:], E_total)
plt.xlabel('Time')
plt.ylabel('Total Energy')
plt.title('Energy Conservation Check')
plt.show()
```

## 🎯 Advanced Ideas

- Fourier analysis to find normal mode frequencies
- Animation of the oscillating masses
- 3D visualization of the wave propagation
- Energy spectrum analysis
- Comparison with analytical solutions

---

Happy visualizing! 📈
