from Interface import Interface


class PlayerConfiguration:
    players         = None

    def __init__(self):

        self.players = {}

        self.players['player_1'] = {}
        self.players['player_1']['R'] = {}
        self.players['player_1']['R']['position'] = [6,5]
        self.players['player_1']['R']['label'] = 'Rato'
        self.players['player_1']['R']['short_label'] = 'R1'
        self.players['player_1']['R']['live'] = True
        self.players['player_1']['R']['eat_by'] = None
        self.players['player_1']['E'] = {}
        self.players['player_1']['E']['position'] = [6,1]
        self.players['player_1']['E']['label'] = 'Elefante'
        self.players['player_1']['E']['short_label'] = 'E1'
        self.players['player_1']['E']['live'] = True
        self.players['player_1']['E']['eat_by'] = None
        self.players['player_1']['T'] = {}
        self.players['player_1']['T']['position'] = [5,4]
        self.players['player_1']['T']['label'] = 'Tigre'
        self.players['player_1']['T']['short_label'] = 'T1'
        self.players['player_1']['T']['live'] = True
        self.players['player_1']['T']['eat_by'] = None
        self.players['player_1']['C'] = {}
        self.players['player_1']['C']['position'] = [5,2]
        self.players['player_1']['C']['label'] = 'Cachorro'
        self.players['player_1']['C']['short_label'] = 'C1'
        self.players['player_1']['C']['live'] = True
        self.players['player_1']['C']['eat_by'] = None
        self.players['player_2'] = {}
        self.players['player_2']['R'] = {}
        self.players['player_2']['R']['position'] = [0,1]
        self.players['player_2']['R']['label'] = 'Rato'
        self.players['player_2']['R']['short_label'] = 'R2'
        self.players['player_2']['R']['live'] = True
        self.players['player_2']['R']['eat_by'] = None
        self.players['player_2']['E'] = {}
        self.players['player_2']['E']['position'] = [0,5]
        self.players['player_2']['E']['label'] = 'Elefante'
        self.players['player_2']['E']['short_label'] = 'E2'
        self.players['player_2']['E']['live'] = True
        self.players['player_2']['E']['eat_by'] = None
        self.players['player_2']['T'] = {}
        self.players['player_2']['T']['position'] = [1,2]
        self.players['player_2']['T']['label'] = 'Tigre'
        self.players['player_2']['T']['short_label'] = 'T2'
        self.players['player_2']['T']['live'] = True
        self.players['player_2']['T']['eat_by'] = None
        self.players['player_2']['C'] = {}
        self.players['player_2']['C']['position'] = [1,4]
        self.players['player_2']['C']['label'] = 'Cachorro'
        self.players['player_2']['C']['short_label'] = 'C2'
        self.players['player_2']['C']['live'] = True
        self.players['player_2']['C']['eat_by'] = None


class BurrowsConfiguration:
    burrows         = None

    def __init__(self):
        self.burrows  = {}
        self.burrows['player_1'] = {}
        self.burrows['player_1']['position'] = [6,3]
        self.burrows['player_1']['label'] = 'B1'
        self.burrows['player_2'] = {}
        self.burrows['player_2']['position'] = [0,3]
        self.burrows['player_2']['label'] = 'B2'

class JungleConfiguration:
    _interface  = None
    combat_type = None
    move = 1
    #   combat_type {"HM","HH","MH","MM"}. Labels {"H"=>"Human","M"=>"Machine"}
    _player     = None

    def __init__(self,combat='HM'):
        self._interface = Interface()
        self.setCombatType()

    def setCombatType(self,combat='HM'):
        self.combat_type = combat
        self._player = {}
        self._player['player']          = 'player_1'
        self._player['player_number']   = 1

        if self.combat_type == "HM":
            self._player['is_human'] = True
        elif self.combat_type == "MH":
            self._player['is_human'] = False
        elif self.combat_type == "HH":
            self._player['is_human'] = True
        else: #"MM"
            self._player['is_human'] = False

    def howPlay(self):
        return self._player

    def nextPlayer(self):

        # change the player
        self.move += 1
        if self._player['player'] == 'player_1':
            self._player['player']          = 'player_2'
            self._player['player_number']   = 2
        else:
            self._player['player']          = 'player_1'
            self._player['player_number']   = 1

        # set if the player is human or not
        if self.combat_type == 'HH':
            self._player['is_human'] = True
        elif self.combat_type == "MH":
            if self._player['player'] == 'player_1':
                self._player['is_human'] = False
            else:
                self._player['is_human'] = True
        elif self.combat_type == "HM":
            if self._player['player'] == 'player_1':
                self._player['is_human'] = True
            else:
                self._player['is_human'] = False
        else: # "MM"
            if self._player['player'] == 'player_1':
                self._player['is_human'] = False
            else:
                self._player['is_human'] = False

    def setCombatTypeInterface(self):
        self._interface.clear()
        print "\n                   Simple Jungle                    \n"
        print "Players Mode"
        print " 1) Human   x Machine"
        print " 2) Human   x Human"
        print " 3) Machine x Machine"
        print " 4) Machine x Human"

        try:
            mode=int(raw_input('\nMode Number[1-4]:'))
        except ValueError:
            print 'Oops! We choose for you the Human x Machine'
            mode = 1

        if mode == 1:
            self.setCombatType("HM")
        elif mode == 2:
            self.setCombatType("HH")
        elif mode == 3:
            self.setCombatType("MM")
        elif mode == 4:
            self.setCombatType("MH")
        else:
            self.setCombatType("HM")



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

    # command example "T1 to D1"
    def interpretHumanCommand(self,command,jungleConfig,state):
        matrix  = state.matrix
        players = state.players.players

        #print 'command: '+command+" size: "+str(len(command_bits))

        command_interpreted = {}
        command_interpreted['message']  = ""
        command_interpreted['is_valid'] = False

        command = command.upper()
        command_bits = command.split()

        if len(command_bits) != 3:
            command_interpreted['is_valid'] = False
            command_interpreted['message'] = "Command invalid. Try something like 'E2 to F1'"

        else:

            animal      = command_bits[0]
            quadrant    = command_bits[2]
            pipe        = command_bits[1]
            player      = jungleConfig.howPlay()['player']

            if pipe != "TO":
                command_interpreted['message'] = "You can use other word, but the right is 'to'"


            if animal == "B1" or animal == "B2":
                command_interpreted['message'] = "You can't move this a burrow"
                command_interpreted['is_valid'] = False
                return command_interpreted

            for i in players[player]:
                if animal == players[player][i]['short_label'] and players[player][i]['live']:
                    command_interpreted['is_valid'] = True

            if not command_interpreted['is_valid']:
                command_interpreted['message'] = "You can't move this animal"
                return command_interpreted


            positionAnimal = self.animalTextToPosition(animal,matrix)
            possiblesPositionsAnimal = self.animalPossiblesMoves(positionAnimal)
            quadrant_position = self.validMoveText(quadrant)

            if len(quadrant_position) == 0:
                command_interpreted['message'] = "Quadrant "+quadrant+" is not valid"
                command_interpreted['is_valid'] = False
                return command_interpreted
            # 
            for possible in possiblesPositionsAnimal:
                if possible == quadrant_position:
                    command_interpreted['is_valid'] = True
                    command_interpreted['current_position'] = positionAnimal
                    command_interpreted['quadrant_to_go'] = quadrant_position
                    return command_interpreted

        return command_interpreted

    def animalTextToPosition(self,animal,matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if animal == matrix[i][j]:
                    position = [i,j]
        return position

    def validMoveText(self,position):
        if position[0] == "A" or position[0] == "B" or position[0] == "C" or position[0] == "D" or position[0] == "E" or position[0] == "F" or position[0] == "G":
            try:
                value_i = -1
                value_j = int(position[1])
                if value_j >= 0 and value_j <= 6:
                    if position[0] == "A":
                        value_i = 0
                    elif position[0] == "B":
                        value_i = 1
                    elif position[0] == "C":
                        value_i = 2
                    elif position[0] == "D":
                        value_i = 3
                    elif position[0] == "E":
                        value_i = 4
                    elif position[0] == "F":
                        value_i = 5
                    elif position[0] == "G":
                        value_i = 6
                    return [value_i,value_j]
                else:
                    return []
            except:
                return []
        else:
            return []

    def animalPossiblesMoves(self,currentPosition):

        # Corner
        #   only 2 possilities
        size = 6
        if currentPosition[0] == 0 and currentPosition[1] == 0:
            return [[1,0],[0,1]]
        if currentPosition[0] == size and currentPosition[1] == 0:
            return [[size-1,0],[size,1]]
        if currentPosition[0] == size and currentPosition[1] == size:
            return [[size,size-1],[size-1,size]]
        if currentPosition[0] == 0 and currentPosition[1] == size:
            return [[0,size-1],[1,size]]

        # Margin
        #   three possibilities
        if currentPosition[0] == 0:
            return [[currentPosition[0],currentPosition[1]-1],[currentPosition[0],currentPosition[1]+1],[currentPosition[0]+1,currentPosition[1]]]
        if currentPosition[0] == size:
            return [[currentPosition[0],currentPosition[1]-1],[currentPosition[0],currentPosition[1]+1],[currentPosition[0]-1,currentPosition[1]]]
        if currentPosition[1] == 0:
            return [[currentPosition[0]-1,currentPosition[1]],[currentPosition[0]+1,currentPosition[1]],[currentPosition[0],currentPosition[1]+1]]
        if currentPosition[1] == size:
            return [[currentPosition[0]-1,currentPosition[1]],[currentPosition[0]+1,currentPosition[1]],[currentPosition[0],currentPosition[1]-1]]

        # Inside
        #   four possibilities
        return [[currentPosition[0]-1,currentPosition[1]],[currentPosition[0]+1,currentPosition[1]],[currentPosition[0],currentPosition[1]-1],[currentPosition[0],currentPosition[1]+1]]
