import pygame

class Background:
    """A class to manage the scrolling background."""

    def __init__(self, ai_game, image_path, scroll_speed):
        """Initialize the background."""
        self.screen = ai_game.screen
        self.scroll_speed = scroll_speed

        # Load the background image
        self.image = pygame.image.load(image_path).convert()
        self.image = pygame.transform.scale(self.image, (ai_game.settings.screen_width, ai_game.settings.screen_height))
        self.height = ai_game.settings.screen_height

        # Initialize two positions for the background images
        self.y1 = 0
        self.y2 = -self.height

    def update(self):
        """Update the position of the background for scrolling."""
        self.y1 += self.scroll_speed
        self.y2 += self.scroll_speed

        # Reset positions to create a looping effect
        if self.y1 >= self.height:
            self.y1 = -self.height
        if self.y2 >= self.height:
            self.y2 = -self.height

    def draw(self):
        """Draw the scrolling background on the screen."""
        self.screen.blit(self.image, (0, self.y1))
        self.screen.blit(self.image, (0, self.y2))

