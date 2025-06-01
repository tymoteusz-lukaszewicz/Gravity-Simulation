# Gravity-Simulation

# 2D N-Body Gravity Simulation with Interactive System Creation

## Purpose

Presentation of the final version of the project for my portfolio. This project implements a 2D N-body gravity simulation using Pygame. It allows users to create and simulate their own planetary systems through an interactive interface. The system creation is handled internally by the `planet_creator.py` script, which is utilized by the main simulation script `planet_simulatorV6.py`.

## Key Features

* **N-Body Simulation:** Simulates the gravitational interactions between multiple celestial bodies in a 2D plane.
* **Interactive System Creation:** The `planet_simulationV6.py` script uses the `planet_creator.py` script internally to provide an interactive interface that enables users to:
    * Define the initial position of each planet with a left-click.
    * Set the radius (and consequently mass) of the planet by dragging the mouse after the initial click and confirming with Enter.
    * Define the initial velocity vector by dragging the mouse from the planet's position and confirming with Enter (vector magnitude represents speed).
    * Create multiple planets sequentially.
    * Finalize the system creation by pressing Space.
* **Realistic Gravity:** Implements the fundamental laws of Newtonian gravity to calculate the forces between bodies.
* **Basic Rendering:** Visualizes the planets as yellow circles on a dark background.
* **Interactive Camera (Panning):** Allows users to pan the view of the simulation by holding down the left mouse button and dragging.

## Technologies Used

* Programming Language: Python
* Libraries: Pygame, math
* Scripts:
    * `planet_simulatorV6.py` (main simulation script)
    * `planet_creator.py` (system creation interface, used by `planet_simulatorV6.py`)

## Setup Instructions

1.  Make sure you have Python 3.x and Pygame installed:

    ```bash
    pip install pygame
    ```
2.  Ensure that both `planet_simulatorV6.py` and `planet_creator.py` are located in the same directory.

## Running the Code

To run the simulation and create your own planetary system, execute the main simulation script:

```bash
python planet_simulatorV6.py
