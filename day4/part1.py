#get input

f = open("day4/input.txt", "r")
input = f.read()
f.close()

#solution

input = input.splitlines()

draws = []
marked = []

for x in input[0].split(","):
    draws.append(int(x))
    marked.append(set())

bingo_boards = []

for i in range((len(input) - 1)//6):
    new_board = dict()
    for j in range(1,6):
        current_row_raw = input[6*i + j + 1]
        current_row_raw = current_row_raw.split()
        for k in range(len(current_row_raw)):
            new_board[int(current_row_raw[k])] = (k, j-1)
    bingo_boards.append(new_board)

def detect_bingo(marked):
    #rows
    for j in range(0,5):
        flagRow = True
        for i in range(0,5):
            if((i,j) not in marked):
                flagRow = False
        if(flagRow):
            return True
    
    #columns
    for i in range(0,5):
        flagCol = True
        for j in range(0,5):
            if((i,j) not in marked):
                flagCol = False
        if(flagCol):
            return True
    
    return False

winning_num = 0
unmarked = []



def get_answer():
    won = dict()
    wins = 0
    for n in draws:
        for i in range(len(bingo_boards)):
            try:
                marked[i].add(bingo_boards[i][n])
                bingo_boards[i].pop(n, None)
            except:
                pass
            #print(detect_bingo(bingo_boards[i]))
            if(detect_bingo(marked[i])):
                if (i not in won.keys()):
                    won[i] = (wins, n, sum(bingo_boards[i].keys()))
                    wins += 1
    for i in range(len(bingo_boards)):
        if (won[i][0] == len(bingo_boards) - 1):
            return won[i][1]*won[i][2]
        

print(get_answer())


        
