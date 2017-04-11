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
        self.grid = [[1],[0,0],[1,0,1],[0,1,0,0],[1,0,1,0,1]]

    def create_ball_set(self):
        """
        This function returns a list containing
        a shuffled pool balls set
        """
        balls = []
        [balls.append([number]) for number in range(1, 16)]
        for ball in balls:
            if ball[0] < 9:
                ball.append("Solid")
            else:
                ball.append("Striped")
        shuffle(balls)
        return balls

    def sort_ball_set(self, unsorted_balls):
        """
        This function returns a
        list of sorted balls from a list of
        shuffled balls
        """
        # Ball 1 always goes in 1st place
        self.grid[0][0] = unsorted_balls.pop(unsorted_balls.index([1, 'Solid']))
        # Ball 8 always goes in the 2nd row, in the middle
        self.grid[2][1] = unsorted_balls.pop(unsorted_balls.index([8, 'Solid']))
        # Creating an empty list for solid balls
        unsorted_solid_balls = []
        # Same thing but for striped balls
        unsorted_striped_balls = []

        # Now it is time to divide solid balls from striped ones
        for ball in unsorted_balls:
            if ball[1] == 'Solid':
                unsorted_solid_balls.append(ball)
            elif ball[1] == 'Striped':
                unsorted_striped_balls.append(ball)

        # Once the balls are divided it is time to put them in the grid
        for grid_row_index, grid_row in enumerate(self.grid):
            for grid_col_index, grid_col_value in enumerate(grid_row):
                # In their corresponding placeholder spot
                if grid_col_value == 1:
                    # 1 is for solid balls
                    self.grid[grid_row_index][grid_col_index] = unsorted_solid_balls.pop()
                elif grid_col_value == 0:
                    # 0 is for striped balls
                    self.grid[grid_row_index][grid_col_index] = unsorted_striped_balls.pop()
        return self.grid

pool_table = Pool()
print "Getting new set of balls from the pool table:"
unsorted_balls = pool_table.create_ball_set()
print unsorted_balls
print "Sorted balls:"
sorted_balls = pool_table.sort_ball_set(unsorted_balls)
# Pretty printing sorted balls
for row in sorted_balls:
    print row