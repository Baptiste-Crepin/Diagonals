
def newBoard(n):
    """
    Une fonction "newBoard(n)" qui retourne une liste à deux dimensions représentant l'état initial d'un plateau de jeu de n cases sur n cases.
    >>> newBoard(5)
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    >>> newBoard(3)
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    """
    return [[0 for x in range(n)] for x in range(n)]


def displayBoard(board, n):
    """
    Une procédure "displayBoard(board, n)" qui réalise l'affichage du plateau sur la console. On représentera une case vide par un ".", un pion blanc par un "x" et un pion noir par un "o". On numérotera les lignes et les colonnes(à partir de 1) pour que les joueurs puissent repérer facilement les coordonnées d'une case.
    >>> displayBoard(newBoard(5), 5)
    1 | . . . . .
    2 | . . . . .
    3 | . . . . .
    4 | . . . . .
    5 | . . . . .
      ------------
        1 2 3 4 5
    >>> displayBoard([[2, 0, 0], [0, 0, 0], [0, 0, 0]], 3)
    1 | X . .
    2 | . . .
    3 | . . .
      -------
        1 2 3
    """
    for i_row, row in enumerate(board):
        displayableRow = []
        for i_col, col in enumerate(row):
            if board[i_row][i_col] == 0:
                displayableRow.append(".")
            if board[i_row][i_col] == 1:
                displayableRow.append("O")
            if board[i_row][i_col] == 2:
                displayableRow.append("X")
        print(f'{i_row+1} | {" ".join(map(str, displayableRow))}')
    print(f'  {"-"*int(n*2.5)}')
    print(
        f'    {" ".join(map(str, [x[0]+1 for x in enumerate(board)]))}')


def displayScore(score):
    """
    Une procédure "displayScore(score)" qui réalise l'affichage du score sur la console.
    >>> displayScore((5, 3))
    Current score: 5 vs 3
    >>> displayScore((7, 9))
    Current score: 7 vs 9
    >>> displayScore((15, 32))
    Current score: 15 vs 32
    """
    print(f'Current score: {score[0]} vs {score[1]}')


def possibleSquare(board, n, i, j):
    """
    Une fonction "possibleSquare(board, n, i, j)" qui retourne True si i et j sont les coordonnées d'une case où le joueur courant peut poser un pion, et False sinon.
    >>> possibleSquare(newBoard(5), 5, 1, 4)
    True
    >>> possibleSquare(newBoard(15), 15, 14, 6)
    True
    >>> possibleSquare(newBoard(5), 5, 0, 4)
    True
    >>> possibleSquare(newBoard(15), 15, 14, 16)
    Invalid input
    False
    """
    if (i >= 0 and i < n) and (j >= 0 and j < n):
        return True
    return False


def playableSquare(board, n, i, j):
    if (possibleSquare(board, n, i, j) and board[i][j] == 0):
        return True
    return False


def selectSquare(board, n):
    """
    Une fonction "selectSquare(board, n)" qui fait saisir au joueur player les coordonnées d'une case où il peut poser un pion. On supposera qu'il existe une telle case, on ne testera pas ce fait ici. Tant que ces coordonnées ne seront pas valides en regard des règles du jeu(et des dimensions du plateau), on lui demandera de nouveau de les saisir. Finalement, la fonction retournera ces coordonnées.
    """
    selectedRow, selectedColumn = -1, -1
    while not playableSquare(board, n, selectedRow, selectedColumn):
        selectedRow = int(input("select a row inside the board")) - 1
        selectedColumn = int(input("select a column inside the board")) - 1

    return selectedRow, selectedColumn


def updateBoard(board, player, i, j):
    """
    Une procédure "updateBoard(board, player, i, j)" où l'on suppose ici que i et j sont les coordonnées d'une case où le joueur player peut poser un pion. Cette procédure réalise cette pose.
    >>> board = newBoard(5)
    >>> updateBoard(board, 1, 2, 3)
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    >>> board = newBoard(3)
    >>> updateBoard(board, 2, 1, 1)
    [[0, 0, 0], [0, 2, 0], [0, 0, 0]]
    """
    if player == 1:
        board[i][j] = 1
        return board
    board[i][j] = 2
    return board


def full_diag(board, i, j, direction):
    """
    return True si la diagonale direction (0= \  1= /)  qui comporte la case (i, j) est remplie, dans le cas contraire return False
    """
    # empeche de compter le coin
    if ((i == 0 and i == n-1) or (j == 0 and j == n-1)):
        return False

    last_i, last_j, iteration = i, j, 0
    if direction == 0:
        if ((i == 0 and j == n-1) or (i == n-1 and j == 0)):
            return False

        #print("bas droite")
        while ((i+iteration < n) and (j+iteration < n)):
            if board[i+iteration][j+iteration] == 0:
                return False
            last_i, last_j = i-iteration, j-iteration
            iteration += 1

        #print("haut gauche")
        last_i, last_j, iteration = i, j, -1

        while ((i+iteration >= 0) and (j+iteration >= 0)):
            if board[i+iteration][j+iteration] == 0:
                return False
            last_i, last_j = i-iteration, j-iteration
            iteration -= 1

        return True

    if direction == 1:
        # empeche de compter le coin
        if ((i == 0 and j == 0) or (i == n-1 and j == n-1)):
            return False

        #print("bas gauche")
        while ((i-iteration >= 0) and (j+iteration < n)):
            if board[i-iteration][j+iteration] == 0:
                return False
            last_i, last_j = i-iteration, j-iteration
            iteration += 1

        #print("haut droite")
        last_i, last_j, iteration = i, j, 0

        while ((i+iteration < n) and (j-iteration >= 0)):
            if board[i+iteration][j-iteration] == 0:
                return False
            last_i, last_j = i-iteration, j-iteration
            iteration += 1

        return True


def updateScore(board, n, player, score, i, j):
    """
    # Une procédure "updateScore(board, n, player, score, i, j)" où l'on suppose ici que i et j sont les coordonnées d'une case où le joueur player vient de poser un pion. Cette procédure met à jour le score du joueur player.
    """
    b = 1
    print(full_diag(board, i, j, 0))
    print(full_diag(board, i, j, 1))
    if full_diag(board, i, j, 0):
        print("A")
        # bas droite
        while (possibleSquare(board, n, i+b, j+b) and (board[i+b][j+b] == player)):
            if ((i == 0 and j == 0) or ((i+1)+b == n and (j+1)+b == n)):
                break

            print("bas droite")
            if b == 1:
                score[player-1] += 2
            else:
                score[player-1] += 1
            b += 1
        b = 1

        # haut gauche
        while (possibleSquare(board, n, i-b, j-b) and (board[i-b][j-b] == player)):

            if ((i == n and j == n) or (i-b == 0 and j-b == 0)):
                break

            print("haut gauche")
            if b == 1:
                score[player-1] += 2
            else:
                score[player-1] += 1
            b += 1

    if full_diag(board, i, j, 1):
        print('B')
        # bas gauche
        while (possibleSquare(board, n,  i+b, j-b) and (board[i+b][j-b] == player)):
            if (((j+1) == n and i == 0) or (j-b == 0 and (i+1)+b == n)):
                break

            print("bas gauche")
            if b == 1:
                score[player-1] += 2
            else:
                score[player-1] += 1
            b += 1
        b = 1

        # haut droite
        while (possibleSquare(board, n, i-b, j+b) and (board[i-b][j+b] == player)):
            if (i+1 == n and j == 0) or ((i-b == 0 and (j+1)+b == n)):
                break

            print("haut droite")
            if b == 1:
                score[player-1] += 2
            else:
                score[player-1] += 1
            b += 1


def again(board, n):
    """
    Une fonction "again(board, n)" qui retourne True si le joueur courant peut poser un pion sur le plateau et False sinon.
    >> > board = [[1, 2, 1], [1, 2, 1], [1, 2, 1]]
    >> > again(board, 3)
    False
    >> > board = [[1, 2, 1], [1, 0, 1], [1, 2, 1]]
    >> > again(board, 3)
    True
    """
    for row in board:
        for col in row:
            if col == 0:
                return True
    return False


def win(score):
    """
    Une fonction "win(score)" qui retourne une chaîne de caractères indiquant l'issue de la partie.
    >> > win((5, 3))
    Player 1 wins
    >> > win((7, 9))
    Player 2 wins
    >> > win((15, 32))
    Player 2 wins
    """
    if score[0] > score[1]:
        print("Player 1 wins")
        return
    print("Player 2 wins")


def diagonals(n):
    """
    Un programme principal "diagonals(n)" qui utilisera les sous-programmes précédents(et d'autres si besoin est) afin de permettre à deux joueurs de disputer une partie complète sur un plateau de jeu de n cases sur n cases.
    """
    # TODO diagonals
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    doctest.testmod(verbose=False)
    board = newBoard(5)
    n = len(board)
    score = [0, 0]
    displayBoard(board, n)
    displayScore(score)

    for i in range(15):
        selectedRow, selectedColumn = selectSquare(board, n)
        updateBoard(board, 1, selectedRow, selectedColumn)
        displayBoard(board, n)
        updateScore(board, n, 1, score, selectedRow, selectedColumn)
        displayScore(score)
        print("|", full_diag(board, selectedRow, selectedColumn, 0))
        print("/", full_diag(board, selectedRow, selectedColumn, 1))
