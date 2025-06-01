import pygame as pg, math
import planet_creator

pg.init()

SIZE_X = 1400
SIZE_Y = 800
FPS = 60
run = True

new_x_pos = []
new_y_pos = []
x_pos = []
y_pos = []
radius = []
mass = []
total_x = []
total_y = []
new_x_vel = []
new_y_vel = []
x_vel = []
y_vel = []
x_mouse_pos = []
y_mouse_pos  = []
names = []

# Load initial parameters of celestial bodies from the planet_creator module.
# The planet_creator module provides a GUI for users to define these parameters.
list_of_bodies_parameters = planet_creator.main()
for BODY in list_of_bodies_parameters:
    print(BODY)
    x_pos.append(int(BODY[0]))    # Initial x-coordinate
    y_pos.append(int(BODY[1]))    # Initial y-coordinate
    radius.append(int(BODY[2]))   # Radius of the body (used for visual representation)
    mass.append(int(BODY[2])*10**24) # Mass of the body (proportional to radius)
    x_vel.append(int(int(BODY[3]))/5) # Initial x-velocity
    y_vel.append(int(int(BODY[4]))/5) # Initial y-velocity



# This commented section is a representation of the 3-body problem.
# Uncomment it to observe how this system evolves from stable to chaotic.
'''new_x_pos = []
new_y_pos = []
x_pos = [400, 250, 250]
y_pos = [300, 386.60254038, 213.39745962]
radius = [7, 7, 7]
mass = []
total_x = []
total_y = []
new_x_vel = []
new_y_vel = []
x_vel = [0, -2.59807621, 2.59807621]
y_vel = [3, -1.5, -1.5]
x_mouse_pos = []
y_mouse_pos  = []
names = []'''


# Calculate mass for each body based on its radius (scaling factor applied).
for i in radius:
    mass.append(int(i)*10**24)


screen = pg.display.set_mode([SIZE_X, SIZE_Y]) # Initialize the display window.
clock = pg.time.Clock()                     # Create a clock object to control frame rate.
print(names)

class Bodies():
    """Class to manage the celestial bodies and their interactions."""
    def __init__(self):
        self.bodies_num = len(x_pos) # Number of bodies in the simulation.
        self.G = 6.67*10**-11        # Gravitational constant.
        self.meters = 500000          # Scaling factor for converting pixel distance to meters.
        #self.mode = mode

    def mouse_shift(self):
        """Handles mouse input for panning the simulation view."""
        # Get the current mouse position.
        pos = pg.mouse.get_pos()

        # Calculate the shift in mouse position between two consecutive frames.
        # This is used for panning the view when the left mouse button is held.
        if len(x_mouse_pos) == 2:
            self.mouse_x_shift_parameter = x_mouse_pos[0] - x_mouse_pos[1]
            x_mouse_pos.remove(x_mouse_pos[0])
            x_mouse_pos.append(pos[0])
            self.mouse_y_shift_parameter = y_mouse_pos[0] - y_mouse_pos[1]
            y_mouse_pos.remove(y_mouse_pos[0])
            y_mouse_pos.append(pos[1])
        else:
            self.mouse_x_shift_parameter = 0
            x_mouse_pos.append(pos[0])
            self.mouse_y_shift_parameter = 0
            y_mouse_pos.append(pos[1])


    def draw(self):
        """Draws all the celestial bodies on the screen."""
        for i in range(self.bodies_num):
            # Check if the left mouse button is pressed.
            mouse_butts = pg.mouse.get_pressed()

            # If the left mouse button is pressed, pan the view by subtracting the mouse shift.
            if mouse_butts[0]:
                x_pos[i] = x_pos[i] - self.mouse_x_shift_parameter*1.5
                y_pos[i] = y_pos[i] - self.mouse_y_shift_parameter*1.5
            # Draw the body as a yellow circle.
            pg.draw.circle(screen, 'yellow', (x_pos[i], y_pos[i]), radius[i])

    def calculate(self):
        """Calculates the gravitational forces and updates the positions and velocities of the bodies."""
        # Initialize lists to store the new accelerations for each body in both x and y directions.
        new_x_acc = [0]*self.bodies_num
        new_y_acc = [0]*self.bodies_num
        # Iterate through each body to calculate the gravitational forces exerted on it by every other body.
        for body1 in range(self.bodies_num):
            for body2 in range(self.bodies_num):
                # Skip calculation if the body is interacting with itself.
                if body1 == body2:
                    continue

                # Calculate the distance between the two bodies in both x and y directions.
                x_dist = x_pos[body2] - x_pos[body1]
                y_dist = y_pos[body2] - y_pos[body1]
                # Calculate the pixel distance between the two bodies.
                pix_dist = math.sqrt(x_dist**2 + y_dist**2)
                # Scale the pixel distance to meters.
                distance = pix_dist*self.meters

                # Calculate the gravitational force between the two bodies.
                force = self.G*mass[body1]*mass[body2]/distance**2

                # Calculate the acceleration of body1 due to the force from body2.
                acc = force/mass[body1]

                # Calculate the angle (theta) of the vector pointing from body1 to body2.
                theta = math.atan2(y_dist, x_dist)
                # Calculate the x and y components of the acceleration.
                x_acc = math.cos(theta) * acc
                y_acc = math.sin(theta) * acc

                # Accumulate the accelerations from all other bodies for body1.
                new_x_acc[body1] += x_acc
                new_y_acc[body1] += y_acc


        # Update the velocities and positions of all bodies based on the calculated accelerations.
        for i in range(len(x_pos)):
            x_vel[i] = x_vel[i] + new_x_acc[i]
            y_vel[i] = y_vel[i] + new_y_acc[i]
            x_pos[i] = x_pos[i] + x_vel[i]
            y_pos[i] = y_pos[i] + y_vel[i]


bodies = Bodies()

while run:
    screen.fill((0, 0, 30)) # Fill the screen with a dark blue color.
    fps = clock.get_fps()
    print('FPS: ' + str(fps)) # Print the current frames per second.
    clock.tick(FPS)
    for evt in pg.event.get(): # Event handling loop.
        if evt.type == pg.QUIT:
            run = False
    bodies.mouse_shift()
    bodies.draw()        # Draw the celestial bodies.
    bodies.calculate()   # Calculate the physics for the next frame.
    pg.display.flip()    # Update the full display Surface to the screen.