from random import shuffle

class Pool(object):
    """
    Simple object that allows to sort
    """

    def __init__(self):
        """
        During initalization the final grid containing
        ordered balls is created
        1 is placeholder for Solid balls
        0 is placeholder for Striped balls
        """
        self.GRID = [[1], [0, 0], [1, 0, 1], [0, 1, 0, 0], [1, 0, 1, 0, 1]]

    def is_ball_solid(self, ball):
        """
        Checks if a ball is solid or striped
        
        :return:
        String containing Solid or Striped
        """
        if ball < 9:
            return "Solid"
        else:
            return "Striped"

    def create_ball_set(self):
        """
        Creates a list containing
        a shuffled pool balls set
        
        :return:
        A list containing 15 balls.
        Each ball is a tuple containing number and
        Solid or Striped attribute.
        """
        balls = [number for number in range(1, 16)]
        balls = [(ball, self.is_ball_solid(ball)) for ball in balls]
        shuffle(balls)
        return balls

    def sort_ball_set(self, unsorted_balls):
        """
        Sorts a list of unsorted_balls

        :return:
        A list-made grid representing a pool triangle
        """
        # Ball 1 always goes in 1st row, 1st column
        self.GRID[0][0] = unsorted_balls.pop(unsorted_balls.index((1, 'Solid')))
        # Ball 8 always goes in the 3rd row, 2nd column
        self.GRID[2][1] = unsorted_balls.pop(unsorted_balls.index((8, 'Solid')))

        # Creating an empty list for solid balls
        unsorted_solid_balls = []
        # Same thing for striped balls
        unsorted_striped_balls = []
        # Let's divide solid balls from striped ones
        for ball in unsorted_balls:
            if ball[1] == 'Solid':
                unsorted_solid_balls.append(ball)
            elif ball[1] == 'Striped':
                unsorted_striped_balls.append(ball)

        # Once the balls are divided it is time to put them in the grid
        for grid_row_index, grid_row in enumerate(self.GRID):
            for grid_col_index, grid_col_value in enumerate(grid_row):
                # In their corresponding placeholder spot
                if grid_col_value == 1:
                    # 1 is for solid balls
                    self.GRID[grid_row_index][grid_col_index] = unsorted_solid_balls.pop()
                elif grid_col_value == 0:
                    # 0 is for striped balls
                    self.GRID[grid_row_index][grid_col_index] = unsorted_striped_balls.pop()
        return self.GRID

pool_table = Pool()
print "Getting new set of balls from the pool table:"
unsorted_balls = pool_table.create_ball_set()
print unsorted_balls
print "Sorted balls:"
sorted_balls = pool_table.sort_ball_set(unsorted_balls)
# Pretty printing sorted balls
for row in sorted_balls:
    print row
