import Viewer

EMPTY = 0
WALL = 1
START = 2
END = 3
VISITED = 4
    
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

if __name__ == "__main__":
    grid = [
        [ WALL,  WALL,  EMPTY,  WALL,  WALL,  WALL,  WALL,  EMPTY,  WALL, WALL],
        [START, EMPTY,  WALL,  WALL, EMPTY, EMPTY, EMPTY, EMPTY,  WALL, WALL],
        [ WALL, EMPTY, EMPTY, WALL, EMPTY, EMPTY,  WALL, EMPTY,  WALL, WALL],
        [ WALL,  WALL,  WALL,  EMPTY, EMPTY,  WALL, EMPTY,  WALL, EMPTY, WALL],
        [ WALL, WALL, EMPTY, EMPTY, EMPTY,  WALL, EMPTY, WALL, EMPTY, WALL],
        [ WALL,  WALL, EMPTY,  WALL,  WALL, WALL, EMPTY,  WALL, EMPTY, WALL],
        [ WALL,  WALL, EMPTY, EMPTY, EMPTY, EMPTY,  WALL,  WALL, EMPTY,  END],
        [ WALL,  WALL,  WALL,  EMPTY,  WALL,  WALL,  EMPTY,  WALL,  WALL, EMPTY],
    ]
                    
    Viewer.view(grid)


    print("Find a solution to get from ^^ to $$, using the characters " 
        + "'" + NORTH + "', '" + EAST + "', '" + SOUTH + "' and '" + WEST + "'"
        + " (for north, east, south and west).")
    solution = input("Your solution: ")

    row = 1
    col = 0
    done = False
    solved = False
    charIndex = 0
    solutionLength = len(solution)

    while not done and charIndex < solutionLength:
        
        direction = solution[charIndex]
        print("Location: (" + str(row) + ", " + str(col) 
            + "), next direction: '" + direction + "'")
        
        if direction == NORTH:
            row -= 1
            
        elif direction == EAST:
            col += 1
                
        elif direction == SOUTH:
            row += 1
                
        elif direction == WEST:
            col -= 1
        
        else:
            print("Future archeologists gaze upon your remains in bafflement.") # Invalid direction.
        
        if (row < 0 or col < 0 
                        or row >= len(grid) 
                        or col >= len(grid[row])):
            done = True
            print("You stumble blindly into a solid concrete wall.") # Out of bounds.
            
        else:
            cell = grid[currentRow][currentCol]
            if cell == EMPTY:
                grid[currentRow][currentCol] = VISITED
            elif cell == WALL:
                done = True
                print("You stumble blindly into a solid concrete wall.")
            elif cell == END:
                done = True
                solved = True
                print("SOLVED!")
            else:
                pass # Do nothing
        
        charIndex += 1
    # end-while


    if not solved:
        print("MESSAGE 5") # Did not reach the end.


    Viewer.view(grid)
