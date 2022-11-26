
def newBoard(n: int):
    """
    Une fonction "newBoard(n)" qui retourne une liste à deux dimensions représentant l'état initial d'un plateau de jeu de n cases sur n cases.
    >>> newBoard(1)
    [[0]]
    >>> newBoard(2)
    [[0, 0], [0, 0]]
    >>> newBoard(3)
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    """
    return [[0 for x in range(n)] for x in range(n)]


def otherplayer(player: int):
    """
    return the opponent of the player
    >>> otherplayer(1)
    2
    >>> otherplayer(2)
    1
    """
    return 2 if player == 1 else 1


def intInput(message: str):
    """
    Returns the int value of the input given a message, else asks again until an int is given
    """
    while True:
        try:
            return int(input(message+"\n"))
        except ValueError:
            print("please enter a valid number \n")


def possibleSquare(board: list, n: int, i: int, j: int):
    """
    Une fonction "possibleSquare(board, n, i, j)" qui retourne True si i et j sont les coordonnées d'une case où le joueur courant peut poser un pion, et False sinon.
    >>> possibleSquare(newBoard(5), 5, 1, 4)
    True
    >>> possibleSquare(newBoard(15), 15, 14, 6)
    True
    >>> possibleSquare(newBoard(5), 5, 0, 4)
    True
    >>> possibleSquare(newBoard(15), 15, 14, 16)
    False
    """
    if (i >= 0 and i < n) and (j >= 0 and j < n):
        return True
    return False


def playableSquare(board: list, n: int, i: int, j: int):
    """
    return True if there is not already a piece in this square
    >>> playableSquare([[2, 0, 0], [0, 0, 0], [0, 0, 0]], 3, 2, 2)
    True
    >>> playableSquare([[2, 0, 0], [0, 0, 0], [0, 0, 0]], 3, 0, 0)
    False
    """
    if (possibleSquare(board, n, i, j) and board[i][j] == 0):
        return True
    return False


def selectSquare(board: list, n: int):
    """
    Une fonction "selectSquare(board, n)" qui fait saisir au joueur player les coordonnées d'une case où il peut poser un pion. On supposera qu'il existe une telle case, on ne testera pas ce fait ici. Tant que ces coordonnées ne seront pas valides en regard des règles du jeu(et des dimensions du plateau), on lui demandera de nouveau de les saisir. Finalement, la fonction retournera ces coordonnées.
    """
    selectedRow, selectedColumn = -1, -1
    while not playableSquare(board, n, selectedRow, selectedColumn):
        selectedRow = intInput("select a row inside the board") - 1
        selectedColumn = intInput("select a row inside the board") - 1

    return selectedRow, selectedColumn


def compute_diagonal(board: list, n: int, i: int, j: int, direction: int):
    """
    return True si la diagonale direction (0= \  1= /)  qui comporte la case (i, j) est remplie, dans le cas contraire return False
    >>> compute_diagonal([[1,0,0],[0,1,0],[0,0,1]], 3, 1, 1, 0)
    (True, [1, 1, 1])
    >>> compute_diagonal([[1,0,0],[0,1,0],[0,0,2]], 3, 1, 1, 0)
    (True, [1, 1, 2])
    >>> compute_diagonal([[0,0,0],[0,1,0],[0,0,2]], 3, 1, 1, 0)
    (False, [])
    """
    iteration = 0
    diags = []
    if direction == 0:
        # empeche de compter le coin
        if ((i == 0 and j == n-1) or (i == n-1 and j == 0)):
            return (False, [])

        while i > 0 and j > 0:
            i -= 1
            j -= 1

        # vers bas droite
        while ((i+iteration < n) and (j+iteration < n)):
            if board[i+iteration][j+iteration] == 0:
                return (False, [])
            diags.append(board[i+iteration][j+iteration])

            iteration += 1

    if direction == 1:
        # empeche de compter le coin
        if ((i == 0 and j == 0) or (i == n-1 and j == n-1)):
            return (False, [])

        while (i > 0 and j < n-1):
            i -= 1
            j += 1

        # vers bas gauche
        while ((i+iteration < n) and (j-iteration >= 0)):
            if board[i+iteration][j-iteration] == 0:
                return (False, [])
            diags.append(board[i+iteration][j-iteration])

            iteration += 1
    return (True, diags)


def again(board, n: int):
    """
    Une fonction "again(board, n)" qui retourne True si le joueur courant peut poser un pion sur le plateau et False sinon.
    >>> board = [[1, 2, 1], [1, 2, 1], [1, 2, 1]]
    >>> again(board, 3)
    False
    >>> board = [[1, 2, 1], [1, 0, 1], [1, 2, 1]]
    >>> again(board, 3)
    True
    """
    for row in board:
        for col in row:
            if col == 0:
                return True
    return False


def win(score: list):
    """
    Une fonction "win(score)" qui retourne une chaîne de caractères indiquant l'issue de la partie.
    >>> win((5, 3))
    Player 1 wins 5 - 3
    >>> win((7, 9))
    Player 2 wins 7 - 9
    >>> win((2, 2))
    It's a draw 2 - 2
    """
    if score[0] == score[1]:
        print(f"It's a draw {score[0]} - {score[1]}")
        return
    if score[0] > score[1]:
        print(f"Player 1 wins {score[0]} - {score[1]}")
        return
    print(f"Player 2 wins {score[0]} - {score[1]}")


def updateBoard(board: list, player: int, i: int, j: int):
    """
    Une procédure "updateBoard(board, player, i, j)" où l'on suppose ici que i et j sont les coordonnées d'une case où le joueur player peut poser un pion. Cette procédure réalise cette pose.
    >>> board = newBoard(3)
    >>> updateBoard(board, 1, 2, 2)
    [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
    >>> board = newBoard(3)
    >>> updateBoard(board, 2, 1, 1)
    [[0, 0, 0], [0, 2, 0], [0, 0, 0]]
    """
    if player == 1:
        board[i][j] = 1
        return board
    board[i][j] = 2
    return board


def updateScore(board: list, n: int, player: int, score: list, i: int, j: int):
    """
    # Une procédure "updateScore(board, n, player, score, i, j)" où l'on suppose ici que i et j sont les coordonnées d'une case où le joueur player vient de poser un pion. Cette procédure met à jour le score du joueur player.
    >>> score = [0, 0]
    >>> updateScore([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3, 1, score, 0, 0)
    >>> displayScore(score)
    Current score: 3 vs 0
    >>> score = [0, 0]
    >>> updateScore([[2, 0, 0], [0, 1, 0], [0, 0, 1]], 3, 1, score, 0, 0)
    >>> displayScore(score)
    Current score: 2 vs 0
    >>> score = [0, 0]
    >>> updateScore([[2, 0, 0], [0, 1, 0], [0, 0, 2]], 3, 1, score, 0, 0)
    >>> displayScore(score)
    Current score: 0 vs 0

    """
    diags = [compute_diagonal(board, n, i, j, 0)[1],
             compute_diagonal(board, n, i, j, 1)[1]]

    for direction in range(2):
        if compute_diagonal(board, n, i, j, direction)[0]:
            last = -1

            for index, item in enumerate(diags[direction]):
                if index+1 < len(diags[direction]):
                    if item == diags[direction][index+1] and item == player:
                        score[player-1] += 1
                    elif (index != 0) and (item == last) and (diags[direction][index+1] == otherplayer(player)):
                        score[player-1] += 1

                # to calculate the last one
                if index == len(diags[direction])-1 and item == last and item == player:
                    score[player-1] += 1

                last = item


def displayBoard(board: list, n: int):
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


def displayScore(score: list):
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


def diagonals(n: int):
    """
    Un programme principal "diagonals(n)" qui utilisera les sous-programmes précédents(et d'autres si besoin est) afin de permettre à deux joueurs de disputer une partie complète sur un plateau de jeu de n cases sur n cases.
    """
    player = 1
    board = newBoard(n)
    score = [0, 0]
    displayBoard(board, n)
    displayScore(score)

    while again(board, n):
        selectedRow, selectedColumn = selectSquare(board, n)
        updateBoard(board, player, selectedRow, selectedColumn)
        displayBoard(board, n)
        updateScore(board, n, player, score, selectedRow, selectedColumn)
        displayScore(score)

        player = otherplayer(player)
    win(score)


if __name__ == "__main__":
    import doctest
    # doctest.testmod(verbose=True)
    doctest.testmod(verbose=False)

    diagonals(intInput("Entrez la taille de la grille"))
