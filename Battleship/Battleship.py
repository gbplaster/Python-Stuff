def new_board(NumRowsAndColumns):   
    board=[['0' for i in range(NumRowsAndColumns)]for i in range(NumRowsAndColumns)]
    return board

def print_player_board(board,board_size):   
    counter1=0 #controls which set we are looking at in the list (rows)
    counter2=0 #controls when we move to a new row
    counter3=1 #used to print the column numbers across the top
    c4=0 #used to print the row letters along the right side of the printout
    print "PLAYER'S BOARD"
    print"   ",
    for i in range (board_size):
        print "|", str(counter3),"|",
        counter3+=1
    print ""
        
    for i in range(board_size):
        if c4 == 0:
            print "_A_",
        elif c4 == 1:
            print "_B_",
        elif c4 == 2:
            print "_C_",
        elif c4 == 3:
            print "_D_",
        elif c4 == 4:
            print "_E_",
        elif c4 == 5:
            print "_F_", 
        elif c4 == 6:
            print "_G_",
        elif c4 == 7:
            print "_H_",
        elif c4 == 8:
            print "_I_",
        elif c4 == 9:
            print "_J_",
        elif c4 == 10:
            print "_K_",
        elif c4 == 11:
            print "_L_",
        row = []
        row = board[counter1]
        for e in row:
            if e=='0':
                print "|___|",
                counter2+=1
            if e=='X':
                print "|_X_|",
                counter2+=1
            if e=='H':
                print "|_H_|",
                counter2+=1
            if e=='S':
                print "|_S_|",
                counter2+=1
            if e=='A':
                print "|_A_|",
                counter2+=1
            if e=='B':
                print "|_B_|",
                counter2+=1
            if e=='C':
                print "|_C_|",
                counter2+=1
            if e=='D':
                print "|_D_|",
                counter2+=1
            if counter2%board_size==0:
                print ""
                c4+=1
                
        counter1 +=1
            
def print_computer_board(board,board_size): #the only difference from print player board is that a |__| is printed when a ship is listed in the list   
    counter1=0 # so that players cannot see the location of the computer's ships
    counter2=0
    counter3=1
    c4=0
    print "COMPUTER'S BOARD"
    print"   ",
    for i in range (board_size):
        print "|", str(counter3),"|",
        counter3+=1
    print ""
        
    for i in range(board_size):
        if c4 == 0:
            print "_A_",
        elif c4 == 1:
            print "_B_",
        elif c4 == 2:
            print "_C_",
        elif c4 == 3:
            print "_D_",
        elif c4 == 4:
            print "_E_",
        elif c4 == 5:
            print "_F_",
        elif c4 == 6:
            print "_G_",
        elif c4 == 7:
            print "_H_",
        elif c4 == 8:
            print "_I_",
        elif c4 == 9:
            print "_J_",
        elif c4 == 10:
            print "_K_",
        elif c4 == 11:
            print "_L_",
        row = []
        row = board[counter1]
        for e in row:
            if e=='0':
                print "|___|",
                counter2+=1
            if e=='X':
                print "|_X_|",
                counter2+=1
            if e=='H':
                print "|_H_|",
                counter2+=1
            if e=='S':
                print "|___|",
                counter2+=1
            if e=='A':
                print "|___|",
                counter2+=1
            if e=='B':
                print "|___|",
                counter2+=1
            if e=='C':
                print "|___|",
                counter2+=1
            if e=='D':
                print "|___|",
                counter2+=1
            if counter2%board_size==0:
                print ""
                c4+=1
                
        counter1 +=1
            
            
def get_row(): #This function was created to more efficiently take a row letter and return the corresponding coordinate row number
    while True:
        text_row = str(raw_input())
        if text_row[0] == 'A' or text_row[0] == 'a':
            row = 0
            return row
        elif text_row[0] == 'B' or text_row[0] == 'b':
            row = 1
            return row
        elif text_row[0] == 'C' or text_row[0] == 'c':
            row = 2
            return row
        elif text_row[0] == 'D' or text_row[0] == 'd':
            row = 3
            return row
        elif text_row[0] == 'E' or text_row[0] == 'e':
            row = 4
            return row
        elif text_row[0] == 'F' or text_row[0] == 'f':
            row = 5
            return row
        elif text_row[0] == 'G' or text_row[0] == 'g':
            row = 6
            return row
        elif text_row[0] == 'H' or text_row[0] == 'h':
            row = 7
            return row
        elif text_row[0] == 'I' or text_row[0] == 'i':
            row = 8
            return row
        elif text_row[0] == 'J' or text_row[0] == 'j':
            row = 9
            return row
        else:
            print "Invalid Row..."
            
def get_column(): # This function exists for quality control so that only valid inputs will be accepted
    while True:
        column = int(raw_input())-1
        if 0 <= column <= 9:
            return column
        else:
            print "Invalid Column"
    
                
def get_ship_text(ship,ship_part,row_or_column): # This function is used when the player is placing his ships, it cuts down on clutter for higher level functions
    if ship == "aircraft carrier":
        units_long = 5
    if ship == "battleship":
        units_long =4
    if ship == "submarine":
        units_long =3
    if ship == "cruiser":
        units_long = 3
    if ship == "destroyer":
        units_long = 2
            
    print "Choose the ",row_or_column, "for the ", ship_part, "of the your ", ship, "(", units_long, " units long)"
    
def is_valid_placement(stern_row,stern_column,bow_row,bow_column,board_size,ship_size):
    is_valid = True # if the placement can pass the below tests, is_valid remains true
    is_in_row = False
    is_in_column = False
    
    if stern_row > board_size:
        is_valid=False
    elif stern_column > board_size:
        is_valid=False
    elif bow_row > board_size:
        is_valid = False
    elif bow_column > board_size:
        is_valid = False
        
    #print "if any of the inputs are outside of the board this will come out False... ",is_valid
    if stern_row == bow_row: #test if the two ends of the ship are in the same row
        is_in_row = True
    #print "are they in the same row? ", is_in_row
    if stern_column == bow_column: #test if the two ends of the ship are in the same column
        is_in_column =True
    #print "are they in the same column? ",is_in_column
    if is_in_row ==False:
        if is_in_column == False:
            is_valid = False # the ship placement must either be in a row or column or else it is invalid
    #print "if they are neither in the same row or column this will come out false..", is_valid
    if is_in_column == True:
        diff1=(bow_row-stern_row)+1 #We are testing if the coordinates are correct for the length of the ship
        diff2=(stern_row-bow_row)+1 #We check it both directions in case the ship is backwards
        if diff1 != ship_size and diff2 != ship_size:
            is_valid = False
        #print "this would mean that they are in the same column and if true the ship size is good, if false ship size is wrong", is_valid
    if is_in_row == True:
        diff1=(bow_column-stern_column)+1 #We are testing if the coordinates are correct for the length of the ship
        diff2=(stern_column-bow_column)+1
        if diff1 != ship_size and diff2 != ship_size:
            is_valid = False
        #print "this would mean that they are in the same row and if true the ship size is good, if false ship size is wrong", is_valid
    return is_valid

def bigger(a,b): #This is a general low level function that can be used in a lot of different programs
    if a > b:
        return a
    else:
        return b

def get_ship_size(ship_name): # This is a small function that returns the size of the ship based on the name
    if ship_name ==  "aircraft carrier":
        ship_size = 5
    elif ship_name == "battleship":
        ship_size = 4
    elif ship_name == "submarine":
        ship_size = 3
    elif ship_name == "cruiser":
        ship_size = 3
    elif ship_name == "destroyer":
        ship_size = 2
    return ship_size

def get_ship_letter(ship_name): # This is a small function that returns the letter abbreviation for the ship based on the name
    if ship_name ==  "aircraft carrier":
        ship_letter = 'A'
    elif ship_name == "battleship":
        ship_letter = 'B'
    elif ship_name == "submarine":
        ship_letter = 'S'
    elif ship_name == "cruiser":
        ship_letter = 'C'
    elif ship_name == "destroyer":
        ship_letter = 'D'
    return ship_letter


def make_ship(board,stern_row,stern_column,bow_row,bow_column,ship_name):
    is_in_row = False
    is_in_column = False
    no_overlap=True
    ship_size = get_ship_size(ship_name) #Get the ship size
    if stern_row == bow_row: #check if the ship is in a row
        is_in_row = True
    if stern_column == bow_column: #check if the ship is in a column
        is_in_column =True
    if is_in_row == True:
        start_pos=bigger(stern_column,bow_column) #We need to standardize our starting position for simplicity's sake
        for i in range(ship_size):
            if board[stern_row][start_pos]== '0': #We must test if the space is empty
                board[stern_row][start_pos] = get_ship_letter(ship_name)
                start_pos-=1
            else:
                no_overlap=False # if the space wasn't empty then overlap has occurred
    if is_in_column == True:
        start_pos=bigger(stern_row,bow_row)
        for i in range(ship_size):
            if board[start_pos][stern_column]=='0':
                board[start_pos][stern_column] = get_ship_letter(ship_name)
                start_pos-=1
            else:
                no_overlap = False
    return board,no_overlap #if there was overlap then we don't want to update the player board

def place_player_ship(board,board_size,ship_name,ship_size):
    import copy
    while True:
        print_player_board(board,board_size)
        get_ship_text(ship_name,"stern","row")
        player_ship_stern_row = get_row()
        get_ship_text(ship_name,"stern","column")
        player_ship_stern_column = int(raw_input())-1
            
        get_ship_text(ship_name,"bow","row")
        player_ship_bow_row = get_row()
        get_ship_text(ship_name,"bow","column")
        player_ship_bow_column = int(raw_input())-1
            
        if is_valid_placement(player_ship_stern_row,player_ship_stern_column,player_ship_bow_row,player_ship_bow_column,board_size,ship_size) == True:
            temp_board=copy.deepcopy(board) # if the placement is valid we make a copy of the player board, we then go ahead and try to place on the temp board
            temp_board,no_overlap=make_ship(temp_board,player_ship_stern_row,player_ship_stern_column,player_ship_bow_row,player_ship_bow_column,ship_name)
            
            if no_overlap == True: # if there is no overlap on the temp board then we make the ship on the player board.
                make_ship(board,player_ship_stern_row,player_ship_stern_column,player_ship_bow_row,player_ship_bow_column,ship_name)
                return board
            else:
                print "Sorry you've already placed a ship there. Please try again."
        else:
            print "Your placement was invalid. Please try again."
            
def test_direction(direction,ship_size,board,start_row,start_column):
    good_direction = True
    if direction == 'up':
        counter = start_row
        for i in range(ship_size):
            if board[counter][start_column] != '0':
                good_direction = False
                return good_direction
            counter -= 1
        return good_direction
    
    if direction == 'down':
        counter = start_row
        for i in range(ship_size):
            if board[counter][start_column] != '0':
                good_direction = False
                return good_direction
            counter += 1
        return good_direction
    
    if direction == 'left':
        counter = start_column
        for i in range(ship_size):
            if board[start_row][counter] != '0':
                good_direction = False
                return good_direction
            counter -= 1
        return good_direction
    
    if direction == 'right':
        counter = start_column
        for i in range(ship_size):
            if board[start_row][counter] != '0':
                good_direction = False
                return good_direction
            counter += 1
        return good_direction
    
def get_ship_directions(board,board_size,start_row,start_column,ship_size):
    possible_directions = []
    from random import randint
    #test up direction
    if ((start_row+1) - ship_size)>=0:
        up = test_direction('up',ship_size,board,start_row,start_column)
        if up == True:
            possible_directions.append('up')
            #print "shows which values are in possible directions list ",possible_directions
            
    #test down direction
    if ((start_row+1)+ship_size) <= board_size:
        down = test_direction('down',ship_size,board,start_row,start_column)
        if down == True:
            possible_directions.append('down')
            #print "shows which values are in possible directions list ",possible_directions
        
    #test left direction
    if ((start_column+1)-ship_size)>=0:
        left = test_direction('left',ship_size,board,start_row,start_column)
        if left == True:
            possible_directions.append('left')
            #print "shows which values are in possible directions list ",possible_directions
        
    #test right direction
    if ((start_column+1)+ship_size) <= board_size:
        right = test_direction('right',ship_size,board,start_row,start_column)
        if right == True:
            possible_directions.append('right')
            #print "shows which values are in possible directions list ",possible_directions
            
    if possible_directions:
        rand_direction = randint(0,(len(possible_directions))-1)
        chosen_direction = possible_directions[rand_direction]
        #print "The chosen direction is ",chosen_direction
        return chosen_direction
    return None

def make_computer_ship(board,start_row,start_column,direction,ship_name,ship_size):
    if direction == 'up':
        counter = start_row
        for i in range (ship_size):
            board[counter][start_column]=get_ship_letter(ship_name)
            counter -=1
        return board
    if direction == 'down':
        counter = start_row
        for i in range (ship_size):
            board[counter][start_column]=get_ship_letter(ship_name)
            counter +=1
        return board
    if direction == 'left':
        counter = start_column
        for i in range (ship_size):
            board[start_row][counter]=get_ship_letter(ship_name)
            counter -=1
        return board
    if direction == 'right':
        counter = start_column
        for i in range (ship_size):
            board[start_row][counter]=get_ship_letter(ship_name)
            counter +=1
        return board
    
def place_computer_ship(board,board_size,ship_name,ship_size):
    from random import randint
    while True:
        stern_ship_row = randint(0,(board_size-1))
        stern_ship_column = randint(0,(board_size-1))
        #print "the stern_ship_row for the ",ship_name,"is located at ", stern_ship_row
        #print "the stern_ship_column for the ",ship_name,"is located at ", stern_ship_column
        if board[stern_ship_row][stern_ship_column] == '0':
            chosen_direction=get_ship_directions(board,board_size,stern_ship_row,stern_ship_column,ship_size)
            if chosen_direction: ##if this variable has a value then we will place the ship on the board
                make_computer_ship(board,stern_ship_row,stern_ship_column,chosen_direction,ship_name,ship_size)
                return board
            
def player_take_shot(board,shot):
    valid_shots = ['0','A','B','S','C','D']
    while True:
        print "Time to take shot number ", shot, " !!!"
        print "Enter desired row (A-J) for shot number ", shot
        player_shot_row = get_row()
        print "Enter desired column."
        player_shot_column = get_column()
        if board[player_shot_row][player_shot_column] not in valid_shots:
            print "You've already shot in that space!"
        else:
            return player_shot_row,player_shot_column
        
def computer_take_shot(board):
    from random import randint
    valid_shots = ['0','A','B','S','C','D']
    while True:
        computer_shot_row = randint(0,9)
        computer_shot_column = randint(0,9)
        if board[computer_shot_row][computer_shot_column] in valid_shots:
            return computer_shot_row,computer_shot_column
        
def update_board(board,shot_row,shot_column):
    if board[shot_row][shot_column] == '0':
        board[shot_row][shot_column] = 'X'
        return board
    else:
        board[shot_row][shot_column] = 'H'
        return board
    
def sink_ship_text(player_or_computer,ship_name):
    if player_or_computer == "player":
        print "You sunk my ",ship_name,"!!!"
    else:
        print "The Grand Champion of the Depths sank your ",ship_name,"!!!"
    
def check_board(board,turn_counter,player_win,computer_win,keep_playing):
    if turn_counter%2 == 0:
        player_or_computer = 'player'
    else:
        player_or_computer = 'computer'
    
    a = False
    b = False
    s = False
    c = False
    d = False
    
    counter = 0  
    for row in board:
        for e in row:
            if e == 'A':
                counter+=1
    if counter == 0:
        a = True
        sink_ship_text(player_or_computer,'aircraft carrier')
        
    counter = 0  
    for row in board:
        for e in row:
            if e == 'B':
                counter+=1
    if counter == 0:
        b = True
        sink_ship_text(player_or_computer,'battleship')
        
    counter = 0  
    for row in board:
        for e in row:
            if e == 'S':
                counter+=1
    if counter == 0:
        s = True
        sink_ship_text(player_or_computer,'submarine')
        
    counter = 0  
    for row in board:
        for e in row:
            if e == 'C':
                counter+=1
    if counter == 0:
        c = True
        sink_ship_text(player_or_computer,'cruiser')
        
    counter = 0  
    for row in board:
        for e in row:
            if e == 'D':
                counter+=1
    if counter == 0:
        d = True
        sink_ship_text(player_or_computer,'destroyer')
        
    if a and b and s and c and d:
        if player_or_computer == 'computer':
            computer_win = True
            keep_playing = False
        else:
            player_win = True
            keep_playing = False
    
    return player_win,computer_win,keep_playing

def rampage_check(board,board_size):
    spaces_left = 0
    counter1 = 0

    for i in range(board_size):
        row = []
        row = board[counter1]
        for e in row:
            if e == 'A':
                spaces_left += 1
            if e == 'B':
                spaces_left += 1
            if e == 'S':
                spaces_left += 1
            if e == 'C':
                spaces_left += 1
            if e == 'D':
                spaces_left += 1
            if e == '0':
                spaces_left += 1
                
        counter1 += 1
        
    return spaces_left        
                
def battleship():   
    from random import randint
    print"Welcome to Battleship! ... Are you ready to face the GRAND MASTER OF THE SEAS!?"
    print ""
    print 'Type "yes" to continue'
    s=raw_input()
    if s == 'yes':
        print "Let's Begin!!"
        print ""
        
        board_size = 10  
        
        player_board=new_board(board_size)  ###initialize player board
        computer_board=new_board(board_size) ### initialize computer board
        
        player_board=place_player_ship(player_board,board_size,"aircraft carrier",5)
        player_board=place_player_ship(player_board,board_size,"battleship",4)
        player_board=place_player_ship(player_board,board_size,"submarine",3)
        player_board=place_player_ship(player_board,board_size,"cruiser",3)
        player_board=place_player_ship(player_board,board_size,"destroyer",2)
        print ""
        print_player_board(player_board,board_size)
        
        
        print_computer_board(computer_board,board_size)
        place_computer_ship(computer_board,board_size,"aircraft carrier",5)
        place_computer_ship(computer_board,board_size,"battleship",4)
        place_computer_ship(computer_board,board_size,"submarine",3)
        place_computer_ship(computer_board,board_size,"cruiser",3)
        place_computer_ship(computer_board,board_size,"destroyer",2)
        

        print ""
        print "Let's begin!!!"
        
        keep_playing=True ### This boolean controls if we continue to play the game
        shot=1   ### keeps track of the number of shots the player has taken
        turn_counter = 2
        computer_win=False
        player_win=False
        while keep_playing == True:
            print "It time for the fumbling voyager to take turn number ", shot, "..."
            print_computer_board(computer_board,board_size)
            player_shot_row,player_shot_column = player_take_shot(computer_board,shot)
            computer_board=update_board(computer_board,player_shot_row,player_shot_column)
            print_computer_board(computer_board,board_size)
            player_win,computer_win,keep_playing = check_board(computer_board,turn_counter,player_win,computer_win,keep_playing)
            turn_counter+=1
            if keep_playing == False:
                break
            
            print "Time for the master of the seas to take turn number ", shot, " !!!"
            computer_shot_row,computer_shot_column = computer_take_shot(player_board)
            player_board=update_board(player_board,computer_shot_row,computer_shot_column)
            print_player_board(player_board,board_size)
            spaces_left = rampage_check(player_board,board_size)
            if spaces_left > 7:
                if player_board[computer_shot_row][computer_shot_column] == 'H':
                    print "RAMPAGE!!!"
                    for i in range (6):
                        computer_shot_row,computer_shot_column = computer_take_shot(player_board)
                        player_board=update_board(player_board,computer_shot_row,computer_shot_column)
                    
            print_player_board(player_board,board_size)
            player_win,computer_win,keep_playing = check_board(player_board,turn_counter,player_win,computer_win,keep_playing)
            turn_counter+=1
            if keep_playing == False:
                break
            shot+=1
            
        
        if computer_win == True:
            print "PLAYER DEMOLISHED BY THE LE CAPITAN OF THE SEAS!!!"
        
        if player_win == True:
            print "CONGRATULATIONS!!! Thou hast done what no mere mortal can. Thou has slain the MASTER OF THE SEAS. What an historic day this will be. Tell your friends, let it be proclaimed from the highest of heights and from the deepest of depths! Thou hast looked death in the face and won. Think of it....you....A CHAMPION!!!"
                    
    else:
        print "Come back when you're ready for a beating!"  ### This is if they don't say "yes" at the beginning