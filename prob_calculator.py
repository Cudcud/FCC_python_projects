import copy
import random
# Consider using the modules imported above.

class Hat:

  #**kwargs makes a keyworded, variable-length argument dictionary
  def __init__(self, **kwargs) :
    self.contents = []
    for k, v in kwargs.items():
      for i in range(v) :
        self.contents.append(k)

  def draw(self, num) :
    randomdraw = []
    if num > len(self.contents) :
      #draws all the balls at the same time
      randomdraw = random.sample(self.contents, len(self.contents))
      self.contents = []
      return randomdraw
    else :
      #i goes through a random sample of contents of size num
      for i in random.sample(self.contents, num):
        randomdraw.append(i)
        self.contents.remove(i)
      return randomdraw
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  #how many times we got the expected_balls
  M = 0
  for i in range(num_experiments) :
    #runs each experiment on a new copy of hat, because draw removes contents
    #copy copies references, deep copy actually makes a copy
    experiment_hat = copy.deepcopy(hat)
    experiment_draw = experiment_hat.draw(num_balls_drawn)
    
    #checks for match of key value, pairs in both dictionaries, returns a number of how many were matched
    experiment_draw_d = {}
    for x in experiment_draw:
      if x not in experiment_draw_d:
        experiment_draw_d[x] = 1
      else:
        experiment_draw_d[x] += 1

    #matched pairs in a draw
    m = 0
    
    for k1, v1 in experiment_draw_d.items():
      for k2, v2 in expected_balls.items():
        #v1 >= v2 takes into account when it matches more balls than necessary
        if k1 == k2 and v1 >= v2 :
          m += 1
    
    #if there are more or the same amount of matched pairs as the length of expected balls, we've got a match!
    if m >= len(expected_balls):
     M += 1
      
  return M/num_experiments
  
  
