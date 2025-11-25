# Physics Documentation

## Overview

This document explains the physics and mathematics behind the spring-mass simulations implemented in this project.

## 🎯 Physical System

### Two-Mass System (dinamica_molas.c)

The system consists of two masses connected by springs:

```
Wall ----[k1]---- M1 ----[k12]---- M2 ----[k2]---- Wall
         spring   mass    spring    mass   spring
```

### N-Mass Chain System (dinamica_nmolas.c)

A chain of N masses connected by springs with fixed endpoints:

```
Wall ----[k]---- M1 ----[k]---- M2 ----[k]---- ... ----[k]---- Mn ---- Wall
```

## 📐 Mathematical Model

### Newton's Second Law

The motion of each mass is governed by Newton's second law:

```
F = ma
```

Where:
- `F` = net force on the mass
- `m` = mass
- `a` = acceleration

### Hooke's Law

The force exerted by a spring is proportional to its displacement:

```
F = -k(x - x₀)
```

Where:
- `k` = spring constant (stiffness)
- `x` = current position
- `x₀` = equilibrium position (natural length)

### Equations of Motion

#### For the Two-Mass System:

**Mass 1:**
```
m₁ · a₁ = -k₁·x₁ - k₁₂·(x₁ - x₂)
a₁ = -(k₁ + k₁₂)·x₁/m₁ + k₁₂·x₂/m₁
```

**Mass 2:**
```
m₂ · a₂ = -k₁₂·(x₂ - x₁) - k₂·x₂
a₂ = k₁₂·x₁/m₂ - (k₁₂ + k₂)·x₂/m₂
```

#### For the N-Mass Chain:

**Interior masses (i = 1 to N-2):**
```
m · aᵢ = -k·(xᵢ - xᵢ₋₁) + k·(xᵢ₊₁ - xᵢ)
aᵢ = k·(xᵢ₋₁ - 2xᵢ + xᵢ₊₁)/m
```

**Boundary masses (i = 0 and i = N-1):**
- Fixed at x₀ = 0 and x_{N-1} = 0 (wall boundary conditions)

## 🔢 Numerical Integration: Verlet Algorithm

The Verlet algorithm is a numerical method for integrating Newton's equations of motion. It's particularly well-suited for molecular dynamics and oscillatory systems.

### Standard Verlet Method

The position update:
```
x(t + Δt) = x(t) + v(t)·Δt + ½·a(t)·Δt²
```

The velocity update (velocity Verlet):
```
v(t + Δt) = v(t) + ½·[a(t) + a(t + Δt)]·Δt
```

### Algorithm Steps

1. **Calculate current accelerations** for all masses based on current positions
2. **Update positions** using current velocities and accelerations
3. **Calculate new accelerations** at the new positions
4. **Update velocities** using the average of old and new accelerations

### Why Verlet?

Advantages:
- **Symplectic**: Preserves the structure of Hamiltonian systems
- **Energy conservation**: Better long-term energy conservation than Euler methods
- **Time-reversible**: Running backward gives the same trajectory
- **Second-order accurate**: Error is O(Δt²)

Disadvantages:
- Requires small time steps for stability
- Not suitable for systems with strong dissipation
- Needs careful choice of Δt

## 📊 Physical Properties

### Energy Conservation

The total energy of an ideal spring-mass system should be conserved:

```
E_total = E_kinetic + E_potential
E_kinetic = ½·Σ(mᵢ·vᵢ²)
E_potential = ½·Σ(k·Δxᵢ²)
```

### Normal Modes

For N coupled oscillators, there are N normal modes of oscillation. Each mode has its own characteristic frequency:

```
ωₙ = √(k/m) · |sin(nπ/(2N+2))|  for n = 1, 2, ..., N
```

### Wave Propagation

When you displace one mass in the chain, the disturbance propagates as a wave. The wave speed depends on:

```
v_wave ∝ √(k/m)
```

## 🎲 Initial Conditions

### Two-Mass System
```c
x₁(0) = 1.1    // Slightly displaced from equilibrium
v₁(0) = 0      // Released from rest
x₂(0) = 1.0    // At equilibrium
v₂(0) = 0      // Released from rest
```

### N-Mass Chain
```c
xᵢ(0) = 0      // All masses at equilibrium
vᵢ(0) = 0      // All at rest
EXCEPT:
x₅(0) = 0.1    // Mass 5 displaced by 0.1 units
```

This creates an initial displacement that propagates through the chain.

## 🔍 Expected Behavior

### Two-Mass System
- Both masses oscillate with complex periodic motion
- The motion is a superposition of two normal modes
- Energy transfers back and forth between the masses
- The system shows **beating** behavior if masses are similar

### N-Mass Chain
- Initial displacement propagates as a wave
- Wave reflects at the fixed boundaries
- Complex interference patterns emerge
- Eventually all masses participate in the oscillation

## 📈 Stability Considerations

The time step `Δt` must satisfy the CFL (Courant-Friedrichs-Lewy) condition for stability:

```
Δt < 2/ω_max
```

Where `ω_max` is the highest natural frequency of the system. For our parameters:

```
ω_max ≈ 2√(k/m)
Δt < 1/√(k/m)
```

With `k = 1`, `m = 1`:
- `ω_max ≈ 2 rad/s`
- `Δt < 0.5 s`

The code uses `Δt = 0.01 s`, which provides a good safety margin.

## 🧮 Dimensionless Units

The simulations use dimensionless units where:
- Mass: `m = 1`
- Spring constant: `k = 1`
- Time unit: `t = √(m/k) = 1`
- Length unit: arbitrary

This simplification makes the code cleaner and the physics easier to understand.

## 📚 Further Reading

### Classical Mechanics
- Normal modes of coupled oscillators
- Lagrangian and Hamiltonian mechanics
- Wave equation in discrete systems

### Numerical Methods
- Symplectic integrators
- Stability analysis of differential equations
- Error analysis in numerical integration

### Applications
- Molecular dynamics simulations
- Crystal lattice vibrations (phonons)
- Electrical transmission lines (LC circuits)
- Seismic wave propagation

---

**Note**: This is a simplified model. Real-world systems include damping, non-linear effects, and external driving forces!
