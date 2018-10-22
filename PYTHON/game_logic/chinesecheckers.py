
board_size = 13

max_depth = 100

class Node():
    def __init__(self):
        self.neighbours = []
        self.color = "0" #What shows when I print the board
        self.r=0 #row placement
        self.c=0 #column placement
        self.visited = 0


def newCreateBoardTree():
    #plan: separate the creating of the board, and the connecting, previous solution was way to cluttered

    #stage 1, create the onion, layerslayerslayers

    matrix = []
    global board_size

    if(board_size%2 ==0):
        print("Board size must be odd, fixing the issue")
        board_size += 1

    
    for i in range(0, board_size):
        row = []

        if (i<board_size//2 +1):
            for j in range(0, i+1):
                node = Node()
                node.r = i
                node.c = j
                row.append(node)
            matrix.append(row)
        else:
            lengthOfLastRow = len(matrix[i-1])
            lengthOfThisRow = lengthOfLastRow-1
            for j in range(0, lengthOfThisRow):
                node = Node()
                node.r = i
                node.c = j
                row.append(node)
            matrix.append(row)

    #stage 2, connect the layers and nodes in the same layer
    
    for j in range(0, len(matrix)):
        row = matrix[j]

        if len(row) != 1: #Connect internally on a layer
            for i in range(1, len(row)):
                row[i].neighbours.append(row[i-1])
                row[i-1].neighbours.append(row[i])
        
        if j+1 < len(matrix): # Connect nodes between layers

            nextRow = matrix[j+1]
            

            if (len(row)<len(nextRow)): #When connecting layers in increasing order
                for x in range(0, len(row)):
                    row[x].neighbours.append(nextRow[x])
                    row[x].neighbours.append(nextRow[x+1])
                    nextRow[x].neighbours.append(row[x])
                    nextRow[x+1].neighbours.append(row[x])

            else: #When connecting layers in decreasing order

                for z in range(0, len(nextRow)):
                    nextRow[z].neighbours.append(row[z])
                    nextRow[z].neighbours.append(row[z+1])
                    row[z].neighbours.append(nextRow[z])
                    row[z+1].neighbours.append(nextRow[z])

    return matrix



def printCheckerBoard(matrix, aligned):
    #board_size determines amount of rows
    #TODO: does not print just right for all sizes, some scaling issue 
    half_point = (board_size//2)
    half_size = len(matrix[half_point])
    padding = half_size//2+3
    i=0
    if aligned:
        axis = "    "
        for x in range(0, half_size):
            axis+=str(x)+ " "
        print(axis)

    for row in matrix:
        if not aligned:
            if (i>9):
                 stringprint =str(i)+ "" + " "*(padding)
            else:

                stringprint =str(i)+ " " + " "*(padding)
        else:
            if i>9:
                stringprint = str(i)+" "
            else:

                stringprint=str(i)+"  "

        if (i<half_point):
            padding-=1
        else:
            padding+=1

        #print("Padding is ", padding) 
        i+=1 
        for item in row:
            stringprint += " "+str(item.color)
        print(stringprint)





def placeToken(row,column, matrix, token):
    matrix[row][column].color = token

def removeToken(row, column, matrix):
    saveToken = matrix[row][column].color 
    matrix[row][column].color = "0"
    return saveToken

def moveToken(startRow, startColumn, endRow, endColumn, matrix):
    if (matrix[endRow][ebdColumn] == "0"):
        savedToken = removeToken(startRow, startColumns, matrix)
        placeToken(endRow, endColumn, matrix, savedToken)

def calculateScore(matrix, token, startingRow):






def printNeighbours(node):
    neighbours = []
    for i in node.neighbours:
        neighbours.append((i.r, i.c))
    print(neighbours)


def possibleMovesVisual(row, column, matrix):
    #moves = possibleMoves(row, column, matrix)
    moves = {}
    fullRecursivePossibleMoves(max_depth, row, column, matrix, moves)
    for t in moves.keys():
        placeToken(t[0], t[1], matrix,  "x")


def fullRecursivePossibleMoves(depth, row, column, matrix, moves):
    # This seems to actually work, i dub the the delta rule

    if depth==0:
        return

    node = matrix[row][column]

    node.visited = 1
    
    for n in node.neighbours:
        if n.visited == 1:
            continue

        if n.color == "0" and depth == max_depth:
            n.visited = 1
            moves[(n.r, n.c)] = (n.r, n.c)
        if n.color != "0":
            for item in n.neighbours:
                if item.color == "0":
                    row_delta = abs(item.r-node.r)
                    col_delta = abs(item.c-node.c)
                    #delta rule
                    if (row_delta == 2 or row_delta ==0) and (col_delta ==2 or col_delta ==0):
                        item.visited = 1
                        n.visited = 1
                        moves[(item.r, item.c)] = (item.r, item.c)
                        fullRecursivePossibleMoves(depth-1, item.r, item.c, matrix, moves)

            


    


def run():
    print("Starting print")
    matrix = newCreateBoardTree()

    placeToken(0,0, matrix,"1")
    placeToken(1,1, matrix, "1")
    placeToken(3,2,matrix,"1")
    placeToken(4, 3, matrix, "1")
    placeToken(4,4, matrix, "1")
    placeToken(5, 2, matrix, "1")
    placeToken(7, 2, matrix, "1")
    placeToken(9,1,matrix,"1")
    placeToken(11,0,matrix,"1")

    possibleMovesVisual(0,0,matrix)

    printCheckerBoard(matrix, False)
    print("End print")





if __name__=="__main__":
    run()