#Schlange

### DATA 
Snake = { growth: 0,
          body: [],
          direction: "up"
        }

fruit = [Math.random(X)+1; Math.random(Y)+1] 


# function
def move_head(head):
  if Snake.dir ='up':
      return [ head.x , head.y+1]
  else if Snake.dir = 'down':
      return [ head.x, head.y-1]
  else if Snake.dir = 'left':
      return [ head.x-1, head.y ]
  else if Snake.dir = 'right':
      return [ head.x+1, head.y]

# function
def move_body():
  if snake.growth == 0:
     tail = Snake.body[0;-1]
  else:
     Snake.growth--
     tail = Snake.body
  Snake.body = [ new head, tail ]
  return


## GAME STARTS HERE
def main_loop():
    wait_for_frame();
    new_head = move_head(snake.body[0])
    # check collisions
    if check_wall(new_head) and check_body(new_head):
        game_over()
    else if collision(new_head, fruit):
        snake.growth = 1;
    move_body()
    draw()

# function
def collision(a, b):
  if ( a.x = b.x ) and ( a.y = b.y ): return True

# function
def check_wall(head):
  if head.x > x : return True
  if head.y > y : return True
  if head.x < 0 : return True
  if head.y < y : return True

# function
def check_body(head):
  if head in Snake.body:
    return True

# function
def new_fruit():
  while collision(fruit, snake.body)
    fruit.x = Math.random(X)+1;
    fruit.y = Math.random(Y)+1;
  return

# TODO

def wait_for_frame():
    ## TODO


def draw():
    ## TODO
