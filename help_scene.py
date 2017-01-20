# Created by: Mr.Coxall
# Modified by: Sheldon Hitgano
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
from main_menu_scene import *
import ui


class HelpScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        back_button_down = False
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2

        
        # add MT blue background color
        background_position = Vector2(self.size_of_screen_x * 0.5, self.size_of_screen_y * 0.5)
        self.background = SpriteNode('./assets/sprites/help_background.png',
                                     position = background_position, 
                                     parent = self, 
                                     size = self.size)
                                     
        back_button_position = Vector2(self.size_of_screen_x * (0.7/6), self.size_of_screen_y * (2.1/3))
        self.back_button = SpriteNode('./assets/sprites/left_button1.png',
                                      position = back_button_position,
                                      parent = self,
                                      scale = 0.75)
        
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        #if this button is touched, go to game scene
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()

    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
