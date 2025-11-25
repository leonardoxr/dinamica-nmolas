# Makefile for Dinâmica N-Molas
# A simple build system for the spring dynamics simulations

# Compiler and flags
CC = gcc
CFLAGS = -Wall -Wextra -O2
LDFLAGS = -lm

# Targets
TARGETS = dinamica_molas dinamica_nmolas

# Default target: build everything
all: $(TARGETS)
	@echo "✓ All programs compiled successfully!"
	@echo "Run './dinamica_molas' or './dinamica_nmolas' to execute"

# Build the 2-mass system
dinamica_molas: dinamica_molas.c
	@echo "Compiling dinamica_molas..."
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS)

# Build the N-mass chain system
dinamica_nmolas: dinamica_nmolas.c
	@echo "Compiling dinamica_nmolas..."
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS)

# Clean compiled binaries and output files
clean:
	@echo "Cleaning up..."
	rm -f $(TARGETS)
	rm -f *.txt
	rm -f *.o
	@echo "✓ Clean complete"

# Run both simulations
run: all
	@echo "\n=== Running 2-mass system ==="
	./dinamica_molas
	@echo "✓ Output saved to dinamica_mola.txt"
	@echo "\n=== Running N-mass chain system ==="
	./dinamica_nmolas
	@echo "✓ Output saved to dinamica_n_molas.txt"

# Run only the 2-mass system
run-2mass: dinamica_molas
	@echo "Running 2-mass system..."
	./dinamica_molas
	@echo "✓ Output saved to dinamica_mola.txt"

# Run only the N-mass system
run-nmass: dinamica_nmolas
	@echo "Running N-mass chain system..."
	./dinamica_nmolas
	@echo "✓ Output saved to dinamica_n_molas.txt"

# Help target
help:
	@echo "Available targets:"
	@echo "  make          - Compile all programs (default)"
	@echo "  make all      - Compile all programs"
	@echo "  make clean    - Remove compiled files and outputs"
	@echo "  make run      - Compile and run all simulations"
	@echo "  make run-2mass   - Run 2-mass system only"
	@echo "  make run-nmass   - Run N-mass chain system only"
	@echo "  make help     - Show this help message"

# Phony targets (not actual files)
.PHONY: all clean run run-2mass run-nmass help
