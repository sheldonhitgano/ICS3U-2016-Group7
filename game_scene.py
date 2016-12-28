
# Created by: Sheldon H
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows a splash screen for 2 seconds,
#   then transitions to the main menu.
from numpy import random
from scene import *
import ui



class GameScene(Scene):
    def setup(self):
        
        # this method is called, when user moves to this scene
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        
        self.score_position = Vector2()
        self.center_of_screen = self.size/2
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
        self.health = 3
        
        
        
        #add background colour
        background_position = self.center_of_screen
        background_position.y = 100
        self.background = SpriteNode('./assets/sprites/full_background.png',
                                    position = self.size/2,
                                    parent =self,
                                    size = self.size)
        
        #character
        
        character_position = self.center_of_screen
        character_position.y = 125
        self.character = SpriteNode('./assets/sprites/character.png',
                                    parent = self,
                                    position = character_position,
                                    scale = self.scale_size)
       
       
        #left button
        left_button_position = self.center_of_screen
        left_button_position.x = 150
        left_button_position.y = 75
        self.left_button = SpriteNode('./assets/sprites/left_button1.png',
                                      parent = self,
                                      position = left_button_position,
                                      alpha = 0.5)
        
        #right button
        right_button_position = self.center_of_screen
        right_button_position.x = 400
        right_button_position.y = 75
        self.right_button = SpriteNode('./assets/sprites/right_button1.png',
                                       parent = self,
                                       position = right_button_position,
                                       alpha = 0.5)
        
        #dash button
        dash_button_position = self.center_of_screen
        dash_button_position.x= 900
        dash_button_position.y= 75
        self.dash_button = SpriteNode('./assets/sprites/dash_button.png',
                                       parent = self,
                                       position = dash_button_position)
        
        #Score Label
        self.score_position.x = 100
        self.score_position.y = self.size_of_screen_y - 50
        self.score_label = LabelNode(text = 'Score: 0',
                                     font=('Helvetica', 40),
                                     parent = self,
                                     position = self.score_position)



    def update (self):
        # this method is called, hopefully, 60 times a second
        # move the character if button down
        
        #If button held down, move left
        if self.left_button_down == True:
             characterMove = Action.move_by(-1*self.character_move_speed, 
                                           0.0, 
                                           0.1)
             self.character.run_action(characterMove)
        #If button held down. move right
        if self.right_button_down == True:
            characterMove = Action.move_by(self.character_move_speed, 
                                           0.0, 
                                           0.1)
            self.character.run_action(characterMove)
        
        #double the speed when held down
        #Dash Right
        if self.dash_button_down == True:
            if self.right_button_down == True:
             
                characterMoveDash = Action.move_by(self.dash_move_speed, 
                                               0, 
                                               0.1)
                self.character.run_action(characterMoveDash)
            
            #Dash Left
            if self.left_button_down == True:
                
                characterMoveDash = Action.move_by(-1*self.dash_move_speed, 
                                               0, 
                                               0.1)
                self.character.run_action(characterMoveDash)
            
            
            #check if an arrow should spawn
        arrow_create_chance = random.randint(1,13)
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
        
        #When a arrow hits the character, game over
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
                    
                    if self.hearts == 0:
                        self.dead = True
                    	
                        self.menu_button = SpriteNode('./assets/sprites/menu.png',
                                      parent = self,
                                      position = Vector2(self.screen_center_x, 
                                                         self.screen_center_y),
                                      alpha = 1.0,
                                      scale = self.scale_size)
                    	
                        self.character.remove_from_parent()
                        
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
        #If I remove my finger, then the spaceship shouldn't move anymore
        
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
        arrow_start_position.x = random.randint(970)
                                 
       
        arrow_start_position.y = self.size_of_screen_y + 100
        arrow_end_position = Vector2()
        arrow_end_position.x = arrow_start_position.x
                              
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
        
    



        #character
        
        character_position = self.center_of_screen
        character_position.y = 125
        self.character = SpriteNode('./assets/sprites/character.png',
                                    parent = self,
                                    position = character_position,
                                    scale = self.scale_size)
       
       
        #left button
        left_button_position = self.center_of_screen
        left_button_position.x = 150
        left_button_position.y = 75
        self.left_button = SpriteNode('./assets/sprites/left_button1.png',
                                      parent = self,
                                      position = left_button_position,
                                      alpha = 0.5)
        
        #right button
        right_button_position = self.center_of_screen
        right_button_position.x = 400
        right_button_position.y = 75
        self.right_button = SpriteNode('./assets/sprites/right_button1.png',
                                       parent = self,
                                       position = right_button_position,
                                       alpha = 0.5)
        
        #dash button
        dash_button_position = self.center_of_screen
        dash_button_position.x= 900
        dash_button_position.y= 75
        self.dash_button = SpriteNode('./assets/sprites/dash_button.png',
                                       parent = self,
                                       position = dash_button_position)
        
        #Score Label
        self.score_position.x = 100
        self.score_position.y = self.size_of_screen_y - 50
        self.score_label = LabelNode(text = 'Score: 0',
                                     font=('Helvetica', 40),
                                     parent = self,
                                     position = self.score_position)



    def update (self):
        # this method is called, hopefully, 60 times a second
        # move the character if button down
        
            
        if self.left_button_down == True:
             characterMove = Action.move_by(-1*self.character_move_speed, 
                                           0.0, 
                                           0.1)
             self.character.run_action(characterMove)
        
        if self.right_button_down == True:
            characterMove = Action.move_by(self.character_move_speed, 
                                           0.0, 
                                           0.1)
            self.character.run_action(characterMove)
        
        #double the speed when held down
        
        if self.dash_button_down == True:
            if self.right_button_down == True:
             
                characterMoveDash = Action.move_by(self.dash_move_speed, 
                                               0, 
                                               0.1)
                self.character.run_action(characterMoveDash)
            
            
            if self.left_button_down == True:
                
                characterMoveDash = Action.move_by(-1*self.dash_move_speed, 
                                               0, 
                                               0.1)
                self.character.run_action(characterMoveDash)
            
            
            #check if an arrow should spawn
        arrow_create_chance = random.randint(1,13)
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
        
        #When a arrow hits the character, game over
        if len(self.arrows) > 0:
            #print('checking')
            for arrow_hit in self.arrows:
                #print('arrows ->' + str(arrows_hitframe))
                #print('character  ->' + str(self.character.frame))
                if arrow_hit.frame.intersects(self.character.frame):
                    #print('a hit')
                    self.character.remove_from_parent()
                    arrow_hit.remove_from_parent()
                    self.arrows.remove(arrow_hit)
                    
                    self.dead = True
                    
                    self.menu_button = SpriteNode('./assets/sprites/menu.png',
                                      parent = self,
                                      position = Vector2(self.screen_center_x, 
                                                         self.screen_center_y),
                                      alpha = 1.0,
                                      scale = self.scale_size)
                    
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
        #If I remove my finger, then the spaceship shouldn't move anymore
        
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
        arrow_start_position.x = random.randint(970)
                                 
       
        arrow_start_position.y = self.size_of_screen_y + 100
        arrow_end_position = Vector2()
        arrow_end_position.x = arrow_start_position.x
                              
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
        
    



        character_position.y = 125
        self.character = SpriteNode('./assets/sprites/character.png',
                                    parent = self,
                                    position = character_position,
                                    scale = self.scale_size)
       
       
        #left button
        left_button_position = self.center_of_screen
        left_button_position.x = 150
        left_button_position.y = 75
        self.left_button = SpriteNode('./assets/sprites/left_button1.png',
                                      parent = self,
                                      position = left_button_position,
                                      alpha = 0.5)
        
        #right button
        right_button_position = self.center_of_screen
        right_button_position.x = 375
        right_button_position.y = 75
        self.right_button = SpriteNode('./assets/sprites/right_button1.png',
                                       parent = self,
                                       position = right_button_position,
                                       alpha = 0.5)
        
        #dash button
        dash_button_position = self.center_of_screen
        dash_button_position.x= 900
        dash_button_position.y= 75
        self.dash_button = SpriteNode('./assets/sprites/dash_button.png',
                                       parent = self,
                                       position = dash_button_position)
        
        #Score Label
        self.score_position.x = 100
        self.score_position.y = self.size_of_screen_y - 50
        self.score_label = LabelNode(text = 'Score: 0',
                                     font=('Helvetica', 40),
                                     parent = self,
                                     position = self.score_position)



    def update (self):
        # this method is called, hopefully, 60 times a second
        # move the character if button down
            
        if self.left_button_down == True:
            characterMove = Action.move_by(-1*self.character_move_speed, 
                                           0.0, 
                                           0.1)
            self.character.run_action(characterMove)
        
        if self.right_button_down == True:
            characterMove = Action.move_by(self.character_move_speed, 
                                           0.0, 
                                           0.1)
            self.character.run_action(characterMove)
        
        #double the speed when held down
        
        if self.dash_button_down == True:
            
            if self.right_button_down == True:
             
                characterMove = Action.move_by(2*self.character_move_speed, 
                                               0, 
                                               0.1)
            self.character.run_action(characterMove)
            
            
            if self.left_button_down == True:
                
                characterMove = Action.move_by(-2*self.character_move_speed, 
                                               0, 
                                               0.1)
            self.character.run_action(characterMove)
            
            
            #check if an arrow should spawn
        arrow_create_chance = random.randint(1,7.5)
        if arrow_create_chance <= self.arrow_rate:
            self.add_arrow()
        
        #Remove arrow when it hits the ground
        for arrow in self.arrows:
            if arrow.position.y == 130:
                arrow.remove_from_parent()
                self.arrows.remove(arrow)
                self.score = self.score + 10
        
        #When a arrow hits the character, game over
        if len(self.arrows) > 0:
            #print('checking')
            for arrow_hit in self.arrows:
                #print('arrows ->' + str(arrows_hitframe))
                #print('character  ->' + str(self.character.frame))
                if arrow_hit.frame.intersects(self.character.frame):
                    #print('a hit')
                    self.character.remove_from_parent()
                    arrow_hit.remove_from_parent()
                    self.arrows.remove(arrow_hit)
                    
                    self.dead = True
                    
                    self.menu_button = SpriteNode('./assets/sprites/menu.png',
                                      parent = self,
                                      position = Vector2(self.screen_center_x, 
                                                         self.screen_center_y),
                                      alpha = 1.0,
                                      scale = self.scale_size)
                    
                    # since game over, move to next scene
        else:
            pass

        # update every frame the current score
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
        #If I remove my finger, then the spaceship shouldn't move anymore
        
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
        arrow_start_position.x = random.randint(970)
                                 
       
        arrow_start_position.y = self.size_of_screen_y + 100
        arrow_end_position = Vector2()
        arrow_end_position.x = arrow_start_position.x
                              
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
        
    


