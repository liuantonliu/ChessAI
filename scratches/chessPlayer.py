from chessPlayer_tree import *
import random

def genBoard():
    r = [0]*64
    r[0] = 13
    r[1] = 11
    r[2] = 12
    r[3] = 15
    r[4] = 14
    r[5] = 12
    r[6] = 11
    r[7] = 13
    for i in range(8,16):
        r[i]=10
    for i in range(48,56):
        r[i]=20
    r[56] = 23
    r[57] = 21
    r[58] = 22
    r[59] = 25
    r[60] = 24
    r[61] = 22
    r[62] = 21
    r[63] = 23
    return r

def printBoard(r):
   out = []
   for row in range(0,8):
      for col in range(0,8):
         if row%2 == 0 and col%2 == 0:
            out = out + ['_']
         elif row%2 == 0 and col%2 == 1:
            out = out + ['#']
         elif row%2 == 1 and col%2 == 0:
            out = out + ['#']
         elif row%2 == 1 and col%2 == 1:
            out = out + ['_']

   for i in range(0,64):
      if r[i] == 10:
          out[i] = 'p'
      elif r[i] == 11:
          out[i] = 'n'
      elif r[i] == 12:
          out[i] = 'b'
      elif r[i] == 13:
          out[i] = 'r'
      elif r[i] == 14:
          out[i] = 'q'
      elif r[i] == 15:
          out[i] = 'k'
      elif r[i] == 20:
          out[i] = 'P'
      elif r[i] == 21:
          out[i] = 'N'
      elif r[i] == 22:
          out[i] = 'B'
      elif r[i] == 23:
          out[i] = 'R'
      elif r[i] == 24:
          out[i] = 'Q'
      elif r[i] == 25:
          out[i] = 'K'

   i = 8
   while i >= 1:
      for j in range(1,9):
         print(out[i*8-j], end = " ")
      print("       ", end = " ")
      for k in range(1,9):
          if(i*8 -k)>9:
              print((i*8-k),end = " ")
          else:
              print(str(i*8-k)+" ",end = " ")
      print("")
      i=i-1

def GetPlayerPosition(r, player):
    out = []
    if player != 10:
        if player != 20:
            return ["fuck you"]
    for i in range(0,64):
        if player <= r[i] and player + 10 > r[i]:
            out = out + [i]
    return out

def GetPiecesLegalMoves(r, pos):
   if OnBoard(pos) == False:
       return -1
   id = r[pos]%10
   if id == 0:
       return GetP(r,pos)
   elif id == 1:
       return GetN(r,pos)
   elif id == 2:
       return GetB(r,pos)
   elif id == 3:
       return GetR(r,pos)
   elif id == 4:
       return GetB(r,pos)+GetR(r,pos)
   elif id == 5:
       return GetK(r,pos)
   else:
       return -1

def GetP(r,pos):
    out = []
    mycol = GetCol(r,pos)
    if mycol == 10 and OnBoard(pos+9):
        if r[pos+8] == 0:
            out += [pos+8]
        if GetCol(r,pos+7) != mycol and r[pos+7] != 0:
            if (pos%8)!=0:
               out += [pos+7]
        if GetCol(r,pos+9) != mycol and r[pos+9] != 0:
            if (pos%8)!=7:
               out += [pos+9]
    if mycol == 20 and OnBoard(pos-9):
        if r[pos - 8] == 0:
            out += [pos - 8]
        if GetCol(r,pos-7) != mycol and r[pos - 7] != 0:
            if (pos%8) != 7:
                out += [pos - 7]
        if GetCol(r,pos-9) != mycol and r[pos - 9] != 0:
            if (pos%8) != 0:
                out += [pos - 9]
    return out
def GetN(r,pos):
    out = []
    mycol = GetCol(r,pos)
    if pos%8==0:
        posloc = [pos-15,pos-6,pos+10,pos+17]
    elif pos%8==1:
        posloc = [pos-17,pos-15,pos-6,pos+10,pos+15,pos+17]
    elif pos%8==6:
        posloc = [pos-17,pos-15,pos-10,pos+6,pos+15,pos+17]
    elif pos%8==7:
        posloc = [pos-17,pos-10,pos+6,pos+15]
    else:
        posloc = [pos-17,pos-15,pos-10,pos-6,pos+6,pos+10,pos+15,pos+17]
    for i in posloc:
        if OnBoard(i):
           if GetCol(r,i) != mycol:
              out += [i]
    return out
def GetB(r,pos):
    out = []
    mycol = GetCol(r,pos)
    temppos = pos
    while (temppos)%8 <= 6 and OnBoard(temppos+9):
        if GetCol(r,temppos+9)!= mycol:
            temppos+=9
            out += [temppos]
        elif GetCol(r,temppos+9) == mycol:
            break
        if GetCol(r,temppos) != 0:
            break
    temppos = pos
    while (temppos)%8 <= 6 and OnBoard(temppos-7):
        if GetCol(r,temppos-7)!= mycol:
            temppos-=7
            out += [temppos]
        elif GetCol(r,temppos-7) == mycol:
            break
        if GetCol(r,temppos) != 0:
            break
    temppos = pos
    while (temppos)%8 >= 1 and OnBoard(temppos+7):
        if GetCol(r, temppos+7) != mycol:
            temppos += 7
            out += [temppos]
        elif GetCol(r, temppos+7) == mycol:
            break
        if GetCol(r, temppos) != 0:
            break
    temppos = pos
    while (temppos) % 8 >= 1 and OnBoard(temppos-9):
        if GetCol(r, temppos-9) != mycol:
            temppos -= 9
            out += [temppos]
        elif GetCol(r, temppos-9) == mycol:
            break
        if GetCol(r, temppos) != 0:
            break
    return out
def GetR(r,pos):
    out = []
    mycol = GetCol(r,pos)
    temppos = pos
    while temppos%8 <=6 and GetCol(r,temppos+1)!= mycol:
        temppos+=1
        out += [temppos]
        if GetCol(r,temppos) != 0:
            break
    temppos = pos
    while temppos%8 >=1 and GetCol(r,temppos-1)!= mycol:
        #print(temppos)
        temppos-=1
        out += [temppos]
        if GetCol(r,temppos) != 0:
            break
    temppos = pos
    while OnBoard(temppos) and OnBoard(temppos+8):
        if GetCol(r,temppos+8)!= mycol:
            temppos += 8
            out += [temppos]
            if GetCol(r, temppos) != 0:
                break
        else:
            break
    temppos = pos
    while OnBoard(temppos) and OnBoard(temppos-8):
        if GetCol(r,temppos-8) != mycol:
            temppos -= 8
            out += [temppos]
            if GetCol(r, temppos) != 0:
                break
        else:
            break
    return out
def GetK(r,pos):
    out = []
    mycol = GetCol(r,pos)
    if pos%8 == 0:
        posloc = [pos-8,pos-7,pos+1,pos+8,pos+9]
    elif pos%8 == 7:
        posloc = [pos-9,pos-8,pos-1,pos+7,pos+8]
    else:
        posloc = [pos-9,pos-8,pos-7,pos-1,pos+1,pos+7,pos+8,pos+9]
    for i in posloc:
        if OnBoard(i):
           if GetCol(r,i) != mycol:
              out += [i]
    return out

def OnBoard(pos):
    if (pos >= 0) and (pos <= 63):
        return True
    else:
        return False

def GetCol(r,pos):
    return r[pos]-r[pos]%10

def IsPositionUnderThreat(r,pos,player):
    pieces = GetPlayerPosition(r,player)
    boo = False
    for piece in pieces:
        moves = GetPiecesLegalMoves(r,piece)
        for move in moves:
            if move == pos:
                boo = True
    return boo

def GetAllMoves(r,player):
    out = []
    pieces = GetPlayerPosition(r,player)
    for piece in pieces:
        out += GetPiecesLegalMoves(r,piece)
    return out

def candidateMove(r,player):
    out = []
    poss = GetPlayerPosition(r, player)
    for pos in poss:
       for singleMove in GetPiecesLegalMoves(r,pos):
           out += [[[pos,singleMove],valBoard(r,[pos,singleMove])/2000]]
    return out

def valBoard(r, move):
    rf = []
    for i in r:
        rf += [i]
    rf[move[1]] = rf[move[0]]
    rf[move[0]] = 0
    tot = 0
    for i in range(0,64,1):
        if rf[i] == 10:
            tot += 10
        elif rf[i] == 11:
            tot += 30
        elif rf[i] == 12:
            tot += 30
        elif rf[i] == 13:
            tot += 50
        elif rf[i] == 14:
            tot += 90
        elif rf[i] == 15:
            tot += 900
        elif rf[i] == 20:
            tot -= 10
        elif rf[i] == 21:
            tot -= 30
        elif rf[i] == 22:
            tot -= 30
        elif rf[i] == 23:
            tot -= 50
        elif rf[i] == 24:
            tot -= 90
        elif rf[i] == 25:
            tot -= 900
        else:
            tot += 0
    return tot

def valTreeBoard(rf):
    tot = 0
    for i in range(0,64,1):
        if rf[i] == 10:
            tot += 10
        elif rf[i] == 11:
            tot += 30
        elif rf[i] == 12:
            tot += 30
        elif rf[i] == 13:
            tot += 50
        elif rf[i] == 14:
            tot += 90
        elif rf[i] == 15:
            tot += 900
        elif rf[i] == 20:
            tot -= 10
        elif rf[i] == 21:
            tot -= 30
        elif rf[i] == 22:
            tot -= 30
        elif rf[i] == 23:
            tot -= 50
        elif rf[i] == 24:
            tot -= 90
        elif rf[i] == 25:
            tot -= 900
        else:
            tot += 0
    return tot

def decideMove(r,player):
    selectmoves = candidateMove(r,player)
    minimum = 1
    maximum = -1
    selectmove = []
    if player == 20:
        for i in selectmoves:
            if i[1] < minimum:
                minimum = i[1]
        for i in selectmoves:
            if i[1] == minimum:
                selectmove += [i[0]]
    elif player == 10:
        for i in selectmoves:
            if i[1] > maximum:
                maximum = i[1]
        for i in selectmoves:
            if i[1] == maximum:
                selectmove += [i[0]]
    print("selectmove",selectmove)
    if selectmove == []:
        return []
    elif len(selectmove[0])>1:
        o = selectmove[random.randint(0,len(selectmove)-1)]
        print("o",o)
        return o
    else:
        print("s",selectmove)
        return selectmove

def evalTreeMove(r,player):
    out = []
    poss = GetPlayerPosition(r, player)
    for pos in poss:
        for singleMove in GetPiecesLegalMoves(r, pos):
            out += [[pos, singleMove]]
    return out

def evalTree(r,player):
    x = tree(r)
    #y = tree(0)
    oppo = getOppo(player)
    for move1 in evalTreeMove(r,oppo):
        pseudor1 = []
        for i in r:
            pseudor1 += [i]
        pseudor1[move1[1]] = pseudor1[move1[0]]
        pseudor1[move1[0]] = 0
        pr1 = tree(pseudor1)
        #y1 = tree(0)
        for move2 in evalTreeMove(pseudor1,player):
            pseudor2 = []
            for i in pseudor1:
                pseudor2 += [i]
            pseudor2[move2[1]] = pseudor2[move2[0]]
            pseudor2[move2[0]] = 0
            pr2 = tree(pseudor2)
            #y2 = tree(0)
            #printBoard(pr2.store[0])
            # for move3 in evalTreeMove(pseudor2, oppo):
            #     pseudor3 = []
            #     for i in pseudor2:
            #         pseudor3 += [i]
            #     pseudor3[move3[1]] = pseudor3[move2[0]]
            #     pseudor3[move3[0]] = 0
            #     pr3 = tree(pseudor3)
            #     #y3 = tree(0)
            #     for move4 in evalTreeMove(pseudor3, player):
            #         pseudor4 = []
            #         for i in pseudor3:
            #             pseudor4 += [i]
            #         pseudor4[move4[1]] = pseudor4[move2[0]]
            #         pseudor4[move2[0]] = 0
            #         pr4 = tree(pseudor4)
            #         #y4 = tree(valTreeBoard(pseudor4))
            #         #printBoard(pr4.store[0])
            #         pr3.AddSuccessor(pr4)
            #         #y3.AddSuccessor(y4)
            #     pr2.AddSuccessor(pr3)
            #     #y2.AddSuccessor(y3)
            pr1.AddSuccessor(pr2)
            #y1.AddSuccessor(y2)
        x.AddSuccessor(pr1)
        #y.AddSuccessor(y1)
    return x

def getOppo(player):
    if player == 10:
        return 20
    elif player == 20:
        return 10

def chessPlayer(r,player):
    status = [True]
    move = decideMove(r,player)
    candidateMoves = candidateMove(r,player)
    evalTreeOut= evalTree(r,player).Get_LevelOrder()
    if move == []:
        status = False
    return [status] + [move] + [candidateMoves] + [evalTreeOut]

board = genBoard()
done = False
b = False
bb = False
while done == False:

    printBoard(board)
    # while True:
    #     b = False
    #     prepos = int(input("white from? "))
    #     if OnBoard(prepos) == False:
    #         print("end")
    #         bb = True
    #         break
    #     if GetCol(board,prepos) == 10:
    #         moves = GetPiecesLegalMoves(board, prepos)
    #         print(moves)
    #         postpos = int(input("white to? "))
    #         for move in moves:
    #             if move == postpos:
    #                 board[postpos] = board[prepos]
    #                 board[prepos] = 0
    #                 print(candidateMove(board,10))
    #                 #print((evalTree(board,10)).Get_LevelOrder())
    #                 b = True
    #                 break
    #             else:
    #                 continue
    #         if b == False:
    #             print("invalid move")
    #     elif GetCol(board,prepos) != 10:
    #         print("illegal colour")
    #     if b == True:
    #         break
    # if bb == True:
    #     break

    finald = chessPlayer(board,10)
    if finald[0] == False:
        print("error")
        break
    board[finald[1][1]] = board[finald[1][0]]
    board[finald[1][0]] = 0
    printBoard(board)
    finald = chessPlayer(board, 20)
    if finald[0] == False:
        print("error")
        break
    board[finald[1][1]] = board[finald[1][0]]
    board[finald[1][0]] = 0
    # while True:
    #     b = False
    #     prepos = int(input("black from? "))
    #     if OnBoard(prepos) == False: #check if prepos value is on board
    #         print("end")
    #         bb = True
    #         break
    #     if GetCol(board,prepos) == 20: #check if the colour is right
    #         moves = GetPiecesLegalMoves(board, prepos)
    #         print(moves)
    #         postpos = int(input("black to? "))
    #         for move in moves: #moving pieces
    #             if move == postpos:
    #                 board[postpos] = board[prepos]
    #                 board[prepos] = 0
    #                 print(candidateMove(board,20))
    #                 b = True #success, double break
    #                 break
    #             else:
    #                 continue
    #         if b == False:
    #             print("invalid move")
    #     elif GetCol(board,prepos) != 20: #wrong color
    #         print("illegal colour")
    #     if b == True: #success
    #         break
    # if bb == True: #end game
    #     break

