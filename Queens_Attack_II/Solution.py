board_cols = 10
board_rows = 10

queen_loc = {'row': 4, 'col': 4}


#def get_path(start, end):
#
#    squares = []
#
#    if start[0] != end[0]:
#        # moving alone the row
#        y_loc = start[1]
#
#        if start[0] < end[0]:
#            run_range = range(start[0] + 1, end[0] + 1)
#        else:
#            run_range = reversed(range(end[0], start[0]))
#
#        for spot in run_range:
#            # also moving alone the column
#            if start[1] < end[1]:
#                y_loc += 1
#            elif end[1] < start[1]:
#                y_loc -= 1
#            else:
#                y_loc = start[1]
#
#            squares.append((spot, y_loc))
#    else:
#        # moving alone the column only
#        if start[1] > end[1]:
#            run_range = reversed(range(end[1] + 1, start[1] + 1))
#        else:
#            run_range = range(start[1] + 1, end[1] + 1)
#
#        for spot in run_range:
#            squares.append((start[0], spot))
#    return squares
#
#print get_path((5, 2), (5, 9))
#print get_path((5, 2), (8, 5))
#print get_path((8, 8), (1, 1))
#print get_path((4, 4), (1, 7))
#print get_path((4, 4), (1, 7))
#print get_path((4, 4), (9, 4))

def get_path(start, end):

    squares = []

    if start[0] != end[0]:
        # moving alone the row
        y_loc = start[1]

        if start[0] < end[0]:
            run_range = range(start[0] + 1, end[0] + 1)
        else:
            run_range = reversed(range(end[0], start[0]))

        for spot in run_range:
            # also moving alone the column
            if start[1] < end[1]:
                y_loc += 1
            elif end[1] < start[1]:
                y_loc -= 1
            else:
                y_loc = start[1]

            squares.append((spot, y_loc))
    else:
        # moving alone the column only
        if start[1] > end[1]:
            run_range = reversed(range(end[1] + 1, start[1] + 1))
        else:
            run_range = range(start[1] + 1, end[1] + 1)

        for spot in run_range:
            squares.append((start[0], spot))
    return squares

print get_path((5, 2), (5, 9))
print get_path((5, 2), (8, 5))
print get_path((8, 8), (1, 1))
print get_path((4, 4), (1, 7))
print get_path((4, 4), (1, 7))
