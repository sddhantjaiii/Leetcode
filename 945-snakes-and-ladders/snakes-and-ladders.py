class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        END = N**2

        # Given a square number, return the (x,y) coordinate on the board
        def coordToSquare(square):
            x = N - math.ceil(square / N)
            if x % 2 == (N-1) % 2:
                # If last row is same modularity as x, then the rows count up when going from left to right
                firstSquare = (N - x) * N - N + 1 # The first square in row x
                y = square - firstSquare
            else:
                # The rows count down when going from left to right
                firstSquare = (N - x) * N # The first square in row x
                y = firstSquare - square

            return (x, y)        
        
        queue = deque([(0, 1)]) # (rolls, square#)
        seen = [False for _ in range(END+1)]
        while queue:
            rolls, square = queue.popleft()

            if square == END:
                return rolls
            
            # Add adjacent squares
            for diceRoll in range(1,7):
                adjSquare = square + diceRoll
                if adjSquare == END:
                    return rolls + 1
                if seen[adjSquare]:
                    continue
                
                #print("adjSquare: ", adjSquare)
                seen[adjSquare] = True

                # If there is a ladder or snake, take it
                (x, y) = coordToSquare(adjSquare)
                jumpSquare = board[x][y]
                if jumpSquare != -1:
                    adjSquare = jumpSquare
                    if jumpSquare == END:
                        return rolls + 1
                
                queue.append((rolls + 1, adjSquare))

        # There was a cycle and the snakes constantly bring the user back down
        return -1