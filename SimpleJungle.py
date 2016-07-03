from Configuration import Configuration
from Structure import *
from Interface import Interface
from SimpleJungleHelpers import *
import os


class SimpleJungle:
    _config	        = None
    _burrowConfig   = None
    _animalsConfig  = None
    _interface      = None
    _jungleConfig   = None
    _rules          = None
    _state          = None

    def __init__(self):

        self._config    = Configuration()
        self._config.size_puzzle = 7 # Configuration to show a correctly tablet

        self._interface = Interface()
        self._state = State()

        #self._interface.printJungle(self._state.matrix)
        #print self._state.statusHash()



    def play(self,combat_type=None):

        someone_win         = False

        self._jungleConfig  = JungleConfiguration()
        self._rules         = Rules()

        self._interface.clear()

        if combat_type != None:
            self._jungleConfig.setCombatType(combat_type)
        else:
            self._jungleConfig.setCombatTypeInterface()

        while not someone_win:

            self._interface.clear()
            print "\n                   Simple Jungle                    \n"
            print " Play "+str(self._jungleConfig.move)
            self._interface.printJungle(self._state.matrix)



            if self._jungleConfig.howPlay()['is_human']:
                self.playerHuman()
            else:
                self.playerMachine()

    def playerHuman(self):
        print " Player "+str(self._jungleConfig.howPlay()['player_number'])+" (Human)"
        is_valid    = False
        message     = ""
        while not is_valid:
            if message != "":
                print message

            commands    = self._rules.interpretHumanCommand(raw_input('\nCommand:'),self._jungleConfig,self._state)
            is_valid    = commands['is_valid']
            message     = commands['message']

        self._jungleConfig.nextPlayer()
        raw_input('\nPress Enter')

    def playerMachine(self,):
        print " Player "+str(self._jungleConfig.howPlay()['player_number'])+" (Machine)"
        print " Waiting..."
        self._jungleConfig.nextPlayer()

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
