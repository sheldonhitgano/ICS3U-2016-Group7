# Created by: Mr.Coxall
# Modified by: Sheldon Hitgano
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
from game_scene import*
from help_scene import *
from credits_scene import *

import ui


class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2

        # add MT blue background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'white', 
                                     parent = self, 
                                     size = self.size)
        
        title_position = Vector2(self.size_of_screen_x * 0.55, self.size_of_screen_y * 0.75)
        self.title_label = SpriteNode('./assets/sprites/title.png',
                                      parent = self,
                                      position = title_position,
                                      scale = 1.5)
                                      
        
        start_button_position = Vector2(self.size_of_screen_x * 0.55, self.size_of_screen_y * (1.25/3))
        self.start_button = SpriteNode('./assets/sprites/start1.png',
                                       parent = self,
                                       position = start_button_position,
                                       scale = 1)
        
        help_button_position = Vector2(self.size_of_screen_x * 0.55, self.size_of_screen_y * (0.75/3))
        self.help_button = SpriteNode('./assets/sprites/help1.png',
                                       parent = self,
                                       position = help_button_position,
                                       scale = 1)
    
        credits_button_position = Vector2(self.size_of_screen_x * (0.55), self.size_of_screen_y * (0.25/3))
        self.credits_button = SpriteNode('./assets/sprites/credits.png',
                                       parent = self,
                                       position = credits_button_position,
                                       scale = 1)
    
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
        if self.start_button.frame.contains_point(touch.location):
            self.present_modal_scene(GameScene())
        
        #if this button is touched, go to help scene
        if self.help_button.frame.contains_point(touch.location):
            self.present_modal_scene(HelpScene())
         
         #if button is touched, go to credits scene
        if self.credits_button.frame.contains_point(touch.location):
            self.present_modal_scene(CreditsScene())
         
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
    
