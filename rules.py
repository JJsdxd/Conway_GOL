#Less than two neighbours = DEAD cell
#More than three live neighbours = DEAD
#Two or Three neighbours while alive = stays alive
#Dead cell with three live neighbours = becomes alive
def cell_next_state_isAlive(cell_state,alive_neighbour_count):
    if cell_state == 1:
        if alive_neighbour_count <2 or alive_neighbour_count > 3:
            return False
        else:
            return True
    else:
        if alive_neighbour_count == 3:
            return True
        else:
            return False

