# The Three Musketeers Game

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.

def create_board():
    global board
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    board = [ [r, r, r, r, m],
              [r, r, r, r, r],
              [r, r, m, r, r],
              [r, r, r, r, r],
              [m, r, r, r, r] ]

def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board

def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board

def string_to_location(s):
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4))."""
    assert s[0] >= 'A' and s[0] <= 'E'
    assert s[1] >= '1' and s[1] <= '5'
    #pass # Replace with code
    return (int(ord(s[0])-65),int(s[1])-1)
    
def location_to_string(location):
    """Returns the string representation of a location."""
    assert location[0] >= 0 and location[0] <= 4
    assert location[1] >= 0 and location[1] <= 4
    #pass # Replace with code
    return chr(location[0]+65)+str(location[1]+1)
    #test chr(0+65)+str(4+1)

def at(location):
    """Returns the contents of the board at the given location."""
    return board[location[0]][location[1]]

def all_locations():
    """Returns a list of all 25 locations on the board."""
    #pass # Replace with code
    all_loc=[]
    c=0
    d=0
    for i in range(len(board)):
        for j in range(len(board[i])):
            all_loc.append((i,j))
    return all_loc
            

def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board."""
    column = location[0]
    row = location[1]
    if direction == "up" :
        column -= 1
    elif direction == "left" :
        row -= 1 
    elif direction == "down" :
        column += 1
    elif direction == "right" :
        row += 1
    return  (column,row)
    #pass # Replace with code

def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction."""
    new_location=adjacent_location(location,direction)
    if not(is_legal_move(location,direction)):
        return False
    if at(new_location)=="R":
        return True
    else:
        return False
    #pass # Replace with code

def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction."""
    assert at(location) == 'R'
    #test is in the board?
    if is_legal_move(location,direction):
        if at(adjacent_location(location,direction)) == '-' :
            return True
        else:
            return False
    else:
        return False
    #pass # Replace with code

def is_legal_move(location, direction):
    return(is_legal_location(adjacent_location(location,direction)))
    """Tests whether it is legal to move the piece at the location
    in the given direction."""
    pass # Replace with code

def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is."""
    all_loc = all_locations()
    for i in range(len(all_loc)):
        for key,value in directions.items():
            if at(all_loc[i]) == 'M' and who == 'M':    
                if is_legal_move_by_musketeer(all_loc[i],value):
                    return True 
            elif at(all_loc[i]) == 'R' and who == "R":
                if is_legal_move_by_enemy(all_loc[i],value):
                    return True
    return False
    #pass # Replace with code

def possible_moves_from(location):
    possible_move=[]
    global directions
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    if at(location) == '-':
        return possible_move
    elif at(location) == 'M':
        for key,value in directions.items():
            if is_legal_move_by_musketeer(location,value):
                possible_move.append(value)
        return possible_move
    elif at(location) == 'R':
        for key,value in directions.items():
            if is_legal_move_by_enemy(location,value):
                possible_move.append(value)
        return possible_move
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, []."""
    pass # Replace with code

def can_move_piece_at(location):
    if at(location) == '-':
        return False
    elif possible_moves_from(location) == []:
        return False
    else:
        return True
    """Tests whether the player at the location has at least one move available."""
    #pass # Replace with code

def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board."""
    #pass # Replace with code
    if not(location[0] in [0, 1, 2, 3, 4]) or not(location[1] in [0, 1, 2, 3, 4]):
        return False
    return True

def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board."""
    if is_legal_location(adjacent_location(location,direction)):
        return True
    else:
        return False
    #pass # Replace with code
    
def all_possible_moves_for(player):
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    all_loc = all_locations()
    possible_move_m=[]
    possible_move_r=[]
    for i in range(len(all_loc)):
        for key,value in directions.items():
            if at(all_loc[i]) == 'M' and player == 'M':    
                if is_legal_move_by_musketeer(all_loc[i],value):
                    possible_move_m.append((all_loc[i],value))
            if at(all_loc[i]) == 'R' and player =='R':
                if is_legal_move_by_enemy(all_loc[i],value):
                    possible_move_r.append((all_loc[i],value))
    
    if player == 'M':
        return possible_move_m
    elif player == 'R':
        return possible_move_r
    """Returns every possible move for the player ('M' or 'R') as a list
       (location, direction) tuples."""
    pass # Replace with code

def make_move(location, direction):
    new_location = adjacent_location(location,direction)
    board[new_location[0]][new_location[1]]= at(location)
    board[location[0]][location[1]]='-'
    return
    """Moves the piece in location in the indicated direction."""
    pass # Replace with code

#used for computing the strategy for m and r.
#basiclly calculate the smallist vertical distance between the 
def value(location,avg_col,avg_row):
    dis_col=abs(location[0]-avg_col)
    dis_row=abs(location[1]-avg_row)
    return(dis_col,dis_row)

def choose_computer_move(who):
    temp_move_collective=all_possible_moves_for(who)
    temp_move=temp_move_collective[0]
    #compute the m position average
    avg_row=0
    avg_col=0
    for i in range(len(m_position())):
        avg_col += m_position()[i][0]
        avg_row += m_position()[i][1]
    avg_col/=3
    avg_row/=3

    if who == 'M':
        for i in range(len(temp_move_collective)):
            if value(adjacent_location(temp_move_collective[i][0],temp_move_collective[i][1]),avg_col,avg_row)\
            >value(adjacent_location(temp_move[0],temp_move[1]),avg_col,avg_row):
                temp_move= temp_move_collective[i]
    
    if who == 'R':
        for i in range(len(temp_move_collective)):
            if value(adjacent_location(temp_move_collective[i][0],temp_move_collective[i][1]),avg_col,avg_row)\
            <value(adjacent_location(temp_move[0],temp_move[1]),avg_col,avg_row):
                temp_move= temp_move_collective[i]
    return temp_move
        
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual."""
    pass # Replace with code

def m_position():
    m_position=[]
    for i in range(len(all_locations())) :
        for key,value in directions.items():
            if at(all_locations()[i]) == 'M':
                m_position.append(all_locations()[i])
    return m_position

def samerow(location1,location2):
    if location1[0] == location2[0]:
        return True
    if location1[1] == location2[1]:
        return True
    return False

def is_enemy_win():
    for i in range(len(m_position())):
        for j in range(len(m_position())):
            if not(samerow(m_position()[i],m_position()[j])):
                return False
    return True
                 
    """Returns True if all 3 Musketeers are in the same row or column."""
    #pass # Replace with code
    

#---------- Communicating with the user ----------

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end = " ")
        for j in range(0, 5):
            print(board[i][j] + " ", end = " ")
        print()
        ch = chr(ord(ch) + 1)
    print()

def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""    
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move()

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')         
        make_move(location, direction)
        describe_move("Musketeer", location, direction)
        
def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')         
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from',\
          location_to_string(location), 'to',\
          location_to_string(new_location) + ".\n")

def start():
    """Plays the Three Musketeers Game."""
    users_side = choose_users_side()
    board = create_board()
    print_instructions()
    print_board()
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print("The Musketeers win!")
            break        

if __name__ == '__main__':
    start()