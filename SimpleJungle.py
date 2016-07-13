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
    _IA             = None

    def __init__(self):

        self._config    = Configuration()
        self._config.size_puzzle = 7 # Configuration to show a correctly tablet

        self._interface = Interface()
        self._state     = State()

        self._IA        = IA()

        #self._interface.printJungle(self._state.matrix)
        print self._state.statusHash()


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

            #self._interface.clear()


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

                if self._jungleConfig.howPlay()['is_human']:
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


    def playerMachine(self):
        print " Player "+str(self._jungleConfig.howPlay()['player_number'])+" (Machine)"
        print " Waiting..."

        #self._IA.calculateScore(self._state,self._jungleConfig)

        #print 'AllCommands'
        #print str(allCommands)
        allCommands         = self._IA.movesOnScene(self._state,self._jungleConfig)
        commands            = self._IA.getBestMoveOnMoves(deepcopy(allCommands), deepcopy(self._state), deepcopy(self._jungleConfig))
        #commands            = self._IA.bestMoveOnScene(self._state,self._jungleConfig)
        moviment_is_valid   = commands['is_valid']
        message             = commands['message']
        print 'command'
        print str(commands)

        if moviment_is_valid:
            self._state.checkPosition(commands['short_label'],commands['quadrant_to_go'])
            self._state.updateAnimal(self._jungleConfig.howPlay()['player'],commands['short_label'][0],commands['quadrant_to_go'])

        self._jungleConfig.nextPlayer()

class State:
    _config     = None
    players     = None
    burrows     = None
    matrix      = None
    depth       = 0
    score       = -9999
    childrens   = None

    def __init__(self):
        self._config    = Configuration()
        self.players     = PlayerConfiguration()
        self.burrows     = BurrowsConfiguration()
        self.matrix      = [['  ' for x in range(self._config.size_jungle)] for x in range(self._config.size_jungle)]
        self.children    = []
        self.update()

    # Update is a method that look inside
    #   que informations of players and the board
    #   and create a matrix that help to view the
    #   information
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

    # update information about the animal on
    #   this state
    def updateAnimal(self,player,animal,position=None,live=True,eat_by=None):

        self.players.players[player][animal]['position'] = position
        self.players.players[player][animal]['live'] = live
        self.players.players[player][animal]['eat_by'] = eat_by
        self.update()

    # check it the status have a winner
    def won_by(self):
        if self.burrows.burrows['player_1']['in'] != None:
            return 'Player 2'
        elif self.burrows.burrows['player_2']['in'] != None:
            return 'Player 1'
        else:
            return None

    # before move is necessary, for example, check
    #   if some animal will be eat, if true we need
    #   put those information inside the animal information
    #   informations like who and how was eat is necessary
    #   for a number of reasons
    def checkPosition(self,animal,currentPosition):
        animal_eated = self.matrix[currentPosition[0]][currentPosition[1]]
        if animal_eated != '  ' and animal_eated != "B1" and animal_eated != "B2":
            self.players.players['player_'+animal_eated[1]][animal_eated[0]]['eat_by'] = animal
            self.players.players['player_'+animal_eated[1]][animal_eated[0]]['live'] = False
        elif animal_eated == "B1" or animal_eated == "B2":
            print 'burrow',animal_eated
            print 'animal',animal
            if animal_eated == "B1":
                self.burrows.burrows['player_1']['in'] = animal
            else:
                self.burrows.burrows['player_2']['in'] = animal


    # transform the elements on hash
    #   to permit other states to compare your content with this.
    #   Cut the string after 4 caracteres, the first half "R2" is
    #   the animal "C" and the player "2" and the second half "01"
    #   is the position on board [0,1].
    #
    #   result example "R201E205T212C214C122T154E161R165"
    def statusHash(self):
        the_hash = ''
        for i in range(self._config.size_jungle):
            for j in range(self._config.size_jungle):
                if self.matrix[i][j] != '  ' and self.matrix[i][j] != 'B1' and  self.matrix[i][j] != 'B2':
                    the_hash += self.matrix[i][j]
                    the_hash += str(i)
                    the_hash += str(j)

        return the_hash
