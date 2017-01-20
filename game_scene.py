# Created by: Mr.Coxall
# Modified by: Sheldon H
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows a splash screen for 2 seconds,
#   then transitions to the main menu.
from __future__ import division
from numpy import random
from scene import *
import time
import ui
import sound


class GameScene(Scene):
    def setup(self):
        
        # this method is called, when user moves to this scene
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        
        self.score_position = Vector2()
        self.left_button_down = False
        self.right_button_down = False
        self.dash_button_down = False
        self.character_move_speed =20.0
        self.dash_move_speed = 40.0
        self.arrows = []
        self.arrow_rate= 1
        self.arrow_speed = 5.0
        self.arrow_size = 0.5
        self.scale_size = 0.75
        self.hearts = 3
        self.dead = False
        self.score = 0
        self.walking_counter =time.time()
        self.left_limit = 30
        self.right_limit = 1012
        
        #add background colour
        background_position = Vector2(self.size_of_screen_x * 0.5, self.size_of_screen_y * 0.5)
        background_size = Vector2(self.size_of_screen_x, self.size_of_screen_y)
        self.background = SpriteNode('./assets/sprites/full_background.png',
                                    position = background_position,
                                    parent =self,
                                    size = background_size)
        
        #character
        
        character_position = Vector2(self.size_of_screen_x * 0.5, self.size_of_screen_y *(1/6))
        #character_position.x = 500
        #character_position.y = 125
        self.character = SpriteNode('./assets/sprites/character.png',
                                    parent = self,
                                    position = character_position,
                                    scale = self.scale_size)
       
       
        #left button
        left_button_position = Vector2(self.size_of_screen_x * (1/6), self.size_of_screen_y * (1/18))
        self.left_button = SpriteNode('./assets/sprites/left_button1.png',
                                      parent = self,
                                      position = left_button_position,
                                      scale = 0.9,
                                      alpha = 0.5)
        
        #right button
        right_button_position = Vector2(self.size_of_screen_x * (1/2.5), self.size_of_screen_y * (1/18))
        self.right_button = SpriteNode('./assets/sprites/right_button1.png',
                                       parent = self,
                                       position = right_button_position,
                                       scale = 0.9,
                                       alpha = 0.5)
        
        #dash button
        dash_button_position = Vector2(self.size_of_screen_x *(2/2.3), self.size_of_screen_y * (1/8.5))
        self.dash_button = SpriteNode('./assets/sprites/dash_button1.png',
                                       parent = self,
                                       position = dash_button_position,
                                       scale = 0.9,
                                       alpha = 0.5)
        
        #Score Label
        self.score_position = Vector2(self.size_of_screen_x * (0.5/6), self.size_of_screen_y * (5.7/6))
        self.score_label = LabelNode(text = 'Score: 0',
                                     font=('Helvetica', 40),
                                     parent = self,
                                     position = self.score_position)
        #Life Bar
        life_bar_position = Vector2(self.size_of_screen_x * (4.938/6), self.size_of_screen_y* (5.5/6))
        self.life_bar= SpriteNode('./assets/sprites/3_hearts.png',
                                 parent = self,
                                 position = life_bar_position)
        
    def update (self):
        # this method is called, hopefully, 60 times a second
        # move the character if button down
        

          #Setting Boundaries
        if self.character.position.x <= self.left_limit:
            self.left_button_down = False
        #If left button is pressed down, then move the character to the left
        if self.left_button_down == True and not self.dead:
             
             characterMove = Action.move_by(-1*self.character_move_speed, 
                                           0.0, 
                                           0.1)
             self.character.run_action(characterMove)
             
             
             #Counter texture change
             if time.time() - self.walking_counter > 0.1 and not self.dead:
                 self.character.texture = Texture('./assets/sprites/walking.png')
             
             if time.time() - self.walking_counter > 0.2 and not self.dead:
                 self.character.texture = Texture('./assets/sprites/walking1.png')

             if time.time() - self.walking_counter > 0.3 and not self.dead:
                 self.character.texture = Texture('./assets/sprites/walking2.png')
                 
             if time.time() - self.walking_counter > 0.4 and not self.dead:
                 self.character.texture = Texture('./assets/sprites/walking3.png')
                 self.walking_counter = time.time()
         
         
             
        

          #Setting Boundaries
        if self.character.position.x >= self.right_limit:
            self.right_button_down = False
          
          #If button held down move right
        if self.right_button_down == True and not self.dead:
        	
            self.character.texture = Texture('./assets/sprites/walking1.png')
            characterMove = Action.move_by(self.character_move_speed, 
                                           0.0, 
                                           0.1)
            self.character.run_action(characterMove)
            
            #Walking Textures
            if time.time() - self.walking_counter > 0.1 and not self.dead:
                self.character.texture = Texture('./assets/sprites/walking.png')
             
            if time.time() - self.walking_counter > 0.2 and not self.dead:
                self.character.texture = Texture('./assets/sprites/walking1.png')

            if time.time() - self.walking_counter > 0.3 and not self.dead:
                self.character.texture = Texture('./assets/sprites/walking2.png')
                 
            if time.time() - self.walking_counter > 0.4 and not self.dead:
                self.character.texture = Texture('./assets/sprites/walking3.png')
                self.walking_counter = time.time()
             
            
          
          #Setting Boundaries
        if self.character.position.x <= self.left_limit:
            self.left_button_down = False
        
        if self.character.position.x >= self.right_limit:
            self.right_button_down = False
        #double the speed when held down
        #Dash Right
        if self.dash_button_down == True and not self.dead:
            if self.right_button_down == True and not self.dead:
                
                
                characterMoveDash = Action.move_by(self.dash_move_speed, 
                                               0, 
                                               0.1)
                self.character.run_action(characterMoveDash)
                
                if time.time() - self.walking_counter > 0.1 and not self.dead:
                    self.character.texture = Texture('./assets/sprites/walking.png')
             
                if time.time() - self.walking_counter > 0.2 and not self.dead:
                    self.character.texture = Texture('./assets/sprites/walking1.png')

                if time.time() - self.walking_counter > 0.3 and not self.dead:
                    self.character.texture = Texture('./assets/sprites/walking2.png')
                 
                if time.time() - self.walking_counter > 0.4 and not self.dead:
                    self.character.texture = Texture('./assets/sprites/walking3.png')
                    self.walking_counter = time.time()

            #Dash Left
            if self.left_button_down == True and not self.dead:
                
                characterMoveDash = Action.move_by(-1*self.dash_move_speed, 
                                               0, 
                                               0.1)
                self.character.run_action(characterMoveDash)
                
                if time.time() - self.walking_counter > 0.1 and not self.dead:
                    self.character.texture = Texture('./assets/sprites/walking.png')
             
                if time.time() - self.walking_counter > 0.2 and not self.dead:
                    self.character.texture = Texture('./assets/sprites/walking1.png')

                if time.time() - self.walking_counter > 0.3 and not self.dead:
                    self.character.texture = Texture('./assets/sprites/walking2.png')
                 
                if time.time() - self.walking_counter > 0.4 and not self.dead:
                    self.character.texture = Texture('./assets/sprites/walking3.png')
                    self.walking_counter = time.time()


                
            #check if an arrow should spawn
        arrow_create_chance = random.randint(1,8)
        if arrow_create_chance <= self.arrow_rate:
            self.add_arrow()
        
        #Remove arrow when it hits the ground
        for arrow in self.arrows:
            if arrow.position.y == 130:
                arrow.remove_from_parent()
                self.arrows.remove(arrow)
                self.score = self.score + 10
            else:
                pass
        
        #When a arrow hits the character, lose 1 heart. If at 1 heart and an arrow hits, game over
        if len(self.arrows) > 0:
            #print('checking')
            for arrow_hit in self.arrows:
                #print('arrows ->' + str(arrows_hitframe))
                #print('character  ->' + str(self.character.frame))
                if arrow_hit.frame.intersects(self.character.frame):
                    
                    #print('a hit')
                    self.hearts = self.hearts - 1
                    arrow_hit.remove_from_parent()
                    self.arrows.remove(arrow_hit)
                    #Sound Effect
                    sound.play_effect('arcade:Hit_4',1)

#If hit once
                    if self.hearts == 2:
                    	
                        life_bar_position = Vector2(self.size_of_screen_x * (5/6),self.size_of_screen_y* (5.5/6))
                        self.life_bar= SpriteNode('./assets/sprites/2_hearts.png',
                                 parent = self,
                                 position = life_bar_position)

#If hit twice
                    if self.hearts == 1:
	
                        life_bar_position = Vector2(self.size_of_screen_x * (5/6), self.size_of_screen_y * (5.5/6))
                        self.life_bar= SpriteNode('./assets/sprites/1_heart.png',
                                 parent = self,
                                 position = life_bar_position)
#Dead
                    if self.hearts == 0:
                        
                        #When Dead show 0 hearts
                        life_bar_position = Vector2(self.size_of_screen_x * (5/6), self.size_of_screen_y* (5.5/6))
                        self.life_bar= SpriteNode('./assets/sprites/0_hearts.png',
                                 parent = self,
                                 position = life_bar_position)
                        self.dead = True
                        
                        #Show return to menu button
                        menu_button_position = Vector2(self.size_of_screen_x * (1/2), self.size_of_screen_y* (1.5/4))
                        
                        self.menu_button = SpriteNode('./assets/sprites/menu1.png',
                                      parent = self,
                                      position = menu_button_position ,
                                      alpha = 1,
                                      scale = 0.5)
                        #Show game over 
                        self.game_over = SpriteNode('./assets/sprites/game_over.png',
                                      parent = self,
                                      position = Vector2(self.size_of_screen_x * (1.1/2), self.size_of_screen_y* (1/2)),
                                      alpha = 1,
                                      scale = 2.5)
                        #Show the dead texture
                        self.character.texture = Texture('./assets/sprites/dead.png')
                        
                        
                        
                        

                    # since game over, move to next scene
        else:
            pass

        # update every frame the current score
        if self.dead == False:
            self.score_label.text = 'Score: ' + str(self.score)

            
    def touch_began(self, touch):
        # this method is called, when user touches the screen
       
        if self.dash_button.frame.contains_point(touch.location):
            self.dash_button_down = True
            
        if self.left_button.frame.contains_point(touch.location):
            self.left_button_down = True
            
        if self.right_button.frame.contains_point(touch.location):
            self.right_button_down = True              	
            
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        #If I remove my finger, then the character shouldn't move anymore
        
        self.left_button_down = False
        self.right_button_down = False
        self.dash_button_down = False
        
        if self.dead == True:
            # if start button is pressed, go to game scene
            if self.menu_button.frame.contains_point(touch.location):
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
    
    def add_arrow(self):
        arrow_start_position = Vector2()
        #Width of spawn
        arrow_start_position.x = random.randint(970)
                                 
        #Arrow Spawn
        arrow_start_position.y = self.size_of_screen_y + 100
        arrow_end_position = Vector2()
        arrow_end_position.x = arrow_start_position.x
                              
        #Arrow stops at this position
        arrow_end_position.y = 130
        
        self.arrows.append(SpriteNode('./assets/sprites/arrow.png',
                             position = arrow_start_position,
                             parent = self,
                             scale = self.arrow_size))
        
        # make an arrow move
        arrowMoveAction = Action.move_to(arrow_end_position.x, 
                                         arrow_end_position.y, 
                                         self.arrow_speed,
                                         TIMING_SINODIAL)
        self.arrows[len(self.arrows)-1].run_action(arrowMoveAction)
        
    


