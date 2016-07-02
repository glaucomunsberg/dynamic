from Configuration import Configuration
from Structure import *
from Interface import Interface
import os


class SimpleJungle:
    _config	        = None
    _matrix         = None
    _burrowConfig   = None
    _animalsConfig  = None
    _interface      = None
    clear = lambda : os.system('tput reset')

    def __init__(self):

        self._config    = Configuration()
        # Configuration to show a correctly tablet
        self._config.size_puzzle = 7

        self._interface = Interface()

        self._matrix  = [['  ' for x in range(self._config.size_jungle)] for x in range(self._config.size_jungle)]

        self._state = State()

        self._interface.printJungle(self._state.matrix)

        print self._state.statusHash()



    def singlePlayer(self):
        self.clear
        print 'Simple Jungle'
        print ''
        print 'Play as'
        print ' 1 - Player 1'
        print ' 2 - Player 2'
        try:
            mode=int(raw_input('Choice:'))
            if mode != 1:

        except:
            print("Oops!  That was no valid number.  Try again...")

        print 'vamos continuar'


    def twoPlayer(self):
        print 'two'

    def printMatrix(self):
        print 'self'


class State:
    _config = None
    players = None
    burrows = None
    matrix  = None

    def __init__(self):
        self._config    = Configuration()
        self.players     = PlayerConfiguration()
        self.burrows     = BurrowsConfiguration()
        self.matrix      = [['  ' for x in range(self._config.size_jungle)] for x in range(self._config.size_jungle)]
        self.update()

    def update(self):

        for i in range(self._config.size_jungle):
            for j in range(self._config.size_jungle):
                self.matrix[i][j] = '  '

        for i in self.players.players:
            for j in self.players.players[i]:
                self.matrix[self.players.players[i][j]['position'][0]][self.players.players[i][j]['position'][1]] = self.players.players[i][j]['short_label']

        for i in self.burrows.burrows:
            self.matrix[self.burrows.burrows[i]['position'][0]][self.burrows.burrows[i]['position'][1]] = self.burrows.burrows[i]['label']

    def statusHash(self):
        the_hash = ''
        for i in range(self._config.size_jungle):
            for j in range(self._config.size_jungle):
                if self.matrix[i][j] != '  ' and self.matrix[i][j] != 'B1' and  self.matrix[i][j] != 'B2':
                    the_hash += self.matrix[i][j]
                    the_hash += str(i)
                    the_hash += str(j)

        return the_hash

class PlayerConfiguration:
    players         = None

    def __init__(self):

        self.players = {}

        self.players['player_1'] = {}
        self.players['player_1']['R'] = {}
        self.players['player_1']['R']['position'] = [6,5]
        self.players['player_1']['R']['label'] = 'Rato'
        self.players['player_1']['R']['short_label'] = 'E2'
        self.players['player_1']['R']['live'] = True
        self.players['player_1']['R']['eat_by'] = None
        self.players['player_1']['E'] = {}
        self.players['player_1']['E']['position'] = [6,1]
        self.players['player_1']['E']['label'] = 'Elefante'
        self.players['player_1']['E']['short_label'] = 'E2'
        self.players['player_1']['E']['live'] = True
        self.players['player_1']['E']['eat_by'] = None
        self.players['player_1']['E']['short_label'] = 'E2'
        self.players['player_1']['T'] = {}
        self.players['player_1']['T']['position'] = [5,4]
        self.players['player_1']['T']['label'] = 'Tigre'
        self.players['player_1']['T']['short_label'] = 'T2'
        self.players['player_1']['T']['live'] = True
        self.players['player_1']['T']['eat_by'] = None
        self.players['player_1']['C'] = {}
        self.players['player_1']['C']['position'] = [5,2]
        self.players['player_1']['C']['label'] = 'Cachorro'
        self.players['player_1']['C']['short_label'] = 'C2'
        self.players['player_1']['C']['live'] = True
        self.players['player_1']['C']['eat_by'] = None
        self.players['player_2'] = {}
        self.players['player_2']['R'] = {}
        self.players['player_2']['R']['position'] = [0,1]
        self.players['player_2']['R']['label'] = 'Rato'
        self.players['player_2']['R']['short_label'] = 'R1'
        self.players['player_2']['R']['live'] = True
        self.players['player_2']['R']['eat_by'] = None
        self.players['player_2']['E'] = {}
        self.players['player_2']['E']['position'] = [0,5]
        self.players['player_2']['E']['label'] = 'Elefante'
        self.players['player_2']['E']['short_label'] = 'E1'
        self.players['player_2']['E']['live'] = True
        self.players['player_2']['E']['eat_by'] = None
        self.players['player_2']['T'] = {}
        self.players['player_2']['T']['position'] = [1,2]
        self.players['player_2']['T']['label'] = 'Tigre'
        self.players['player_2']['T']['short_label'] = 'T1'
        self.players['player_2']['T']['live'] = True
        self.players['player_2']['T']['eat_by'] = None
        self.players['player_2']['C'] = {}
        self.players['player_2']['C']['position'] = [1,4]
        self.players['player_2']['C']['label'] = 'Cachorro'
        self.players['player_2']['C']['short_label'] = 'C1'
        self.players['player_2']['C']['live'] = True
        self.players['player_2']['C']['eat_by'] = None


class BurrowsConfiguration:
    burrows         = None

    def __init__(self):
        self.burrows  = {}
        self.burrows['player_1'] = {}
        self.burrows['player_1']['position'] = [0,3]
        self.burrows['player_1']['label'] = 'B1'
        self.burrows['player_2'] = {}
        self.burrows['player_2']['position'] = [6,3]
        self.burrows['player_2']['label'] = 'B2'

class JungleConfiguration:
    combat_type     = None
    #   combat_type {"HM","HH","MH"}. Labels {"H"=>"Human","M"=>"Machine"}
    _machinePlayer  = None

    def __init__(self,combat='HM'):
        self.combat_type = combat
        if self.combat_type == "HM":
            self._machinePlayer = 'player_2'
        elif self.combat_type == "MH":
            self._machinePlayer = 'player_1'

class Rules:
    animals = None

    def __init__(self):

        self.animals = {}
        self.animals['C']           = {}
        self.animals['C']['eat']    = ['C','R']
        self.animals['C']['food']   = ['C','T','E']
        self.animals['T']           = {}
        self.animals['T']['eat']    = ['T','C','R']
        self.animals['T']['food']   = ['T','E']
        self.animals['E']           = {}
        self.animals['E']['eat']    = ['E','T','C']
        self.animals['E']['foot']   = ['E','R']
        self.animals['R']           = {}
        self.animals['R']['eat']    = ['R','E']
        self.animals['R']['food']   = ['T','C','R']
