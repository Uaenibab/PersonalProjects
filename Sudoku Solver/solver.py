'''
This function finds the first instance of a zero in the array, which is an empty space in our sudoku puzzle,
and fills it with each possible number. This could be made a bit smarter by keeping some sort of list of the counts
of each number to avoid clearly false cases from being tested.
'''
def expand(P):
    A = []
    
    for i in range(9):
        for j in range(9):
            if(P[i][j] == 0):
                for num in range(1, 10):
                    copy = [[0 for _ in range(9)] for _ in range(9)]
                    for h in range(9):
                        for k in range(9):
                            copy[h][k] = P[h][k]
                
                    copy[i][j] = num
                    A.append(copy)
                return A
    return A


'''
This function tests to see if the current configuration of the puzzle is valid, i.e are there two of the same number in each
column, row or 3x3 square. If there is more than one of the same number in either three of those conditions, the test returns
false and is thrown out. If that is not the case, but the puzzle is not completely full, it will keep this configuration to
expand it further. If there are no empty spaces, then it is a solution.
'''
def test(P):
    full = True
    
    for num in range(1, 10):
        for blockCol in range(3):
            for blockRow in range(3):

                numRow = None
                numCol = None
                #check square validity
                for i in range(blockRow*3, (blockRow*3)+3):
                    for j in range(blockCol*3, (blockCol*3)+3):
                        if(P[i][j] == num):
                            if(numRow != None):
                                return False
                            numRow = i
                            numCol = j
                        elif(P[i][j] == 0):
                            full = False
                
                if(numRow != None):
                    for i in range(9):
                        if(i != numRow and P[i][numCol] == num):
                            return False
                        elif(i != numCol and P[numRow][i] == num):
                            return False
    
    if(not full):
        return None
    else:
        return True

#backtrack function is from Dr. David Bremner's CS3383 class at UNB
def backtrack(P0):
    s = [P0]
    while(len(s) > 0):
        P = s.pop()
        result = test(P)
        if result == True: #if the puzzle is solved, return it
            return P
        elif result == None: #if the puzzle can still lead to a correct answer, expand it
            for R in expand(P):
                s.append(R)
    return False #if no puzzles lead to an answer, then it is unsolvable


if __name__ == "__main__":
    #The sudoku puzzle is represented as a 2D array, with 0's for blank spaces
    puzzle = [[] for _ in range(9)]

    puzzle[0] = [0,0,3,7,0,6,0,4,0]
    puzzle[1] = [0,0,6,0,0,0,2,0,0]
    puzzle[2] = [4,8,1,0,2,0,0,0,7]
    puzzle[3] = [0,0,2,4,9,0,0,5,3]
    puzzle[4] = [5,6,0,8,0,0,1,7,4]
    puzzle[5] = [0,0,4,5,6,0,0,8,2]
    puzzle[6] = [0,4,0,0,0,0,8,9,1]
    puzzle[7] = [0,0,8,6,4,0,0,3,0]
    puzzle[8] = [3,0,7,0,5,8,4,0,6]

    result = backtrack(puzzle)

    #Prints the puzzle
    if(result != False):
        for i in range(9):
            line = ""
            if(i%3 == 0):
                print("")
            for j in range(9):
                if(j%3 == 0):
                    line += "   "
                line += str(result[i][j]) + " "
            print(line)
    else:
        print("Unsolvable")