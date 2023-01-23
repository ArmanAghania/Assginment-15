import random
import arcade
import time

class Fruit(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)
        self.change_x = 0
        self.change_y = 0

class Apple(Fruit):
    def __init__(self, game):
        super().__init__(game)
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)
        self.width = 20
        self.height = 20
        self.pic=arcade.load_texture('2003315_apple_education_fitness_food_health_icon.png')

    def draw(self):
        arcade.draw_lrwh_rectangle_textured(self.center_x,self.center_y,self.width,self.height,self.pic)

class Pear(Fruit):
    def __init__(self, game):
        super().__init__(game)
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)
        self.width = 20
        self.height = 20
        self.pic=arcade.load_texture('pear-icon.png')

    def draw(self):
        arcade.draw_lrwh_rectangle_textured(self.center_x,self.center_y,self.width,self.height,self.pic)

class Melon(Fruit):
    def __init__(self, game):
        super().__init__(game)
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)
        self.width = 20
        self.height = 20
        self.pic=arcade.load_texture('melon.png')

    def draw(self):
        arcade.draw_lrwh_rectangle_textured(self.center_x,self.center_y,self.width,self.height,self.pic)

class Dragon(Fruit):
    def __init__(self, game):
        super().__init__(game)
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)
        self.width = 15
        self.height = 15
        self.pic=arcade.load_texture('dragon-fruit.png')

class Mushroom(Fruit):
    def __init__(self, game):
        super().__init__(game)
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)
        self.width = 15
        self.height = 15
        self.pic=arcade.load_texture('mushroom.png')

    def draw(self):
        arcade.draw_lrwh_rectangle_textured(self.center_x,self.center_y,self.width,self.height,self.pic)

class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 20
        self.height = 20
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.color = arcade.color.BLUE_YONDER
        self.change_x = 0
        self.change_y = 0
        self.speed = 4
        self.score = 0
        self.body = []

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)
        
        for i in range(len(self.body)):
            if i % 2 == 0:
                arcade.draw_rectangle_filled(self.body[i]['X'], self.body[i]['Y'], self.width, self.height, self.color)
            else:
                arcade.draw_rectangle_filled(self.body[i]['X'], self.body[i]['Y'], self.width, self.height, arcade.color.RED)

    def move(self):

        self.body.append({'X': self.center_x, 'Y': self.center_y})
        if len(self.body) > self.score:
            self.body.pop(0)
            
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
        


    def eat(self, fruit, ind):
        if ind == 1:
            self.score += ind
        elif ind == 2:
            self.score += ind
        elif ind == 5:
            self.score += ind
        elif ind == -5:
            self.score += ind
        elif ind == 20:
            self.score += ind

        del fruit

    def check_pass_limits(self, game):
        if self.center_x<0 or self.center_x>game.width or self.center_y<0 or self.center_y>game.height:
            game.game_status="Game Over"
        
        
    


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title='Super Snake V1.0')
        arcade.set_background_color(arcade.color.KHAKI)

        self.what = random.randint(0,2)
        self.chance = random.randint(1,30)
        self.snake = Snake(self)
        self.apple = Apple(self)
        self.pear = Pear(self)
        self.melon = Melon(self)
        self.dragon = Dragon(self)
        self.mushroom = Mushroom(self)
        self.food = self.apple
        self.ind = 1
        self.game_status="run"


    def on_draw(self):
        arcade.start_render()

        self.snake.draw()
        self.count = random.randint(1,3)
        self.food.draw()
        self.a=time.time()
        


        arcade.draw_text(f"Score: {self.snake.score}", 8*self.width//10, 20 , arcade.color.VIOLET  , bold=True)

        if self.game_status=="Game Over":
            arcade.draw_lrtb_rectangle_filled(0,self.width,self.height,0,arcade.color.BLACK)
            arcade.draw_text("GAME OVER!", self.width//5 , self.height//2 , arcade.color.RED , 30)
            
                
        arcade.finish_render()

    def on_update(self, delta_time: float):

        
        self.snake.move()

        if arcade.check_for_collision(self.snake, self.food):

            self.snake.eat(self.food, self.ind)
            self.index = random.randint(1,6)
            
            for i in range(self.count):
                if self.index ==1:
                    self.food = self.apple
                    self.ind = 1
                elif self.index == 2:
                    self.food = self.pear
                    self.ind = 2
                elif self.index == 3:
                    self.food = self.melon
                    self.ind = 5
                elif self.index == 4:
                    self.food = self.mushroom
                    self.ind = -5
                elif self.index == 5:
                    self.chance = random.randint(1,30)
                    if self.chance == 30:
                        self.food = self.dragon
                        self.ind = 20

        self.snake.check_pass_limits(self)


             
           

    def on_key_release(self, symbol: int, modifiers: int):

        if symbol == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1

        elif symbol == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1

        elif symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0

        elif symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0



if __name__ == '__main__':
    game = Game()
    arcade.run()