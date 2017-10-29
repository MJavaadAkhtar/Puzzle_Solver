"""
Some functions for working with puzzles
"""
from puzzle import Puzzle
from collections import deque
# set higher recursion limit
# which is needed in PuzzleNode.__str__
# you may uncomment the next lines on a unix system such as CDF
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
import sys
sys.setrecursionlimit(10**6)

'''
Help from
http://code.activestate.com/recipes/576723-dfs-and-bfs-graph-traversal/
for the BFS
'''

# TODO
# implement depth_first_solve
# do NOT change the type contract
# you are welcome to create any helper functions
# you like
def depth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child containing an extension of the puzzle
    in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode
    """
    visited = []
    return recursive_dfs(puzzle, visited)
    
    

def recursive_dfs(puzzle, visited):
    p = PuzzleNode(puzzle)
    if puzzle.is_solved():
        return p
    else:
        h =  puzzle.extensions()
        print (h)
        if len(h) == 0:
            return None
        for child in h:
            if not child.fail_fast() and child not in visited:
                visited.append(child)
                sol = recursive_dfs(child, visited)
                if sol:
                    p.children.append(sol)
                    return p
        return None
    
        
        
        

# TODO
# implement breadth_first_solve
# do NOT change the type contract
# you are welcome to create any helper functions
# you like
# Hint: you may find a queue useful, that's why
# we imported deque
def breadth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child PuzzleNode containing an extension
    of the puzzle in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode
    """
    r = PuzzleNode(puzzle)
    new_queue = deque()
    visited = []
    for p in puzzle.extensions():
        new_ext = PuzzleNode(p, None,r)
        visited.append(p)
        r.children.append(new_ext)
    new_queue.extend(r.children)
    
    while new_queue:
        element = new_queue.popleft()
        if element.puzzle.is_solved():
            while element.parent:
                element.parent.children = [element]
                element = element.parent
            return r
        for p in element.puzzle.extensions():
            new_ext = PuzzleNode(p,None,element)
            if p not in  visited:               
                element.children.append(new_ext)
                visited.append(p)
        new_queue.extend(element.children)
    return None
                
            

       


# Class PuzzleNode helps build trees of PuzzleNodes that have
# an arbitrary number of children, and a parent.
class PuzzleNode:
    """
    A Puzzle configuration that refers to other configurations that it
    can be extended to.
    """

    def __init__(self, puzzle=None, children=None, parent=None):
        """
        Create a new puzzle node self with configuration puzzle.

        @type self: PuzzleNode
        @type puzzle: Puzzle | None
        @type children: list[PuzzleNode]
        @type parent: PuzzleNode | None
        @rtype: None
        """
        self.puzzle, self.parent = puzzle, parent
        if children is None:
            self.children = []
        else:
            self.children = children[:]

    def __eq__(self, other):
        """
        Return whether Puzzle self is equivalent to other

        @type self: PuzzleNode
        @type other: PuzzleNode | Any
        @rtype: bool

        >>> from word_ladder_puzzle import WordLadderPuzzle
        >>> pn1 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "no", "oo"}))
        >>> pn2 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "oo", "no"}))
        >>> pn3 = PuzzleNode(WordLadderPuzzle("no", "on", {"on", "no", "oo"}))
        >>> pn1.__eq__(pn2)
        True
        >>> pn1.__eq__(pn3)
        False
        """
        return (type(self) == type(other) and
                self.puzzle == other.puzzle and
                all([x in self.children for x in other.children]) and
                all([x in other.children for x in self.children]))

    def __str__(self):
        """
        Return a human-readable string representing PuzzleNode self.

        # doctest not feasible.
        """
        return "{}\n\n{}".format(self.puzzle,
                                 "\n".join([str(x) for x in self.children]))
