def AttackStoped(KingOfX, KingOfY, QueenOfX, QueenOfY, PosX, PosY):
    X = PosX - KingOfX ; Y = PosY - KingOfY
    TempX = QueenOfX - KingOfX; TempY = QueenOfY - KingOfY
    Diagonal = X * TempY - Y * TempX 
    if Diagonal != 0: return False
    if abs(TempX) >= abs(TempY):
        if TempX > 0:
            if KingOfX < PosX < QueenOfX: return True
            else: return False        
        else:
            if QueenOfX < PosX < KingOfX: return True  
            else: return False      
    else:
        if TempY > 0:
            if KingOfY < PosY < QueenOfY: return True 
            else: return False    
        else:
            if QueenOfY < PosY < KingOfY: return True 
            else: return False         
    return False
def AnswerShowKar(MYChess):
    print(len(MYChess))
    
    return None
def CheckPossible(KingOfX, KingOfY, PosX, PosY, MYChess):
    for queen in MYChess:
        QueenOfX, QueenOfY = queen
        if QueenOfX == KingOfX and QueenOfY == KingOfY: continue
        if QueenOfX == PosX and QueenOfY == PosY: continue
        if AttackStoped(KingOfX, KingOfY, QueenOfX, QueenOfY, PosX, PosY): continue
        if KingOfX == QueenOfX: return True 
        if KingOfY == QueenOfY: return True
        if abs(KingOfX - QueenOfX) == abs(KingOfY - QueenOfY): return True
    return False
def ReallyValid(x1, y1, x2, y2, MYChess):
    for i in range(max(x1 - 1, 0), min(x1 + 1, 7) + 1):
        for j in range(max(y1 - 1, 0), min(y1 + 1, 7) + 1):
            if i == x2 and j == y2: continue             
            if not CheckPossible(i, j, x2, y2, MYChess): return False               
            if not CheckPossible(x2, y2, i, j, MYChess): return False
    for i in range(max(x2 - 1, 0), min(x2 + 1, 7) + 1):
        for j in range(max(y2 - 1, 0), min(y2 + 1, 7) + 1):
            if i == x1 and j == y1: continue
            if not CheckPossible(i, j, x1, y1, MYChess): return False
            if not CheckPossible(x1, y1, i, j, MYChess): return False   
    return True
#--------------------------------------------------------------------------------
def FindNext(x1, y1, x2, y2, MYChess, size):
    if len(MYChess) == size:
        return ReallyValid(x1, y1, x2, y2, MYChess)
    for i in range(8):
        for j in range(8):
            if (i == x1 and j == y1) or (i == x2 and j == y2): continue
            SetOfGitiya = i, j
            if SetOfGitiya not in MYChess:
                MYChess.append(SetOfGitiya)
                if FindNext(x1, y1, x2, y2, MYChess, size) is True: return True
                MYChess.pop()
    return False
#---------------------------------------------------------------------------------
def CheckDede(x1, y1, x2, y2):
    MYChess = []
    if not FindNext(x1, y1, x2, y2, MYChess, 2):
        FindNext(x1, y1, x2, y2, MYChess, 3)
    AnswerShowKar(MYChess)
#---------------------------------------------------------------------------------
n = int(input())
for i in range(n):
    x1,y1,x2,y2 = list(map(int,input().split()))
    CheckDede(x1, y1, x2, y2)
