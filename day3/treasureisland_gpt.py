import pygame   # Core library for graphics, events, fonts, etc.
import sys      # For clean exit using sys.exit
from textwrap import wrap   # Wraps long paragraphs into multiple lines
from pathlib import Path    # Robust path handling to load treasure.txt

# -----------------------------
# Button: reusable clickable UI element
# -----------------------------
class Button:
    def __init__(self, rect, text, on_click, font, padding=12):
        self.rect = pygame.Rect(rect)     # Button rectangle (x, y, w, h)
        self.text = text                  # Label shown on the button
        self.on_click = on_click          # Callback to invoke on click
        self.font = font                  # Font used to render the label
        self.padding = padding            # Inner horizontal/vertical padding
        self.hover = False                # True when mouse is over the button

        # Pre-render label surface for performance
        self.text_surf = self.font.render(self.text, True, (20, 20, 20))  # pygame.font.render -> Surface
        tw, th = self.text_surf.get_size()                                 # Surface.get_size -> (w, h)

        # Ensure the button is large enough for the text + padding
        self.rect.w = max(self.rect.w, tw + 2 * self.padding)
        self.rect.h = max(self.rect.h, th + 2 * self.padding)

    def draw(self, surf):
        base = (230, 230, 230)   # Default background color
        hovered = (210, 210, 210)  # Background when hovered
        border = (60, 60, 60)    # Border color

        # Draw button background (rounded)
        pygame.draw.rect(surf, hovered if self.hover else base, self.rect, border_radius=8)  # pygame.draw.rect
        # Draw button border
        pygame.draw.rect(surf, border, self.rect, width=2, border_radius=8)                  # pygame.draw.rect

        # Draw the label centered inside the button
        surf.blit(self.text_surf, self.text_surf.get_rect(center=self.rect.center))          # Surface.blit

    def handle_event(self, ev):
        # Update hover state on mouse movement
        if ev.type == pygame.MOUSEMOTION:                                                    # Mouse move event
            self.hover = self.rect.collidepoint(ev.pos)                                      # Rect.collidepoint

        # Trigger callback on left mouse button down
        elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:                           # Left click
            if self.rect.collidepoint(ev.pos):
                self.on_click()                                                              # Invoke callback


# -----------------------------
# Treasure Island game state machine
# -----------------------------
class TreasureGame:
    def __init__(self, screen):
        self.screen = screen
        self.W, self.H = self.screen.get_size()  # Query window width/height from display Surface

        # Fonts (title, body, small hint, and monospace for ASCII art)
        self.title_font = pygame.font.SysFont("consolas", 28)    # pygame.font.SysFont
        self.body_font  = pygame.font.SysFont("arial", 22)
        self.small_font = pygame.font.SysFont("arial", 16, italic=True)
        self.mono_font  = pygame.font.SysFont("consolas", 12)

        # Load ASCII art from external file treasure.txt (same folder as this script)
        ascii_file = Path(__file__).with_name("treasure.txt")
        if ascii_file.exists():
            self.ascii_art = ascii_file.read_text(encoding="utf-8")
        else:
            self.ascii_art = "MISSING FILE: treasure.txt"

        # Initial state and UI
        self.state = "intro"
        self.buttons = []
        self.make_ui()  # Build initial buttons for current state

    # ---- Text utilities ------------------------------------------------------
    def draw_wrapped_text(self, text, rect, font, color=(20, 20, 20), line_spacing=6):
        """
        Render multi-line, wrapped text inside 'rect'.
        Returns the y-position after the last drawn line (not used by caller here).
        """
        x, y, w, h = rect
        line_h = font.get_linesize()                           # Font line height in pixels
        ch_w = max(1, font.size("M")[0])                       # Approximate character width using 'M'
        chars_per_line = max(8, int(w / ch_w))                 # Estimate how many characters fit per line

        for para in text.split("\n"):                          # Preserve paragraph breaks
            for line in wrap(para, width=chars_per_line):      # Wrap each paragraph
                surf = font.render(line, True, color)          # Render a single line
                self.screen.blit(surf, (x, y))                 # Draw the line at current position
                y += line_h + line_spacing
            y += line_spacing                                  # Extra gap between paragraphs
        return y

    def draw_ascii_block(self, text, rect, font, color=(40, 40, 40), padding=10):
        """
        Draw the ASCII art without wrapping inside a framed panel.
        Content is clipped so it won't overflow the panel's area.
        """
        panel_bg = (245, 245, 245)
        border = (100, 100, 100)

        # Draw panel background and border
        pygame.draw.rect(self.screen, panel_bg, rect, border_radius=8)                  # Panel background
        pygame.draw.rect(self.screen, border, rect, width=2, border_radius=8)          # Panel border

        # Define inner clipped area
        inner = rect.inflate(-2 * padding, -2 * padding)                                # Shrink rect for padding
        prev_clip = self.screen.get_clip()                                              # Save previous clip
        self.screen.set_clip(inner)                                                     # Set clipping region

        # Render ASCII art line by line (no wrapping)
        y = inner.top
        line_h = font.get_linesize()
        for raw_line in text.splitlines():
            surf = font.render(raw_line, True, color)
            self.screen.blit(surf, (inner.left, y))
            y += line_h

        # Restore previous clipping region
        self.screen.set_clip(prev_clip)

    # ---- Button layout helpers ----------------------------------------------
    def center_buttons(self, labels_callbacks, y_top):
        """
        Create a horizontal row of centered buttons at vertical position y_top.
        labels_callbacks: List of tuples [(label, callback), ...]
        """
        self.buttons = []
        gap = 16
        widths = []
        # Pre-measure each button width (text width + padding)
        for label, _ in labels_callbacks:
            surf = self.body_font.render(label, True, (0, 0, 0))    # Measure text width
            widths.append(surf.get_width() + 24 * 2)                # Add padding margin

        total_w = sum(widths) + gap * (len(labels_callbacks) - 1)   # Total row width
        x = (self.W - total_w) // 2                                 # Starting X to center the row

        for i, (label, cb) in enumerate(labels_callbacks):
            w = widths[i]
            rect = (x, y_top, w, 52)
            self.buttons.append(Button(rect, label, cb, self.body_font))  # Create and store button
            x += w + gap

    def make_ui(self):
        """
        Define which buttons are visible for the current state.
        """
        if self.state == "intro":
            def go_next():
                self.state = "crossroad"; self.make_ui()
            self.center_buttons([("Start", go_next)], self.H - 100)

        elif self.state == "crossroad":
            def left():  self.state = "lake";       self.make_ui()
            def right(): self.state = "hole_dead";  self.make_ui()
            self.center_buttons([("Left", left), ("Right", right)], self.H - 120)

        elif self.state == "lake":
            def wait(): self.state = "house";       self.make_ui()
            def swim(): self.state = "trout_dead";  self.make_ui()
            self.center_buttons([("Wait (Boat)", wait), ("Swim Across", swim)], self.H - 120)

        elif self.state == "house":
            def red():    self.state = "red_dead";    self.make_ui()
            def yellow(): self.state = "yellow_win";  self.make_ui()
            def blue():   self.state = "blue_dead";   self.make_ui()
            self.center_buttons([("Red", red), ("Yellow", yellow), ("Blue", blue)], self.H - 120)

        elif self.state in ("hole_dead", "trout_dead", "red_dead", "blue_dead", "yellow_win"):
            def restart():  self.state = "crossroad"; self.make_ui()
            def quit_game(): pygame.quit(); sys.exit(0)   # pygame.quit + sys.exit for clean shutdown
            self.center_buttons([("Play Again", restart), ("Quit", quit_game)], self.H - 120)

    # ---- Main drawing --------------------------------------------------------
    def draw(self):
        self.screen.fill((248, 247, 245))  # Clear screen to background color (Surface.fill)

        # Title centered at top
        title_surf = self.title_font.render("Treasure Island", True, (30, 30, 30))  # Render title
        self.screen.blit(title_surf, title_surf.get_rect(midtop=(self.W // 2, 12))) # Blit centered at y=12

        margin = 40

        # Per-state text and panels
        if self.state == "intro":
            # ASCII art panel (fixed height, clipped)
            ascii_h = min(280, self.H - 260)                                      # Keep space for text + buttons
            ascii_rect = pygame.Rect(margin, 70, self.W - 2 * margin, ascii_h)    # Panel rect
            self.draw_ascii_block(self.ascii_art, ascii_rect, self.mono_font)     # Render ASCII art

            # Introductory text below ASCII panel
            body_rect = pygame.Rect(margin, ascii_rect.bottom + 12, self.W - 2 * margin, 120)
            info = "Welcome to Treasure Island.\nYour mission is to find the treasure."
            self.draw_wrapped_text(info, body_rect, self.body_font)

        elif self.state == "crossroad":
            body_rect = pygame.Rect(margin, 80, self.W - 2 * margin, self.H - 220)
            self.draw_wrapped_text("You're at a crossroad. Where do you want to go?", body_rect, self.body_font)

        elif self.state == "lake":
            body_rect = pygame.Rect(margin, 80, self.W - 2 * margin, self.H - 220)
            text = "You've come to a lake. There is an island in the middle of the lake.\nWhat do you do?"
            self.draw_wrapped_text(text, body_rect, self.body_font)

        elif self.state == "house":
            body_rect = pygame.Rect(margin, 80, self.W - 2 * margin, self.H - 220)
            text = "You arrive at the island unharmed. There is a house with 3 doors: Red, Yellow, Blue."
            self.draw_wrapped_text(text, body_rect, self.body_font)

        elif self.state == "hole_dead":
            body_rect = pygame.Rect(margin, 80, self.W - 2 * margin, self.H - 220)
            self.draw_wrapped_text("You fell into a hole.\nGame Over.", body_rect, self.body_font)

        elif self.state == "trout_dead":
            body_rect = pygame.Rect(margin, 80, self.W - 2 * margin, self.H - 220)
            self.draw_wrapped_text("You were attacked by trout.\nGame Over.", body_rect, self.body_font)

        elif self.state == "red_dead":
            body_rect = pygame.Rect(margin, 80, self.W - 2 * margin, self.H - 220)
            self.draw_wrapped_text("Burned by fire.\nGame Over.", body_rect, self.body_font)

        elif self.state == "blue_dead":
            body_rect = pygame.Rect(margin, 80, self.W - 2 * margin, self.H - 220)
            self.draw_wrapped_text("Eaten by beasts.\nGame Over.", body_rect, self.body_font)

        elif self.state == "yellow_win":
            body_rect = pygame.Rect(margin, 80, self.W - 2 * margin, self.H - 220)
            self.draw_wrapped_text("You chose the yellow door. You found the treasure!\nYou Win! 🏆", body_rect, self.body_font)

        # Hint line at the bottom-left
        tip = "Hint: Hover and click the buttons."
        tip_s = self.small_font.render(tip, True, (90, 90, 90))                    # Render hint text
        self.screen.blit(tip_s, (margin, self.H - 40))                              # Draw hint

        # Draw current buttons
        for b in self.buttons:
            b.draw(self.screen)

    def handle_event(self, ev):
        # Forward pygame events to buttons for hover/click handling
        for b in self.buttons:
            b.handle_event(ev)


# -----------------------------
# Program entry point
# -----------------------------
def main():
    pygame.init()  # Initialize all imported pygame modules (video, audio, font, etc.)
    pygame.display.set_caption("Treasure Island - Pygame")  # Set window title

    # Create the main window Surface with size 900x600
    screen = pygame.display.set_mode((900, 600))  # pygame.display.set_mode
    clock = pygame.time.Clock()                   # Rate limiter for consistent FPS

    # Instantiate the game with the screen Surface
    game = TreasureGame(screen)

    # Main loop: process events, update/draw, present to screen
    while True:
        for ev in pygame.event.get():     # Poll all pending events (keyboard, mouse, window)
            if ev.type == pygame.QUIT:    # Window close button pressed
                pygame.quit()             # Uninitialize pygame modules
                sys.exit(0)               # Exit the program immediately
            game.handle_event(ev)         # Let the game (buttons) handle input

        game.draw()                       # Draw the current frame
        pygame.display.flip()             # Swap the display buffers (present frame)
        clock.tick(60)                    # Cap to ~60 FPS (Time since last call based)

# Run only if executed directly, not when imported as a module
if __name__ == "__main__":
    main()
