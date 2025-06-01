import pygame
import math

pygame.init()

# Window setup
WIDTH, HEIGHT = 1400, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity Simulation Input")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Planet:
    """Planet object."""
    def __init__(self, x, y, radius, vx, vy):
        self.x = x
        self.y = y
        self.radius = radius
        self.vx = vx
        self.vy = vy

    def draw(self, win):
        """Draw planet and velocity vector."""
        pygame.draw.circle(win, BLUE, (self.x, self.y), self.radius)
        pygame.draw.line(win, RED, (self.x, self.y), (self.x + self.vx, self.y + self.vy), 2)

    def to_list(self):
        """Return planet data as list."""
        return [self.x, self.y, self.radius, self.vx, self.vy]

def main():
    """Handle planet creation."""
    run = True
    clock = pygame.time.Clock()
    drawing_planet = False
    setting_velocity = False
    start_pos = (0, 0)
    radius = 0
    vx, vy = 0, 0
    vector = (0, 0)
    planets = []

    while run:
        clock.tick(60)
        win.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if not drawing_planet and not setting_velocity:
                        start_pos = pygame.mouse.get_pos()
                        drawing_planet = True
                        radius = 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter
                    if drawing_planet:
                        drawing_planet = False
                        setting_velocity = True
                    elif setting_velocity:
                        setting_velocity = False
                        vector = (vx, vy)
                        new_planet = Planet(start_pos[0], start_pos[1], radius, vector[0], vector[1])
                        planets.append(new_planet)
                elif event.key == pygame.K_SPACE:  # Space
                    run = False

        if drawing_planet:
            current_pos = pygame.mouse.get_pos()
            radius = int(math.hypot(current_pos[0] - start_pos[0], current_pos[1] - start_pos[1]))
            pygame.draw.circle(win, BLUE, start_pos, radius, 1)  # Draw outline

        if setting_velocity:
            current_pos = pygame.mouse.get_pos()
            vx, vy = current_pos[0] - start_pos[0], current_pos[1] - start_pos[1]
            pygame.draw.circle(win, BLUE, start_pos, radius)  # Draw planet
            pygame.draw.line(win, RED, start_pos, current_pos, 2)  # Draw velocity

        for planet in planets:
            planet.draw(win)

        pygame.display.update()

    pygame.quit()

    planet_list = [planet.to_list() for planet in planets]
    return planet_list

if __name__ == "__main__":
    planets_data = main()
    print(planets_data)