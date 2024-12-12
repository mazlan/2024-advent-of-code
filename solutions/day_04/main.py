# Part 1
def search_xmas():
    grid = []
    count = 0
    with open("input.txt") as f:
        for line in f:
            grid.append(list(line.strip()))
            
    rows, cols = len(grid), len(grid[0])
    
    def is_valid_bounds(row_index, column_index, delta_row, delta_column):
        """Check if the next 4 positions are within bounds"""
        for i in range(4):
            next_row_index = row_index + (delta_row * i)
            next_column_index = column_index + (delta_column * i)
            if not (0 <= next_row_index < rows and 0 <= next_column_index < cols):
                return False
        return True
    
    for row in range(rows):
        for col in range(cols):
            # Define coordinates for all 8 directions
            directions = [
                (0, 1),   # East
                (0, -1),  # West
                (-1, 0),  # North
                (1, 0),   # South
                (-1, -1), # Northwest
                (-1, 1),  # Northeast
                (1, -1),  # Southwest
                (1, 1)    # Southeast
            ]
            
            for dr, dc in directions:
                if is_valid_bounds(row, col, dr, dc):
                    if (grid[row][col] == "X" and
                        grid[row + dr][col + dc] == "M" and
                        grid[row + 2*dr][col + 2*dc] == "A" and
                        grid[row + 3*dr][col + 3*dc] == "S"):
                        count += 1    
    print(count)
    return count

# Part 2
def search_x_mas():
    grid = []
    count = 0
    with open("input.txt") as f:
        for line in f:
            grid.append(list(line.strip()))
            
    rows, cols = len(grid), len(grid[0])
    dr, dc = 1, 1

    def is_valid_bounds(row_index, column_index):
        """Check if the next position is within bounds"""
        # Define coordinates for 4 directions
        directions = [
            (-1, -1), # Northwest
            (-1, 1),  # Northeast
            (1, -1),  # Southwest
            (1, 1)    # Southeast
        ]
        for delta_row, delta_column in directions:        
            next_row_index = row_index + delta_row
            next_column_index = column_index + delta_column
            if not (0 <= next_row_index < rows and 0 <= next_column_index < cols):
                return False
        return True
    
    for row in range(rows):
        for col in range(cols):            
            if is_valid_bounds(row, col):
                if (grid[row][col] == "A" and
                    grid[row + dr][col + dc] == "S" and  # Southeast
                    grid[row + dr][col - dc] == "S" and  # Southwest
                    grid[row - dr][col + dc] == "M" and  # Northeast
                    grid[row - dr][col - dc] == "M"):    # Northwest
                    count += 1
                elif (grid[row][col] == "A" and
                    grid[row + dr][col + dc] == "M" and  # Southeast
                    grid[row + dr][col - dc] == "M" and  # Southwest
                    grid[row - dr][col + dc] == "S" and  # Northeast
                    grid[row - dr][col - dc] == "S"):    # Northwest
                    count += 1
                elif (grid[row][col] == "A" and
                    grid[row + dr][col + dc] == "M" and  # Southeast
                    grid[row + dr][col - dc] == "S" and  # Southwest
                    grid[row - dr][col + dc] == "M" and  # Northeast
                    grid[row - dr][col - dc] == "S"):    # Northwest
                    count += 1
                elif (grid[row][col] == "A" and
                    grid[row + dr][col + dc] == "S" and  # Southeast
                    grid[row + dr][col - dc] == "M" and  # Southwest
                    grid[row - dr][col + dc] == "S" and  # Northeast
                    grid[row - dr][col - dc] == "M"):    # Northwest
                    count += 1
    print(count)
    return count


if __name__ == "__main__":
    search_xmas()
    search_x_mas()
