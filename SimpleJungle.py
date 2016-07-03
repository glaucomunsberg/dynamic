from Configuration import Configuration
from Structure import *
from Interface import Interface
from SimpleJungleHelpers import *
import os, copy



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

            player_winner = self._state.won_by()

            if player_winner != None:

                someone_win = True

                if self._jungleConfig.howPlay()['is_human']
                    self._interface.winnerHummanView(player_winner)
                else:
                    self._interface.winnerMachineView(player_winner)


    def playerHuman(self):
        print " Player "+str(self._jungleConfig.howPlay()['player_number'])+" (Human)"
        moviment_is_valid    = False
        message     = ""
        while not moviment_is_valid:
            if message != "":
                print message

            commands            = self._rules.interpretHumanCommand(raw_input('\nCommand:'),self._jungleConfig,self._state)
            moviment_is_valid   = commands['is_valid']
            message             = commands['message']

            if moviment_is_valid:
                self._state.checkPosition(commands['short_label'],commands['quadrant_to_go'])
                self._state.updateAnimal(self._jungleConfig.howPlay()['player'],commands['short_label'][0],commands['quadrant_to_go'])

        self._jungleConfig.nextPlayer()
        if not commands['is_valid']:
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
    score   = 0

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
                if self.players.players[i][j]['live']:
                    self.matrix[self.players.players[i][j]['position'][0]][self.players.players[i][j]['position'][1]] = self.players.players[i][j]['short_label']

        for i in self.burrows.burrows:
            if self.burrows.burrows[i]['in'] == None:
                self.matrix[self.burrows.burrows[i]['position'][0]][self.burrows.burrows[i]['position'][1]] = self.burrows.burrows[i]['label']

    def updateAnimal(self,player,animal,position=None,live=True,eat_by=None):
        if position != None:
            self.players.players[player][animal]['position'] = position
        self.players.players[player][animal]['live'] = live
        self.players.players[player][animal]['eat_by'] = eat_by
        self.update()

    def won_by(self):
        if self.burrows.burrows['player_1']['in'] != None:
            return 'Player 2'
        elif self.burrows.burrows['player_2']['in'] != None:
            return 'Player 1'
        else:
            return None


    def checkPosition(self,animal,currentPosition):
        animal_eated = self.matrix[currentPosition[0]][currentPosition[1]]
        if animal_eated != '  ' and animal_eated == "B1" and animal_eated != "B2":
            print 'eat:'+animal_eated
            self.players.players['player_'+animal_eated[1]][animal_eated[0]]['eat_by'] = animal
            self.players.players['player_'+animal_eated[1]][animal_eated[0]]['live'] = False
        elif animal_eated == "B1" or animal_eated == "B2":
            print 'burrow',animal_eated
            print 'animal',animal
            if animal_eated == "B1":
                self.burrows.burrows['player_1']['in'] = animal
            else:
                self.burrows.burrows['player_2']['in'] = animal



    def statusHash(self):
        the_hash = ''
        for i in range(self._config.size_jungle):
            for j in range(self._config.size_jungle):
                if self.matrix[i][j] != '  ' and self.matrix[i][j] != 'B1' and  self.matrix[i][j] != 'B2':
                    the_hash += self.matrix[i][j]
                    the_hash += str(i)
                    the_hash += str(j)

        return the_hash
