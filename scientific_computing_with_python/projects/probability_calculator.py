import copy
import random

class Hat:
    def __init__(self, **args):
        self.contents = []
        for key, val in args.items():
            self.contents.extend([key] * val)
        
    def draw(self, num_balls):
        balls_drawn = []

        if num_balls > len(self.contents):
            balls_drawn = self.contents
            self.contents = []
            return balls_drawn

        for _ in range(num_balls):
            ball_drawn = random.choice(self.contents)
            self.contents.remove(ball_drawn)
            balls_drawn.append(ball_drawn)

        return balls_drawn
    
    def __str__(self):
        return ' '.join(self.contents)

def valid_balls(balls_drawn, expected_balls):
    for ball, num_balls in expected_balls.items():
        for _ in range(num_balls):
            try:
                balls_drawn.remove(ball)
            except ValueError:
                return False
    return True

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    for _ in range(num_experiments):
        curr_hat = copy.deepcopy(hat)
        balls_drawn = curr_hat.draw(num_balls_drawn)
        successes += 1 if valid_balls(balls_drawn, expected_balls) else 0
    return successes / num_experiments


hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

hat = Hat(black=6, red=4, green=3)

probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(probability)

