#!/usr/bin/env python3
"""
Visualization script for spring dynamics simulations
Plots the position vs time for all masses in the system
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import os

def plot_nmass_system(filename='dinamica_n_molas.txt'):
    """
    Visualize the N-mass chain system
    """
    if not os.path.exists(filename):
        print(f"Error: {filename} not found!")
        print("Please run the simulation first: ./dinamica_nmolas")
        return

    # Load data
    print(f"Loading data from {filename}...")
    data = np.loadtxt(filename)
    time = data[:, 0]
    positions = data[:, 1:]

    n_masses = positions.shape[1]
    print(f"Found {n_masses} masses")
    print(f"Simulation time: {time[0]:.2f} to {time[-1]:.2f}")
    print(f"Time steps: {len(time)}")

    # Create figure with multiple subplots
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))

    # Plot 1: All positions vs time
    ax1 = axes[0]
    for i in range(n_masses):
        ax1.plot(time, positions[:, i], label=f'Mass {i}', alpha=0.7)

    ax1.set_xlabel('Time')
    ax1.set_ylabel('Position')
    ax1.set_title('N-Mass Spring System: Position vs Time')
    ax1.legend(loc='upper right', ncol=2, fontsize=8)
    ax1.grid(True, alpha=0.3)

    # Plot 2: Heatmap showing wave propagation
    ax2 = axes[1]
    # Sample data for better visualization (every 10th point)
    sample_rate = max(1, len(time) // 500)
    im = ax2.imshow(positions[::sample_rate, :].T,
                     aspect='auto',
                     cmap='RdBu_r',
                     extent=[time[0], time[-1], 0, n_masses-1],
                     interpolation='bilinear')

    ax2.set_xlabel('Time')
    ax2.set_ylabel('Mass Index')
    ax2.set_title('Wave Propagation Heatmap')
    plt.colorbar(im, ax=ax2, label='Position')

    plt.tight_layout()

    # Save figure
    output_file = 'nmass_visualization.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"✓ Saved visualization to {output_file}")

    plt.show()


def plot_2mass_system(filename='dinamica_mola.txt'):
    """
    Visualize the 2-mass system
    """
    if not os.path.exists(filename):
        print(f"Error: {filename} not found!")
        print("Please run the simulation first: ./dinamica_molas")
        return

    # Load data
    print(f"Loading data from {filename}...")
    data = np.loadtxt(filename)
    time = data[:, 0]
    x1 = data[:, 1]
    v1 = data[:, 2]
    x2 = data[:, 3]
    v2 = data[:, 4]

    print(f"Simulation time: {time[0]:.2f} to {time[-1]:.2f}")
    print(f"Time steps: {len(time)}")

    # Create figure with multiple subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    # Plot 1: Positions vs time
    axes[0, 0].plot(time, x1, label='Mass 1', color='blue', alpha=0.7)
    axes[0, 0].plot(time, x2, label='Mass 2', color='red', alpha=0.7)
    axes[0, 0].set_xlabel('Time')
    axes[0, 0].set_ylabel('Position')
    axes[0, 0].set_title('Positions vs Time')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)

    # Plot 2: Velocities vs time
    axes[0, 1].plot(time, v1, label='Mass 1', color='blue', alpha=0.7)
    axes[0, 1].plot(time, v2, label='Mass 2', color='red', alpha=0.7)
    axes[0, 1].set_xlabel('Time')
    axes[0, 1].set_ylabel('Velocity')
    axes[0, 1].set_title('Velocities vs Time')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)

    # Plot 3: Phase space for mass 1
    axes[1, 0].plot(x1, v1, color='blue', alpha=0.5, linewidth=0.5)
    axes[1, 0].set_xlabel('Position')
    axes[1, 0].set_ylabel('Velocity')
    axes[1, 0].set_title('Phase Space: Mass 1')
    axes[1, 0].grid(True, alpha=0.3)

    # Plot 4: Phase space for mass 2
    axes[1, 1].plot(x2, v2, color='red', alpha=0.5, linewidth=0.5)
    axes[1, 1].set_xlabel('Position')
    axes[1, 1].set_ylabel('Velocity')
    axes[1, 1].set_title('Phase Space: Mass 2')
    axes[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()

    # Save figure
    output_file = '2mass_visualization.png'
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"✓ Saved visualization to {output_file}")

    plt.show()


def main():
    """
    Main function to handle command-line arguments
    """
    print("Spring Dynamics Visualization Tool")
    print("=" * 40)

    if len(sys.argv) > 1:
        filename = sys.argv[1]

        # Determine which type of simulation based on filename
        if 'mola.txt' in filename or '2mass' in filename:
            plot_2mass_system(filename)
        else:
            plot_nmass_system(filename)
    else:
        # Check which files exist and plot accordingly
        if os.path.exists('dinamica_n_molas.txt'):
            print("\nFound N-mass system output")
            plot_nmass_system()
        elif os.path.exists('dinamica_mola.txt'):
            print("\nFound 2-mass system output")
            plot_2mass_system()
        else:
            print("\nNo simulation output found!")
            print("\nUsage:")
            print("  python visualize.py                    - Auto-detect and plot")
            print("  python visualize.py <filename>         - Plot specific file")
            print("\nFirst run a simulation:")
            print("  ./dinamica_nmolas    - Run N-mass simulation")
            print("  ./dinamica_molas     - Run 2-mass simulation")


if __name__ == '__main__':
    main()
