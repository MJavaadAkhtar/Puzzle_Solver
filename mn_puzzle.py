from puzzle import Puzzle


class MNPuzzle(Puzzle):
    """
    An nxm puzzle, like the 15-puzzle, which may be solved, unsolved,
    or even unsolvable.
    """

    def __init__(self, from_grid, to_grid):
        """
        MNPuzzle in state from_grid, working towards
        state to_grid

        @param MNPuzzle self: this MNPuzzle
        @param tuple[tuple[str]] from_grid: current configuration
        @param tuple[tuple[str]] to_grid: solution configuration
        @rtype: None
        """
        # represent grid symbols with letters or numerals
        # represent the empty space with a "*"
        assert len(from_grid) > 0
        assert all([len(r) == len(from_grid[0]) for r in from_grid])
        assert all([len(r) == len(to_grid[0]) for r in to_grid])
        self.n, self.m = len(from_grid), len(from_grid[0])
        self.from_grid, self.to_grid = from_grid, to_grid



    def __eq__(self, other):
        for i in range(len(self.from_grid)):
            if self.from_grid[i] != other.from_grid[i]:
                return False
        return True

    def __ne__(self,other):
        return not self.__eq__(other)

    # TODO
    # implement __eq__ and __str__
    # __repr__ is up to you
    def __repr__(self):
        return str(self.from_grid)
    # TODOs
    # override extensions
    # legal extensions are configurations that can be reached by swapping one
    # symbol to the left, right, above, or below "*" with "*"
    def extensions(self):
        c,r =0,0
        for i in range(self.n):
            for j in range(self.m):
                if self.from_grid[i][j] == "*":
                    r,c = i, j
        new_lst_board = []
        if r<self.n - 1:
            new_from_grid = [list(x[:]) for x in self.from_grid]
            new_from_grid[r][c] = new_from_grid[r+1][c]
            new_from_grid[r+1][c] = "*"
            new_from_grid = tuple(tuple(x) for x in new_from_grid)
            new_lst_board.append(MNPuzzle(new_from_grid,self.to_grid))
        # do the reamining three

        if c<self.m-1:
            new_from_grid2 = [list(x[:]) for x in self.from_grid]
            new_from_grid2[r][c] = new_from_grid2[r][c+1]
            new_from_grid2[r][c+1] = "*"
            new_from_grid2 = tuple(tuple(x) for x in new_from_grid2)
            new_lst_board.append(MNPuzzle(new_from_grid2,self.to_grid))

        
        if c >0:
            new_from_grid4 = [list(x[:]) for x in self.from_grid]
            new_from_grid4[r][c] = new_from_grid4[r][c-1]
            new_from_grid4[r][c-1] = "*"
            new_from_grid4 = tuple(tuple(x) for x in new_from_grid4)
            new_lst_board.append(MNPuzzle(new_from_grid4,self.to_grid))


        if  r > 0:
            new_from_grid3 = [list(x[:]) for x in self.from_grid]
            new_from_grid3[r][c] = new_from_grid3[r-1][c]
            new_from_grid3[r-1][c] = "*"
            new_from_grid3 = tuple(tuple(x) for x in new_from_grid3)
            new_lst_board.append(MNPuzzle(new_from_grid3,self.to_grid))

        return new_lst_board
    def is_solved(self):
        return self == MNPuzzle(self.to_grid,self.from_grid)

                                 
                                
                                 
                                 
        
                    
    # TODO
    # override is_solved
    # a configuration is solved when from_grid is the same as to_grid


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    target_grid = (("1", "2", "3"), ("4", "5", "*"))
    start_grid = (("*", "2", "3"), ("1", "4", "5"))
    target_grid = (('1', '2', '3'),('4', '5', '6'),('7', '8', '*'))
    start_grid = (('6', '7', '4'),('2', '3', '8'),('5', '*', '1'))
    # start_grid = (("4", "1", "2"), ("5", "*", "3"))
    # target_grid = (("1", "2", "3"), ("4", "5", "*"))
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    s = MNPuzzle(start_grid, target_grid)
    '''
    print(s.extensions())
    start = time()
    solution = breadth_first_solve(MNPuzzle(start_grid, target_grid))
    
    end = time()
    print("BFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
        '''
    start = time()
    solution = depth_first_solve((MNPuzzle(start_grid, target_grid)))
    end = time()
    print("DFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
