# Created by: Mr.Coxall
# Modified by: Sheldon Hitgano
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.
from __future__ import division
from scene import *
from main_menu_scene import *
import ui


class CreditsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        back_button_down = False
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2

        
        # add MT blue background color
        background_position = Vector2(self.size_of_screen_x * 0.5, self.size_of_screen_y * 0.5)
        background_size = Vector2(self.size_of_screen_x, self.size_of_screen_y)
        self.background = SpriteNode(position = background_position, 
                                     color = 'lightblue', 
                                     parent = self, 
                                     size = background_size)

        back_button_position = Vector2(self.size_of_screen_x * (0.7/6), self.size_of_screen_y* (5.2/6))
        self.back_button = SpriteNode('./assets/sprites/left_button1.png',
                                      position = back_button_position,
                                      parent = self,
                                      scale = 0.75)
        background_credit_position = Vector2(self.size_of_screen_x * 0.5, self.size_of_screen_y * 0.5)
        self.background_credit_label = LabelNode(text = 'Background made by:bevouliin.com',
                                     font=('Helvetica', 40),
                                     parent = self,
                                     position = background_credit_position)
        
        character_credit_label_position= Vector2(self.size_of_screen_x * 0.5, self.size_of_screen_y * (2/3))
        self.character_credit_label = LabelNode(text = 'Character(Block Ninja) made by:Korba',
                                     font=('Helvetica', 40),
                                     parent = self,
                                     position = character_credit_label_position)

    
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
    
