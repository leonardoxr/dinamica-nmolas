# Contributing to Dinâmica N-Molas

## 📚 About This Project

This is an **archived academic project** created for a college computational physics course. While it's not actively maintained, it can serve as a learning resource for students studying numerical methods and computational physics.

## 🎓 For Students

If you're a student learning about:
- Numerical integration methods
- Computational physics
- Differential equations
- C programming

Feel free to fork this repository and use it as a learning exercise! Here are some ideas for improvements:

### Beginner Level
- Add command-line argument parsing to set parameters without recompilation
- Add input validation and error handling
- Create a Makefile for easier compilation
- Add more inline comments explaining the physics
- Create visualization scripts (Python, MATLAB, gnuplot)

### Intermediate Level
- Implement other integration methods (Euler, Runge-Kutta, etc.) for comparison
- Add energy conservation checks and reporting
- Support dynamic array allocation for arbitrary number of masses
- Create a configuration file system (JSON, YAML, or simple text)
- Add unit tests for the physics calculations
- Implement damping (friction) in the system

### Advanced Level
- Extend to 2D or 3D spring systems
- Add graphical real-time visualization (SDL, OpenGL)
- Parallelize using OpenMP or MPI
- Implement adaptive time-stepping
- Add different boundary conditions (periodic, free, driven)
- Compare performance with other languages (Python, Julia, Fortran)

## 🔧 Development Setup

### Requirements
```bash
# Install GCC (if not already installed)
sudo apt-get install build-essential  # Ubuntu/Debian
# or
brew install gcc  # macOS with Homebrew
```

### Building
```bash
gcc -o dinamica_molas dinamica_molas.c -lm
gcc -o dinamica_nmolas dinamica_nmolas.c -lm
```

### Testing
```bash
./dinamica_molas
./dinamica_nmolas

# Verify output files were created
ls -l *.txt
```

## 📝 Code Style

If you're improving this code, consider:
- Adding meaningful variable names (the current ones are quite terse)
- Using consistent indentation (4 spaces recommended)
- Adding function documentation
- Separating concerns (I/O, physics calculations, integration)
- Following modern C standards (C99 or C11)

## 🐛 Known Issues

- No error handling for file operations
- Hard-coded array sizes could cause buffer overflows
- No validation of physical parameters (negative masses, etc.)
- Time step size could lead to instability if too large

## 📖 Learning Resources

### Numerical Methods
- "Numerical Recipes in C" by Press et al.
- "Computational Physics" by Nicholas Giordano
- "An Introduction to Computer Simulation Methods" by Gould & Tobochnik

### C Programming
- "The C Programming Language" by Kernighan & Ritchie
- "C Programming: A Modern Approach" by K. N. King

### Physics
- "Classical Mechanics" by John R. Taylor
- "Analytical Mechanics" by Fowles & Cassiday

## 🤝 How to Share Your Improvements

1. **Fork** this repository
2. **Create** a descriptive branch (`git checkout -b feature/adaptive-timestep`)
3. **Commit** your changes with clear messages
4. **Document** what you changed and why
5. **Share** your fork with classmates or on your portfolio!

Since this is an archived academic project, pull requests aren't being accepted to the main repository, but you're encouraged to maintain your own improved version as a learning exercise.

## 💡 Project Ideas

If you want to build on this project:

1. **Create a comparison study**: Implement multiple integration methods and compare accuracy/performance
2. **Build a GUI**: Add real-time visualization of the oscillating masses
3. **Port to another language**: Rewrite in Python, Rust, or Julia and compare
4. **Write a tutorial**: Create a blog post or video explaining the physics and code
5. **Extend the physics**: Add temperature, non-linear springs, or external driving forces

## ❓ Questions?

If you have questions about the physics or implementation, good resources include:
- Your university's physics/computer science department
- Physics Stack Exchange (physics.stackexchange.com)
- Stack Overflow (for C programming questions)
- Computational science communities on Reddit

## 📄 License

All contributions should respect the GPL-3.0 license of the original project.

---

**Remember**: The best way to learn is by doing! Don't be afraid to break things and experiment. That's what education is all about. 🎓
