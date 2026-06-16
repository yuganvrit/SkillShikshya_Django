"""
2-Player Local Multiplayer Car Racing Game
--------------------------------------------
Player 1 (RED car):  A = move left,  D = move right
Player 2 (BLUE car): LEFT arrow = move left,  RIGHT arrow = move right

Both players race on a vertically scrolling road, dodging yellow
obstacles. Score increases the longer you survive. The game ends
when one or both cars crash into an obstacle.

Press R to restart, ESC to quit.
"""

import pygame
import random
import sys

pygame.init()

# ---------------- SETTINGS ----------------
WIDTH, HEIGHT = 800, 600
CAR_WIDTH, CAR_HEIGHT = 50, 90
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 90
FPS = 60

# Colors
ROAD_COLOR = (50, 50, 50)
LINE_COLOR = (255, 255, 255)
RED = (200, 30, 30)
BLUE = (30, 30, 200)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Player Car Race")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)
big_font = pygame.font.SysFont("Arial", 60)


class Car:
    """Represents one player's car."""

    def __init__(self, x, color, controls, lane_min, lane_max):
        self.x = x
        self.y = HEIGHT - CAR_HEIGHT - 20
        self.color = color
        self.controls = controls          # dict with 'left' and 'right' key codes
        self.lane_min = lane_min           # left boundary this car can move within
        self.lane_max = lane_max           # right boundary this car can move within
        self.speed = 7
        self.alive = True
        self.score = 0

    def move(self, keys):
        if not self.alive:
            return

        if keys[self.controls['left']]:
            self.x -= self.speed
        if keys[self.controls['right']]:
            self.x += self.speed

        # Keep the car within its half of the road
        if self.x < self.lane_min:
            self.x = self.lane_min
        if self.x > self.lane_max - CAR_WIDTH:
            self.x = self.lane_max - CAR_WIDTH

    def draw(self, surface):
        color = self.color if self.alive else (100, 100, 100)
        pygame.draw.rect(surface, color, (self.x, self.y, CAR_WIDTH, CAR_HEIGHT), border_radius=8)
        # simple windshield detail
        pygame.draw.rect(surface, WHITE, (self.x + 10, self.y + 15, CAR_WIDTH - 20, 20), border_radius=4)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, CAR_WIDTH, CAR_HEIGHT)


class Obstacle:
    """A falling obstacle the players must dodge."""

    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, YELLOW, (self.x, self.y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT), border_radius=8)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)


def draw_road(offset):
    """Draws the road background and scrolling lane markings."""
    screen.fill(ROAD_COLOR)
    # divider between the two players' lanes
    pygame.draw.line(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 4)

    # dashed center line for each player's half, scrolling downward
    dash_height = 40
    gap = 30
    for lane_center in (WIDTH // 4, 3 * WIDTH // 4):
        y = -dash_height + (offset % (dash_height + gap))
        while y < HEIGHT:
            pygame.draw.rect(screen, LINE_COLOR, (lane_center - 3, y, 6, dash_height))
            y += dash_height + gap


def show_text_center(text, font_obj, color, y):
    surf = font_obj.render(text, True, color)
    rect = surf.get_rect(center=(WIDTH // 2, y))
    screen.blit(surf, rect)


def run_game():
    """Runs one full game session. Returns 'restart' or 'quit'."""

    player1 = Car(
        x=WIDTH // 4 - CAR_WIDTH // 2,
        color=RED,
        controls={'left': pygame.K_a, 'right': pygame.K_d},
        lane_min=0,
        lane_max=WIDTH // 2,
    )

    player2 = Car(
        x=3 * WIDTH // 4 - CAR_WIDTH // 2,
        color=BLUE,
        controls={'left': pygame.K_LEFT, 'right': pygame.K_RIGHT},
        lane_min=WIDTH // 2,
        lane_max=WIDTH,
    )

    players = [player1, player2]

    obstacles = []
    obstacle_timer = 0
    obstacle_speed = 6
    road_offset = 0

    game_over = False
    winner_text = ""

    while True:
        clock.tick(FPS)
        road_offset += obstacle_speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game_over:
                    return "restart"
                if event.key == pygame.K_ESCAPE:
                    return "quit"

        keys = pygame.key.get_pressed()

        if not game_over:
            for p in players:
                p.move(keys)
                p.score += 1  # score increases the longer you survive

            # spawn obstacles in a random lane every ~40 frames
            obstacle_timer += 1
            if obstacle_timer > 40:
                obstacle_timer = 0
                lane = random.choice(['left', 'right'])
                if lane == 'left':
                    x = random.randint(0, WIDTH // 2 - OBSTACLE_WIDTH)
                else:
                    x = random.randint(WIDTH // 2, WIDTH - OBSTACLE_WIDTH)
                obstacles.append(Obstacle(x, -OBSTACLE_HEIGHT, obstacle_speed))

            # move obstacles, remove off-screen ones, check collisions
            for obs in obstacles[:]:
                obs.move()
                if obs.y > HEIGHT:
                    obstacles.remove(obs)
                    continue
                for p in players:
                    if p.alive and obs.get_rect().colliderect(p.get_rect()):
                        p.alive = False

            # difficulty ramps up slowly over time
            obstacle_speed = 6 + (player1.score // 300)

            # check for game over
            if not player1.alive or not player2.alive:
                game_over = True
                if not player1.alive and not player2.alive:
                    winner_text = "It's a tie! Both crashed."
                elif not player1.alive:
                    winner_text = "Player 2 (Blue) wins!"
                else:
                    winner_text = "Player 1 (Red) wins!"

        # ---------------- DRAW EVERYTHING ----------------
        draw_road(road_offset)

        for obs in obstacles:
            obs.draw(screen)

        for p in players:
            p.draw(screen)

        score1_surf = font.render(f"P1 (A/D) Score: {player1.score}", True, RED)
        score2_surf = font.render(f"P2 (Arrows) Score: {player2.score}", True, BLUE)
        screen.blit(score1_surf, (10, 10))
        screen.blit(score2_surf, (WIDTH - score2_surf.get_width() - 10, 10))

        if game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(180)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))
            show_text_center(winner_text, big_font, WHITE, HEIGHT // 2 - 40)
            show_text_center("Press R to Restart or ESC to Quit", font, WHITE, HEIGHT // 2 + 30)

        pygame.display.flip()


def main():
    while True:
        result = run_game()
        if result == "quit":
            break

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
