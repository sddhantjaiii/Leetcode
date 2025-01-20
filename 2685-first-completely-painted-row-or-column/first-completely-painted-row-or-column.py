class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        r, c = len(mat), len(mat[0])
        row_count = [0] * r  # Tracks the number of "visited" elements in each row
        col_count = [0] * c  # Tracks the number of "visited" elements in each column
        value_to_position = {}  # Maps value to its position (row, col) in the matrix

        # Precompute the mapping of values to their positions
        for i in range(r):
            for j in range(c):
                value_to_position[mat[i][j]] = (i, j)

        # Process each value in the array
        for i, value in enumerate(arr):
            rr, cc = value_to_position[value]
            row_count[rr] += 1
            col_count[cc] += 1

            # Check if the row or column is complete
            if row_count[rr] == c or col_count[cc] == r:
                return i

        return -1  # This should never be reached if input guarantees a solution
