from puzzle import Puzzle
import copy


class GridPegSolitairePuzzle(Puzzle):
    """
    Snapshot of peg solitaire on a rectangular grid. May be solved,
    unsolved, or even unsolvable.
    """

    def __init__(self, marker, marker_set):
        """
        Create a new GridPegSolitairePuzzle self with
        marker indicating pegs, spaces, and unused
        and marker_set indicating allowed markers.

        @type marker: list[list[str]]
        @type marker_set: set[str]
                          "#" for unused, "*" for peg, "." for empty
        """
        assert isinstance(marker, list)
        assert len(marker) > 0
        assert all([len(x) == len(marker[0]) for x in marker[1:]])
        assert all([all(x in marker_set for x in row) for row in marker])
        assert all([x == "*" or x == "." or x == "#" for x in marker_set])
        self._marker, self._marker_set = marker, marker_set

    # TODO
    # implement __eq__, __str__ methods
    # __repr__ is up to you

    # TODO
    # override extensions
    # legal extensions consist of all configurations that can be reached by
    # making a single jump from this configuration
    def __repr__(self):
        return str(self._marker)
    def extensions(self):
        lst_gen_bor = []
        for i in range(len(self._marker)):
            for j in range(len(self._marker[i])):
                if self._marker[i][j] == ".":
                    lst_gen_bor += self.gen(i,j)
        return lst_gen_bor

    def gen(self, i, j):
        gen_bor = []
        if i < len(self._marker)-2 and self._marker[i+1][j] == "*" and self._marker[i+2][j] == "*":
            new_marker = [x[:] for x in self._marker]
            new_marker[i][j] = "*"
            new_marker[i+1][j], new_marker[i+2][j] = ".", "."
            new = GridPegSolitairePuzzle(new_marker, self._marker_set)
            gen_bor.append(new)

        elif i > 1 and self._marker[i-1][j] == "*" and self._marker[i-2][j] == "*":
            new_marker1 = [x[:] for x in self._marker]
            new_marker1[i][j] = "*"
            new_marker1[i-1][j], new_marker1[i-2][j] = ".", "."
            new = GridPegSolitairePuzzle(new_marker1, self._marker_set)
            gen_bor.append(new)

        elif j<len(self._marker[0])-2 and self._marker[i][j+1] == "*" and self._marker[i][j+2] == "*":
            new_marker2 = [x[:] for x in self._marker]
            new_marker2[i][j] = "*"
            new_marker2[i][j+1], new_marker2[i][j+2] = ".", "."
            new = GridPegSolitairePuzzle(new_marker2, self._marker_set)
            gen_bor.append(new)

        elif j> 1 and self._marker[i][j-1]=="*" and self._marker[i][j-2] == "*":
            new_marker3 = [x[:] for x in self._marker]
            new_marker3[i][j] = "*"
            new_marker3[i][j-1], new_marker3[i][j-2] = ".", "."
            new = GridPegSolitairePuzzle(new_marker3, self._marker_set)
            gen_bor.append(new)
            
        return gen_bor

    
    ## do the remaining three scenarios that are up, down, left
    
        
            

    # TODO
    # override is_solved
    # A configuration is solved when there is exactly one "*" left
    def is_solved(self):
        counter = 0
        for row in self._marker:
            counter += row.count("*")
        return counter == 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    from puzzle_tools import depth_first_solve

    grid = [["*", "*", "*", "*", "*"],
            ["*", "*", ".", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"]]
    gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
    print(gpsp.extensions())
    import time

    start = time.time()
    solution = depth_first_solve(gpsp)
    end = time.time()
    print("Solved 5x5 peg solitaire in {} seconds.".format(end - start))
    print("Using depth-first: \n{}".format(solution))
