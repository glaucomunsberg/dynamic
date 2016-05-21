from Configuration import Configuration
from Interface import Interface
from random import randint
from copy import copy, deepcopy

class TicTacToe:
    _config	        = None
    _matrix         = None
    _interface      = None
    _tree           = None

    # Start the configuraton
    def __init__(self):
        self._config    = Configuration()
        self._interface = Interface()
        self._tree = Node()
        self._winners = [0,0]

    def createBoard(self):
        self._matrix = [ [ 0 for i in range(3) ] for j in range(3) ]

    def getBoard(self):
        return self._matrix

    def randomBoard(self):
        for i in range(3):
            for j in range(3):
                self._matrix[i][j] = randint(0,2)

    def canPlayAt(self,matrix):
        possiblePositions = []
        for i in range(3):
            for j in range(3):
                if matrix[i][j] == 0:
                    possiblePositions.append([i,j])

        return possiblePositions

    # return array [player,stoke]
    # player{0:none,1:x,2:o}
    # stoke{0:{0,1,2},1:{3,4,5},2:{6,7,8},3:{0,3,6},4:{1,4,7},5:{2,5,8},6:{0,4,8},7:{2,4,6}}
    def winnerOnBoard(self, matrix):

        #  0  1  2
        #  3  4  5
        #  6  7  8

        if matrix[0][0] == matrix[0][1] == matrix[0][2] == 1:
            return [1,0]
        elif matrix[0][0] == matrix[0][1] == matrix[0][2] == 2:
            return [2,0]
        elif matrix[1][0] == matrix[1][1] == matrix[1][2] == 1:
            return [1,1]
        elif matrix[1][0] == matrix[1][1] == matrix[1][2] == 2:
            return [2,1]
        elif matrix[2][0] == matrix[2][1] == matrix[2][2] == 1 :
            return [1,2]
        elif matrix[2][0] == matrix[2][1] == matrix[2][2] == 2 :
            return [2,2]
        elif matrix[0][0] == matrix[1][0] == matrix[2][0] == 1:
            return [1,3]
        elif matrix[0][0] == matrix[1][0] == matrix[2][0] == 2:
            return [2,3]
        elif matrix[0][1] == matrix[1][1] == matrix[2][1] == 1:
            return [1,4]
        elif matrix[0][1] == matrix[1][1] == matrix[2][1] == 2:
            return [2,4]
        elif matrix[0][2] == matrix[1][2] == matrix[2][2] == 1:
            return [1,5]
        elif matrix[0][2] == matrix[1][2] == matrix[2][2] == 2:
            return [2,5]
        elif matrix[0][0] == matrix[1][1] == matrix[2][2] == 1:
            return [1,6]
        elif matrix[0][0] == matrix[1][1] == matrix[2][2] == 2:
            return [2,6]
        elif matrix[0][2] == matrix[1][1] == matrix[2][0] == 1:
            return [1,7]
        elif matrix[0][2] == matrix[1][1] == matrix[2][0] == 2:
            return [2,7]
        else:
            return [0,0]

    def printBoard(self):
        self._interface.printXO(self._matrix)

    def newNode(self,matrix,theType):
        node = Tree()
        node.matrix = matrix
        node.type = theType
        return node

    def createSubNodes(self,node):

        matrix = deepcopy(node.matrix)
        possibles = self.canPlayAt(matrix)
        #print 'type',node.type
        print 'Possibles',possibles

        for i in range(len(possibles)):

            matrix = deepcopy(node.matrix)
            myType = ''
            if node.type == 'max':
                matrix[possibles[i][0]][possibles[i][1]] = 1
                myType = 'min'
            else:
                matrix[possibles[i][0]][possibles[i][1]] = 2
                myType = 'max'
            newNode = Node(matrix,[],myType,0)
            node.nodes.append(newNode)
            #print 'node.matrix    ', node.matrix
            #print 'Possible       ',possibles[i]
            #print 'Pos            ',pos_i,pos_j
            #print 'newNode.matrix ',newNode.matrix
            #print 'newNode.type   ',newNode.type
            #print ''


    #   1 win +1
    #   2 win -1
    def checkNode(self,node):
        print 'checkNode Matrix',node.matrix
        isWinner = self.winnerOnBoard(node.matrix)
        #print 'isWinner',isWinner
        if isWinner[0] == 0:
            print 'plaing'
            winnerBy = -2222
            values = []
            self.createSubNodes(node)
            for i in range(len(node.nodes)):
                value = self.checkNode(node.nodes[i])
                if i == 0:
                    winnerBy = value
                values.append(value)
                print 'value:', value
                if node.type == 'max':
                    if value > winnerBy:
                        winnerBy = value
                else:
                    if value < winnerBy:
                        winnerBy = value
            node.value = winnerBy
            print 'minMax',node.type
            print 'values',values
            print 'send to up',winnerBy
            return node.value
        else:
            print 'winner!'
            self._winners[isWinner[0]-1] += 1
            if isWinner[0] == 1:
                return +1
            else:
                return -1



    def playTicTacToe(self):
        self._tree = Node(deepcopy(self._matrix),[],'max',0)
        self.createSubNodes(self._tree)
        self.checkNode(self._tree)
        print 'number of winners'
        print 'player 1',self._winners[0]
        print 'player 2',self._winners[1]
        print 'tree value',self._tree.value




class Node(object):
    def __init__(self, matrix=None,nodes=[],myType='max',value=0):
        self.matrix = matrix
        self.nodes = nodes
        self.type = myType
        self.value = value
