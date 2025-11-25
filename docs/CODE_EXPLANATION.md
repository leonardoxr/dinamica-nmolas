# Code Explanation

This document provides a detailed walkthrough of the code implementation.

## 📁 File Overview

### dinamica_nmolas.c
Simulates N masses in a chain connected by springs

### dinamica_molas.c
Simulates 2 masses connected by springs

---

## 🔍 Detailed Code Analysis

## dinamica_nmolas.c - N-Mass Chain System

### Includes and Function Declaration

```c
#include<stdio.h>   // For file I/O (fprintf, fopen, fclose)
#include<math.h>    // For pow() function
#include<string.h>  // Not actually used
#include<stdlib.h>  // Not actually used

// Function to calculate acceleration of a mass
double a(double x_atual, double x_anterior, double x_seguinte, double k, double m);
```

### Variable Initialization

```c
FILE *arq;
arq = fopen("dinamica_n_molas.txt", "w+");  // Open output file

int NMAX = 10;      // Number of masses
int tmax = 1000;    // Total simulation time
double dt = 0.01;   // Time step
double m = 1;       // Mass of each mass point
double k = 1;       // Spring constant
```

### Array Declarations

```c
double ac[NMAX];         // Current acceleration
double ac_antigo[NMAX];  // Previous acceleration (for Verlet)
double x[NMAX];          // Position array
double v[NMAX];          // Velocity array
```

### Initial Conditions

```c
for(j = 0; j < NMAX; j++) {
    x[j] = 0;           // All positions at equilibrium
    v[j] = 0;           // All velocities zero
    ac_antigo[j] = 0;   // All accelerations zero
}
x[5] = 0.1;  // Displace mass 5 by 0.1 units
```

This creates a localized perturbation that will propagate through the chain.

### Main Time Loop

The simulation uses the **Verlet integration algorithm**:

```c
for(t = 0; t < tmax; t = t + dt) {
    // 1. Calculate accelerations at current positions
    // 2. Update positions
    // 3. Calculate new accelerations
    // 4. Update velocities
    // 5. Write data to file
}
```

#### Step 1: Calculate Current Accelerations

```c
for(j = 1; j < NMAX-1; j++) {
    ac_antigo[j] = a(x[j], x[j-1], x[j+1], k, m);
}
```

**Why j=1 to NMAX-2?**
- `j=0` and `j=NMAX-1` are boundary masses (fixed to walls)
- Only interior masses can move
- Each mass needs neighbors on both sides

#### Step 2: Update Positions (Verlet)

```c
for(j = 1; j < NMAX-1; j++) {
    x[j] = x[j] + v[j]*dt + 0.5*ac_antigo[j]*pow(dt,2);
}
```

This is the **position update** formula:
```
x(t+Δt) = x(t) + v(t)·Δt + ½·a(t)·Δt²
```

#### Step 3: Calculate New Accelerations

```c
for(j = 1; j < NMAX-1; j++) {
    ac[j] = a(x[j], x[j-1], x[j+1], k, m);
}
```

Recalculate accelerations at the new positions.

#### Step 4: Update Velocities (Verlet)

```c
for(j = 1; j < NMAX-1; j++) {
    v[j] = v[j] + 0.5*(ac_antigo[j] + ac[j])*dt;
    ac[j] = ac_antigo[j];  // Save for next iteration
}
```

This is the **velocity update** formula:
```
v(t+Δt) = v(t) + ½·[a(t) + a(t+Δt)]·Δt
```

Uses the average of old and new accelerations for better accuracy.

#### Step 5: Write to File

```c
fprintf(arq, "%lf\t", t);           // Time
for(j = 0; j < NMAX; j++) {
    fprintf(arq, "%lf\t", x[j]);    // Position of each mass
}
fprintf(arq, "\n");
```

### Acceleration Function

```c
double a(double x_atual, double x_anterior, double x_seguinte, double k, double m)
{
    double ac;
    ac = (-k*(x_atual - x_anterior) + k*(x_seguinte - x_atual))/m;
    return ac;
}
```

**Parameter meanings:**
- `x_atual` = current position (xᵢ)
- `x_anterior` = previous neighbor (xᵢ₋₁)
- `x_seguinte` = next neighbor (xᵢ₊₁)

**Physics:**
```
Force from left spring:   F_left  = -k·(xᵢ - xᵢ₋₁)
Force from right spring:  F_right =  k·(xᵢ₊₁ - xᵢ)
Total force:              F_total = F_left + F_right
Acceleration:             a = F_total / m
```

Simplified:
```
a = k·(xᵢ₋₁ - 2xᵢ + xᵢ₊₁) / m
```

---

## dinamica_molas.c - Two-Mass System

### Variable Initialization

```c
double m1 = 1, m2 = 1;           // Masses
double k1 = 1, k2 = 1;           // Spring constants
double k12 = 1;                   // Coupling spring constant
double x1, x2;                    // Positions
double v1 = 0, v2 = 0;           // Velocities (start at rest)
double a1, a2;                    // Accelerations
double y1 = 1, y2 = 2;           // Equilibrium positions
double d1 = 1, d2 = 1, d3 = 1;   // Natural spring lengths
```

### Initial Conditions

```c
x1 = (y1 - d1) + 0.1;  // Mass 1 displaced by 0.1
x2 = (y2 - d1 - d2);   // Mass 2 at equilibrium
```

### Main Time Loop

```c
for(t = 0; t < tmax; t = t + dt) {
    // Calculate current accelerations
    a1 = a(x1, x2, k1, m1);
    a2 = a(x2, x1, k2, m2);

    // Update positions (Verlet)
    x1 = x1 + v1*dt + 0.5*a1*pow(dt,2);
    x2 = x2 + v2*dt + 0.5*a2*pow(dt,2);

    // Update velocities (Verlet)
    v1 = v1 + 0.5*(a1 + a(x1, x2, k1, m1))*dt;
    v2 = v2 + 0.5*(a2 + a(x2, x1, k2, m2))*dt;

    // Write to file
    fprintf(arq, "%lf %lf %lf %lf %lf\n", t, x1, v1, x2, v2);
}
```

**Same Verlet algorithm as N-mass system**, just for 2 masses.

### Acceleration Function

```c
double a(double x1, double x2, double k1, double m1)
{
    double ac;
    ac = ((-(k1 + k12)*x1) + k12*x2) / m1;
    return ac;
}
```

**Physics for Mass 1:**
```
Force from left spring:     F₁ = -k₁·x₁
Force from coupling spring: F₁₂ = -k₁₂·(x₁ - x₂)
Total force:                F = -k₁·x₁ - k₁₂·x₁ + k₁₂·x₂
                            F = -(k₁ + k₁₂)·x₁ + k₁₂·x₂
Acceleration:               a₁ = F / m₁
```

---

## 🎯 Key Programming Concepts

### 1. Verlet Integration Pattern

```c
// Step 1: Calculate a(t)
a_old = calculate_acceleration(x);

// Step 2: Update x(t) → x(t+dt)
x = x + v*dt + 0.5*a_old*dt²;

// Step 3: Calculate a(t+dt)
a_new = calculate_acceleration(x);

// Step 4: Update v(t) → v(t+dt)
v = v + 0.5*(a_old + a_new)*dt;
```

### 2. Boundary Conditions

The N-mass system uses **fixed boundary conditions**:
- Mass 0 and mass N-1 are fixed to walls (x=0)
- Only interior masses (1 to N-2) can move
- Loop indices reflect this: `for(j=1; j<NMAX-1; j++)`

### 3. File I/O

```c
FILE *arq;
arq = fopen("output.txt", "w+");  // Open for writing
fprintf(arq, "%lf\t", value);     // Write formatted data
fclose(arq);                       // Close when done
```

### 4. Array Indexing

```c
ac_antigo[j] = a(x[j], x[j-1], x[j+1], k, m);
                  //  current ↑    ↑ left    ↑ right neighbor
```

Each mass needs its neighbors to calculate the net force.

---

## ⚠️ Potential Issues and Improvements

### Issues

1. **No bounds checking**: Could access x[-1] or x[NMAX] if loops are wrong
2. **No error handling**: fopen() could fail, no check
3. **Hard-coded NMAX**: Fixed array size limits flexibility
4. **No input validation**: Negative masses or k values would cause problems
5. **Magic numbers**: Constants like 0.1, 0.01 scattered in code

### Improvements

1. **Dynamic allocation**: Use malloc() for arbitrary N
2. **Parameter validation**: Check for k>0, m>0, dt>0
3. **Energy monitoring**: Calculate and print total energy
4. **Modular design**: Separate physics, I/O, and integration
5. **Configuration files**: Read parameters from external file
6. **Command-line args**: Allow user to set N, k, m, dt
7. **Error handling**: Check all I/O operations

---

## 🧪 Testing the Code

### Compile
```bash
gcc -o dinamica_nmolas dinamica_nmolas.c -lm -Wall -Wextra
```

The `-Wall -Wextra` flags enable helpful warnings.

### Run
```bash
./dinamica_nmolas
```

### Verify Output
```bash
# Check file was created
ls -lh dinamica_n_molas.txt

# View first few lines
head -20 dinamica_n_molas.txt

# Count number of timesteps
wc -l dinamica_n_molas.txt
```

Expected: ~100,000 lines (tmax/dt = 1000/0.01)

---

## 📊 Understanding the Output

### Format
```
time    x[0]  x[1]  x[2]  ...  x[9]
0.00    0.0   0.0   0.0   ...  0.0
0.01    0.0   0.0   0.0   ...  0.001
...
```

### What to Look For
- **Wave propagation**: Disturbance spreads from x[5]
- **Energy conservation**: Sum of kinetic + potential should be constant
- **Periodicity**: System should return to initial state (approximately)
- **Symmetry**: Wave should propagate equally in both directions

---

## 🔬 Experimental Ideas

1. **Change initial conditions**: Try x[0]=0.1 instead of x[5]=0.1
2. **Vary parameters**: Try k=2, m=2, see how frequency changes
3. **Multiple perturbations**: Set x[3]=0.1 and x[7]=0.1
4. **Larger systems**: Change NMAX to 50 or 100
5. **Different boundary conditions**: Make x[0] and x[NMAX-1] free

---

This concludes the code explanation! 🎓
