import time

def write_text(text, filename):
    '''
    write the text into a file

    Input:
        text -> string
        filename -> name of the file we want to write

    Output:
        None
    '''

    # Open a file
    # file open modes: w -> write, r -> read, a -> append
    with open(filename, 'w') as f:
            f.write(text + "\n")

write_text("hello world", "hello.txt")



def ask_player_move(symbol):
    '''
    Input:
        move -> integer between o and 8
    Output:
        True if move success False if move is invalid
    '''

    move_data = {}
    # time.time() -> current time in seconds
    move_start_time = time.time()
    move = input("Please enter a valid move between 0 - 8: ")
    move_done_time = time.time()

    move_data['symbol'] = symbol
    move_data['move'] = move
    move_data['duration_seconds'] = move_done_time - move_start_time

    print(move_data)
