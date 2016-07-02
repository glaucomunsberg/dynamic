from TicTacToe import TicTacToe
from Puzzle import Puzzle
from Configuration import Configuration
from SimpleJungle import SimpleJungle
import time

if __name__ == "__main__":

    Configuration = Configuration()

    puzzle      = Puzzle()
    ticTacToe   = TicTacToe()
    simpleJungle = SimpleJungle()

    puzzle.createMatrix()
    puzzle.shakeMatrix(puzzle.getMatrix())

    ticTacToe.createBoard()


    for i in range(Configuration.times_tests):
        print '\nTest '+str(i)


        #xsAndOs.randomBoard()


        start = time.time()

        #puzzle.Astar(puzzle.getMatrix())
        #ticTacToe.playTicTacToe()
        simpleJungle.singlePlayer()
        
        end = time.time()
        elapsed = end - start
        print 'running at',elapsed,'seconds'
