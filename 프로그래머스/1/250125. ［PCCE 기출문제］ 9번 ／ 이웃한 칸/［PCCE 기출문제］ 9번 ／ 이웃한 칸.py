def solution(board, h, w):
    dh = [0,0,1,-1]
    dw = [1,-1,0,0]
    x = len(board)
    y = len(board[0])
    answer = 0
    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]
        if 0<=nh< x and 0<= nw < y and board[nh][nw] == board[h][w]:
            answer+=1

    return answer