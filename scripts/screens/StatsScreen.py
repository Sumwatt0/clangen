from threading import current_thread

import pygame
import pygame_gui

from scripts.cat.cats import Cat
from scripts.game_structure import image_cache
from scripts.game_structure.game_essentials import game, screen, screen_x, screen_y, MANAGER
from scripts.game_structure.ui_elements import UIImageButton
from scripts.game_structure.propagating_thread import PropagatingThread
from scripts.game_structure.windows import SaveCheck, EventLoading
from scripts.utility import update_sprite, scale
from .Screens import Screens


class StatsScreen(Screens):
    """
    TODO: DOCS
    """
    def screen_switches(self):
        """Runs when this screen is switched to."""
        self.main_menu_button = UIImageButton(scale(
            pygame.Rect((50, 50), (305, 60))),
            "",
            object_id="#main_menu_button",
            manager=MANAGER)

    def handle_event(self, event):
        """This is where events that occur on this page are handled.
        For the pygame_gui rewrite, button presses are also handled here. """
        if event.type == pygame_gui.UI_BUTTON_START_PRESS:
            if event.ui_element == self.main_menu_button:
                self.change_screen('start screen')
                return

    def exit_screen(self):
        """Runs when screen exits"""
        self.main_menu_button.kill()
        del self.main_menu_button

    def on_use(self):
        """Runs every frame this screen is used."""