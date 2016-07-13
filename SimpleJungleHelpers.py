from Interface import Interface
from random import randint
from SimpleJungle import *

from copy import copy, deepcopy
import operator


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
        self.players['player_1']['C']['position'] = [2,2] #[5,2]
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
        self.burrows['player_1']['in'] = None
        self.burrows['player_2'] = {}
        self.burrows['player_2']['position'] = [0,3]
        self.burrows['player_2']['label'] = 'B2'
        self.burrows['player_2']['in'] = None

class JungleConfiguration:
    _interface  = None
    combat_type = None
    move = 1
    #   combat_type {"HM","HH","MH","MM"}. Labels {"H"=>"Human","M"=>"Machine"}
    _player     = None

    def __init__(self,combat='HM'):
        self._interface = Interface()
        self.setCombatType()

    # this method will influence how the game player
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

    # change the player 1 to player 2 and vice versa
    def nextPlayer(self):


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
       #print "\n                   Simple Jungle                    \n"
       #print "Players Mode"
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
        self.animals['C']['score']  = 0.25
        self.animals['T']           = {}
        self.animals['T']['eat']    = ['T','C','R']
        self.animals['T']['food']   = ['T','E']
        self.animals['T']['score']  = 0.5
        self.animals['E']           = {}
        self.animals['E']['eat']    = ['E','T','C']
        self.animals['E']['food']   = ['E','R']
        self.animals['E']['score']  = 0.7
        self.animals['R']           = {}
        self.animals['R']['eat']    = ['R','E']
        self.animals['R']['food']   = ['T','C','R']
        self.animals['R']['score']  = 1

    # command example "T1 to D1" and out
    #   a lot of information about how this command
    #   need be operate in the Jungle
    def interpretHumanCommand(self,command,jungleConfig,state):
        matrix  = state.matrix
        players = state.players.players

        #print 'command: '+command+" size: "+str(len(command_bits))

        command_interpreted = {}
        command_interpreted['message']      = ""
        command_interpreted['is_valid']     = False
        command_interpreted['short_label']  = ""
        command_interpreted['quadrant_to_go']   = []
        command_interpreted['player']       = ""

        if command == "" or command == None:
            command_interpreted['is_valid'] = False
            command_interpreted['message'] = "Command empty. Try something like 'E2 to F1'"
            return command_interpreted

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

            # check if the animal is live if not the commmand is invalid
            for i in players[player]:
                if animal == players[player][i]['short_label'] and players[player][i]['live']:
                    command_interpreted['is_valid'] = True

            if not command_interpreted['is_valid']:
                command_interpreted['message'] = "You can't move this animal"
                return command_interpreted


            positionAnimal = self.animalTextToPosition(animal,matrix)
            possiblesPositionsAnimal = self.possiblesMoves(positionAnimal)

            quadrant_position = self.validMoveText(quadrant)

            if len(quadrant_position) == 0:
                command_interpreted['message'] = "Quadrant "+quadrant+" is not valid"
                command_interpreted['is_valid'] = False
                return command_interpreted

            #print 'before'
            #print possiblesPositionsAnimal
            possiblesPositionsAnimal = self.possiblesAndValidsMoves(matrix,players,player,animal,possiblesPositionsAnimal)
            #print 'after'
            #print possiblesPositionsAnimal


            # if the command "quadrant_position" is one of "possiblesPositionsAnimal"
            #   return valid command.
            for possible in possiblesPositionsAnimal:
                if possible == quadrant_position:
                    command_interpreted['is_valid']         = True
                    command_interpreted['short_label']      = animal
                    command_interpreted['current_position'] = positionAnimal
                    command_interpreted['quadrant_to_go']   = quadrant_position
                    command_interpreted['player']           = player
                    return command_interpreted

        command_interpreted['is_valid'] = False
        command_interpreted['message'] = "Quadrant "+quadrant+" is not valid!"
        return command_interpreted

    # return the tuple [x,y] from the search animal
    def animalTextToPosition(self,animal,matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if animal == matrix[i][j]:
                    position = [i,j]
        return position

    # this method transform comand text like "G5"
    #   to coordenates like [6,5] used on board
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

    # Return all tuples on board from the currentPosition
    def possiblesMoves(self,currentPosition):

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


    #  possiblesMoves return all possibilities, but is necessary check if
    #   the movements won't do with the movement eat your own animal.
    def possiblesAndValidsMoves(self,matrix,players,player,animal,possiblesPositions):

        returnedPossiblesPositions = []

        for possiblePosition in possiblesPositions:
            if matrix[possiblePosition[0]][possiblePosition[1]] == '  ':
                returnedPossiblesPositions.append(possiblePosition)
            else:
                animal_on_matrix = matrix[possiblePosition[0]][possiblePosition[1]]
                if animal_on_matrix[1] != animal[1]:
                    for i in self.animals[animal[0]]['eat']:
                        if i == animal_on_matrix[0]:
                            returnedPossiblesPositions.append(possiblePosition)

        return returnedPossiblesPositions

class IA:
    rules   = None
    def __init__(self):
        self.rules = Rules()

    def calculateScore(self,state,jungleConfig):
        players = state.players
        burrows = state.burrows
        player  = jungleConfig.howPlay()['player']
        player_oponent = ""
        if player == "player_1":
            player_oponent = "player_2"
        else:
            player_oponent = "player_1"
        #print 'animals of '+player
        iWillEat        = 0
        iWillFood       = 0
        distanceToWin   = 0
        for animal in players.players[player]:
            if players.players[player][animal]['live']:

                #print 'animal: '+animal

                for animalToEat in self.rules.animals[animal]['eat']:
                    if players.players[player_oponent][animalToEat]['live']:
                        iWillEat += self.manhattanDistance(players.players[player][animal]['position'],players.players[player_oponent][animalToEat]['position'])

                for animalToFood in self.rules.animals[animal]['food']:
                    if players.players[player_oponent][animalToFood]['live']:
                        iWillFood += self.manhattanDistance(players.players[player][animal]['position'],players.players[player_oponent][animalToFood]['position'])

                distanceToWin+= 11 - (self.manhattanDistance(players.players[player][animal]['position'],burrows.burrows[player_oponent]['position']) * 1.22)
                #print 'iWillEat  '+str(iWillEat)
                #print 'iWillFood '+str(iWillFood)
                #print 'distanceTo'+str(distanceToWin)
                #print 'score     '+str(iWillEat-iWillFood+distanceToWin)
        return iWillEat-iWillFood+distanceToWin

    def bestMoveOnScene(self,state,jungleConfig):
        players = state.players
        burrows = state.burrows
        matrix  = state.matrix
        player  = jungleConfig.howPlay()['player']

        player_oponent = ""

        if player == "player_1":
            player_oponent = "player_2"
            player_oponent_number = "2"
            player_number = "1"
        else:
            player_oponent = "player_1"
            player_oponent_number = "1"
            player_number = "2"

        command_interpreted = {}
        command_interpreted['message']      = ""
        command_interpreted['is_valid']     = True
        command_interpreted['short_label']  = ""
        command_interpreted['quadrant_to_go']   = None
        command_interpreted['player']       = player

        animalsScores           = {}
        bestAnimalScore         = 0
        animalsToEat            = {}
        averageAnimalsToEat     = 0
        animalsToFeed           = {}
        averangeAnimalsToFeed   = 0
        bestToSafe              = []
        bestToEat               = []
        averangeToBurrow        = 0

        for animal in players.players[player]:
            if players.players[player][animal]['live']:
                iWillEat        = 0
                iWillFeed       = 0
                distanceToWin   = 0
                #print 'animal: '+animal


                # calculate the avarange to borrow
                averangeToBurrow  = (averangeToBurrow+self.manhattanDistance(players.players[player][animal]['position'],burrows.burrows[player_oponent]['position']))/2

                # calculate the distante of animals that this eat
                for animalToEat in self.rules.animals[animal]['eat']:
                    if players.players[player_oponent][animalToEat]['live']:

                        distance  = self.manhattanDistance(players.players[player][animal]['position'],players.players[player_oponent][animalToEat]['position'])
                        if animal in animalsToEat:
                            animalsToEat[animal] += distance
                        else:
                            animalsToEat[animal] = distance

                        if distance == 1:
                            bestToEat.append([animalToEat,animal])

                        iWillEat += distance
                        averageAnimalsToEat = (averageAnimalsToEat+distance)/2
                for animalToFeed in self.rules.animals[animal]['food']:
                    if players.players[player_oponent][animalToEat]['live']:
                        distance  = self.manhattanDistance(players.players[player][animal]['position'],players.players[player_oponent][animalToFeed]['position'])
                        if distance <= 4:
                            iWillFeed += distance
                # calculate the score
                distanceToWin+= self.manhattanDistance(players.players[player][animal]['position'],burrows.burrows[player_oponent]['position'])
                thisAnimalScore = iWillEat+distanceToWin-iWillFeed

                #print 'Animal Score: '+animal
                #print 'Animal Store: '+str(thisAnimalScore)
                animalsScores[animal] = thisAnimalScore

                if thisAnimalScore > bestAnimalScore:
                    bestAnimalScore = thisAnimalScore
                    bestAnimal      = animal+player_number


                # calculate the distante of animals that this feed
                for animalToFeed in self.rules.animals[animal]['food']:
                    if players.players[player_oponent][animalToFeed]['live']:

                        distance  = self.manhattanDistance(players.players[player][animal]['position'],players.players[player_oponent][animalToFeed]['position'])
                        if animal in animalsToFeed:
                            animalsToFeed[animal] += distance
                        else:
                            animalsToFeed[animal] = distance

                        if distance == 1:
                            bestToSafe.append(animal+player_number)

                        averangeAnimalsToFeed = (averangeAnimalsToFeed+distance)/2

        #print 'Need be safe :     '+str(bestToSafe)
        #print 'Need be eat  :     '+str(bestToEat)
        #print 'Best Animal  :     '+str(bestAnimal)

        # order and revert

        #print 'Animal Scores     :'+str(animalsScores)
        animalsScores = sorted(animalsScores.items(), key=operator.itemgetter(1))
        #print 'Animal Scores Ord :'+str(animalsScores)
        animalsScores.reverse()
        #print 'Animal Scores Reve:'+str(animalsScores)



        #
        # try move to eat
        if len(bestToEat) > 0:
            #print 'Executation: Best to eat'


            score = 0.0
            theBest = None
            for animals in bestToEat:
                if self.rules.animals[animals[1]]['score'] > score:
                    theBest = animals
            bestToEat = theBest

            command_interpreted['type']             = 1
            command_interpreted['short_label']      = bestToEat[1]+player_number
            command_interpreted['quadrant_to_go']   = players.players[player_oponent][bestToEat[0][0]]['position']

            #print 'animal   :'+bestToEat[0]
            #print 'eat by   :'+bestToEat[1]
            #print 'command  :'+str(command_interpreted)
            return command_interpreted

        #
        # try move to safe
        if len(bestToSafe) > 0:
            #print 'Executation: Best to Safe'

            score = 0.0
            theBest = None
            for animals in bestToSafe:
                if self.rules.animals[animals[0]]['score'] > score:
                    theBest = animals
            bestToSafe = theBest

            moves = self.rules.possiblesMoves(players.players[player][bestToSafe[0]]['position'])
            movesToReturn = []

            for move in moves:
                if matrix[move[0]][move[1]] == '  ':
                    willBeFood = False
                    for animalToFeed in self.rules.animals[animal]['food']:
                        if players.players[player_oponent][animalToFeed]['live']:
                            distance = self.manhattanDistance(move,players.players[player_oponent][animalToFeed]['position'])
                            if distance == 1:
                                willBeFood = True
                    if not willBeFood:
                        movesToReturn.append(move)

            #print 'Valids to safe'
            #print movesToReturn
            if len(movesToReturn) > 0:
                choice = randint(0,len(movesToReturn)-1)
                command_interpreted['type']             = 2
                command_interpreted['short_label']      = bestToSafe
                command_interpreted['quadrant_to_go']   = movesToReturn[choice]
                #print 'command :'+str(command_interpreted)
                return command_interpreted

        #
        # The rat is dead and the elephant need be restrained
        if not players.players[player]['R']['live'] and players.players[player_oponent]['E']['live'] and players.players[player]['E']['live']:
           #print 'Executation: get the elephant bitch!'

            moves = self.rules.possiblesMoves(players.players[player]['E']['position'])
            for move in moves:
                if matrix[move[0]][move[1]] == '  ':
                    movesToReturn.append(move)

            choiceMove = None
            distance = 999
            for move in movesToReturn:
                manhattanDistance = self.manhattanDistance(move,players.players[player_oponent]['E']['position'])
                willFeedSomeone = False

                for animalToFeed in self.rules.animals['E']['food']:
                    if players.players[player_oponent][animalToFeed]['live']:
                        distance = self.manhattanDistance(move,players.players[player_oponent][animalToFeed]['position'])
                        if distance == 1:
                            willFeedSomeone = True

                if manhattanDistance < distance and willFeedSomeone != True:
                    choiceMove = move

            if choiceMove != None:
                command_interpreted['type']             = 3
                command_interpreted['short_label']      = bestAnimal
                command_interpreted['quadrant_to_go']   = choiceMove
                #print 'comand: '+str(command_interpreted)
                return command_interpreted

        while(len(animalsScores)>0):

            #
            # try move to eat
            if len(animalsToEat) > 0 and averageAnimalsToEat < averangeToBurrow:
               #print 'Executation: move to eat'
                bestAnimalToEatDistance = 999
                bestAnimalToMove = None
                movesPossible = []
                movesSafes = []

                for animal in animalsToEat:
                    if animalsToEat[animal] < bestAnimalToEatDistance:
                        bestAnimalToEatDistance = animalsToEat[animal]
                        bestAnimalToMove        = animal

                #remove to not repeat
                del animalsToEat[bestAnimalToMove]

                moves = self.rules.possiblesMoves(players.players[player][bestAnimalToMove[0]]['position'])
                for move in moves:
                    if matrix[move[0]][move[1]] == '  ':
                        movesPossible.append(move)

                for move in movesPossible:
                    willFeedSomeone = False
                    for animalToFeed in self.rules.animals[bestAnimalToMove]['food']:
                        if players.players[player_oponent][animalToFeed]['live']:
                            distance  = self.manhattanDistance(move,players.players[player_oponent][animalToFeed]['position'])
                            if distance == 1:
                                willFeedSomeone = True
                    if not willFeedSomeone:
                        movesSafes.append(move)

                bestAnimalToEatDistance = 999
                bestAnimalToEat         = None
                bestMove                = None
                for moveSafe in movesSafes:
                    for animalToEat in self.rules.animals[bestAnimalToMove]['eat']:
                        if players.players[player_oponent][animalToEat]['live']:
                            distance  = self.manhattanDistance(moveSafe,players.players[player_oponent][animalToFeed]['position'])
                            if distance < bestAnimalToEatDistance:
                                bestAnimalToEatDistance = distance
                                bestAnimalEat           = animalToEat
                                bestMove                = moveSafe

                if bestMove != None:
                    command_interpreted['type']             = 4
                    command_interpreted['short_label']      = bestAnimalToMove
                    command_interpreted['quadrant_to_go']   = bestMove
                   #print 'comand: '+str(command_interpreted)
                    return command_interpreted

            #
            # try move to burrow
           #print 'Executation: move to burrow!'

            # get the best score to send!
            element     = animalsScores[0]
            bestAnimal  = element[0]
            animalsScores.remove(element)

            movesToReturn = []
            moves = self.rules.possiblesMoves(players.players[player][bestAnimal]['position'])
            for move in moves:
                if matrix[move[0]][move[1]] == '  ':

                    movesToReturn.append(move)
            choiceMove = None
            distance = 999
            for move in movesToReturn:
                manhattanDistance = self.manhattanDistance(move,burrows.burrows[player_oponent]['position'])
                willFeedSomeone = False

                for animalToFeed in self.rules.animals[bestAnimal]['food']:
                    if players.players[player_oponent][animalToFeed]['live']:
                        distance = self.manhattanDistance(move,players.players[player_oponent][animalToFeed]['position'])
                        if distance == 1:
                            willFeedSomeone = True

                if willFeedSomeone != True:
                    distance = manhattanDistance
                    choiceMove = move

            command_interpreted['type']             = 5
            command_interpreted['short_label']      = bestAnimal
            command_interpreted['quadrant_to_go']   = choiceMove
            #print 'comand  :'+str(command_interpreted)
            return command_interpreted



    def movesOnScene(self,state,jungleConfig):
        allMoves    = []

        players     = state.players
        burrows     = state.burrows
        matrix      = state.matrix
        player      = jungleConfig.howPlay()['player']

        player_oponent = ""

        if player == "player_1":
            player_oponent = "player_2"
            player_oponent_number = "2"
            player_number = "1"
        else:
            player_oponent = "player_1"
            player_oponent_number = "1"
            player_number = "2"

        command_interpreted = {}
        command_interpreted['message']      = ""
        command_interpreted['is_valid']     = True
        command_interpreted['short_label']  = ""
        command_interpreted['quadrant_to_go']   = None
        command_interpreted['player']       = player

        animalsScores           = {}
        bestAnimalScore         = 0
        animalsToEat            = {}
        averageAnimalsToEat     = 0
        animalsToFeed           = {}
        averangeAnimalsToFeed   = 0
        bestToSafe              = []
        bestToEat               = []
        averangeToBurrow        = 0

        for animal in players.players[player]:
            if players.players[player][animal]['live']:
                iWillEat        = 0
                iWillFeed       = 0
                distanceToWin   = 0
                #print 'animal: '+animal


                # calculate the avarange to borrow
                averangeToBurrow  = (averangeToBurrow+self.manhattanDistance(players.players[player][animal]['position'],burrows.burrows[player_oponent]['position']))/2

                # calculate the distante of animals that this eat
                for animalToEat in self.rules.animals[animal]['eat']:
                    if players.players[player_oponent][animalToEat]['live']:

                        distance  = self.manhattanDistance(players.players[player][animal]['position'],players.players[player_oponent][animalToEat]['position'])
                        if animal in animalsToEat:
                            animalsToEat[animal] += distance
                        else:
                            animalsToEat[animal] = distance

                        if distance == 1:
                            bestToEat.append([animalToEat,animal])

                        iWillEat += distance
                        averageAnimalsToEat = (averageAnimalsToEat+distance)/2
                for animalToFeed in self.rules.animals[animal]['food']:
                    if players.players[player_oponent][animalToEat]['live']:
                        distance  = self.manhattanDistance(players.players[player][animal]['position'],players.players[player_oponent][animalToFeed]['position'])
                        if distance <= 4:
                            iWillFeed += distance
                # calculate the score
                distanceToWin+= self.manhattanDistance(players.players[player][animal]['position'],burrows.burrows[player_oponent]['position'])
                thisAnimalScore = iWillEat+distanceToWin-iWillFeed

                #print 'Animal Score: '+animal
                #print 'Animal Store: '+str(thisAnimalScore)
                animalsScores[animal] = thisAnimalScore

                if thisAnimalScore > bestAnimalScore:
                    bestAnimalScore = thisAnimalScore
                    bestAnimal      = animal+player_number


                # calculate the distante of animals that this feed
                for animalToFeed in self.rules.animals[animal]['food']:
                    if players.players[player_oponent][animalToFeed]['live']:

                        distance  = self.manhattanDistance(players.players[player][animal]['position'],players.players[player_oponent][animalToFeed]['position'])
                        if animal in animalsToFeed:
                            animalsToFeed[animal] += distance
                        else:
                            animalsToFeed[animal] = distance

                        if distance == 1:
                            bestToSafe.append(animal+player_number)

                        averangeAnimalsToFeed = (averangeAnimalsToFeed+distance)/2

        #print 'Need be safe :     '+str(bestToSafe)
        #print 'Need be eat  :     '+str(bestToEat)
        #print 'Best Animal  :     '+str(bestAnimal)

        # order and revert

        #print 'Animal Scores     :'+str(animalsScores)
        animalsScores = sorted(animalsScores.items(), key=operator.itemgetter(1))
        #print 'Animal Scores Ord :'+str(animalsScores)
        animalsScores.reverse()
        #print 'Animal Scores Reve:'+str(animalsScores)



        #
        # try move to eat
        if len(bestToEat) > 0:
            #print 'Executation: Best to eat'


            score = 0.0
            theBest = None
            for animals in bestToEat:
                if self.rules.animals[animals[1]]['score'] > score:
                    theBest = animals
            bestToEat = theBest

            command_interpreted_1 = {}
            command_interpreted_1['is_valid']         = True
            command_interpreted_1['message']          = ""
            command_interpreted_1['player']           = player
            command_interpreted_1['type']             = 1
            command_interpreted_1['short_label']      = bestToEat[1]
            command_interpreted_1['quadrant_to_go']   = players.players[player_oponent][bestToEat[0][0]]['position']

            #print 'animal   :'+bestToEat[0]
            #print 'eat by   :'+bestToEat[1]
            #print 'command  :'+str(command_interpreted_1)
            allMoves.append(command_interpreted_1)

        #
        # try move to safe
        if len(bestToSafe) > 0:
            #print 'Executation: Best to Safe'

            score = 0.0
            theBest = None
            for animals in bestToSafe:
                if self.rules.animals[animals[0]]['score'] > score:
                    theBest = animals
            bestToSafe = theBest

            moves = self.rules.possiblesMoves(players.players[player][bestToSafe[0]]['position'])
            movesToReturn = []

            for move in moves:
                if matrix[move[0]][move[1]] == '  ':
                    willBeFood = False
                    for animalToFeed in self.rules.animals[animal]['food']:
                        if players.players[player_oponent][animalToFeed]['live']:
                            distance = self.manhattanDistance(move,players.players[player_oponent][animalToFeed]['position'])
                            if distance == 1:
                                willBeFood = True
                    if not willBeFood:
                        movesToReturn.append(move)

            #print 'Valids to safe'
            #print movesToReturn
            if len(movesToReturn) > 0:
                choice = randint(0,len(movesToReturn)-1)
                command_interpreted_2 = {}
                command_interpreted_2['is_valid']         = True
                command_interpreted_2['message']          = ""
                command_interpreted_2['player']           = player
                command_interpreted_2['type']             = 2
                command_interpreted_2['short_label']      = bestToSafe[0]
                command_interpreted_2['quadrant_to_go']   = movesToReturn[choice]
                #print 'command :'+str(command_interpreted_2)
                allMoves.append(command_interpreted_2)

        #
        # The rat is dead and the elephant need be restrained
        if not players.players[player]['R']['live'] and players.players[player_oponent]['E']['live'] and players.players[player]['E']['live']:
            #print 'Executation: get the elephant bitch!'

            moves = self.rules.possiblesMoves(players.players[player]['E']['position'])
            movesToReturn = []
            for move in moves:
                if matrix[move[0]][move[1]] == '  ':
                    movesToReturn.append(move)

            choiceMove = None
            distance = 999
            for move in movesToReturn:
                manhattanDistance = self.manhattanDistance(move,players.players[player_oponent]['E']['position'])
                willFeedSomeone = False

                for animalToFeed in self.rules.animals['E']['food']:
                    if players.players[player_oponent][animalToFeed]['live']:
                        distance = self.manhattanDistance(move,players.players[player_oponent][animalToFeed]['position'])
                        if distance == 1:
                            willFeedSomeone = True

                if manhattanDistance < distance and willFeedSomeone != True:
                    choiceMove = move

            if choiceMove != None:
                command_interpreted_3 = {}
                command_interpreted_3['is_valid']         = True
                command_interpreted_3['message']          = ""
                command_interpreted_3['player']           = player
                command_interpreted_3['type']             = 3
                command_interpreted_3['short_label']      = bestAnimal
                command_interpreted_3['quadrant_to_go']   = choiceMove
                #print 'comand: '+str(command_interpreted_3)
                allMoves.append(command_interpreted_3)
        tryToMoveToEat  = True
        tryToMoveBurrow = True
        while(len(animalsScores)>0 and (tryToMoveToEat or tryToMoveBurrow)):

            #
            # try move to eat
            if len(animalsToEat) > 0 and averageAnimalsToEat < averangeToBurrow:
                #print 'Executation: move to eat'
                bestAnimalToEatDistance = 999
                bestAnimalToMove = None
                movesPossible = []
                movesSafes = []

                for animal in animalsToEat:
                    if animalsToEat[animal] < bestAnimalToEatDistance:
                        bestAnimalToEatDistance = animalsToEat[animal]
                        bestAnimalToMove        = animal

                #remove to not repeat
                del animalsToEat[bestAnimalToMove]

                moves = self.rules.possiblesMoves(players.players[player][bestAnimalToMove[0]]['position'])
                for move in moves:
                    if matrix[move[0]][move[1]] == '  ':
                        movesPossible.append(move)

                for move in movesPossible:
                    willFeedSomeone = False
                    for animalToFeed in self.rules.animals[bestAnimalToMove]['food']:
                        if players.players[player_oponent][animalToFeed]['live']:
                            distance  = self.manhattanDistance(move,players.players[player_oponent][animalToFeed]['position'])
                            if distance == 1:
                                willFeedSomeone = True
                    if not willFeedSomeone:
                        movesSafes.append(move)

                bestAnimalToEatDistance = 999
                bestAnimalToEat         = None
                bestMove                = None
                for moveSafe in movesSafes:
                    for animalToEat in self.rules.animals[bestAnimalToMove]['eat']:
                        if players.players[player_oponent][animalToEat]['live']:
                            distance  = self.manhattanDistance(moveSafe,players.players[player_oponent][animalToFeed]['position'])
                            if distance < bestAnimalToEatDistance:
                                bestAnimalToEatDistance = distance
                                bestAnimalEat           = animalToEat
                                bestMove                = moveSafe

                if bestMove != None:
                    command_interpreted_4 = {}
                    command_interpreted_4['is_valid']         = True
                    command_interpreted_4['message']          = ""
                    command_interpreted_4['player']           = player
                    command_interpreted_4['type']             = 4
                    command_interpreted_4['short_label']      = bestAnimalToMove
                    command_interpreted_4['quadrant_to_go']   = bestMove
                    #print 'command: '+str(command_interpreted_4)
                    tryToMoveToEat = False
                    allMoves.append(command_interpreted_4)

            #
            # try move to burrow
            #print 'Executation: move to burrow!'

            # get the best score to send!
            element     = animalsScores[0]
            bestAnimal  = element[0]
            animalsScores.remove(element)

            movesToReturn = []
            moves = self.rules.possiblesMoves(players.players[player][bestAnimal]['position'])
            for move in moves:
                if matrix[move[0]][move[1]] == '  ':

                    movesToReturn.append(move)
            choiceMove = None
            distance = 999
            for move in movesToReturn:
                manhattanDistance = self.manhattanDistance(move,burrows.burrows[player_oponent]['position'])
                willFeedSomeone = False

                for animalToFeed in self.rules.animals[bestAnimal]['food']:
                    if players.players[player_oponent][animalToFeed]['live']:
                        distance = self.manhattanDistance(move,players.players[player_oponent][animalToFeed]['position'])
                        if distance == 1:
                            willFeedSomeone = True

                if willFeedSomeone != True:
                    distance = manhattanDistance
                    choiceMove = move
            if choiceMove != None:
                command_interpreted_5 = {}
                command_interpreted_5['is_valid']         = True
                command_interpreted_5['message']          = ""
                command_interpreted_5['player']           = player
                command_interpreted_5['type']             = 5
                command_interpreted_5['short_label']      = bestAnimal
                command_interpreted_5['quadrant_to_go']   = choiceMove
                #print 'comand  :'+str(command_interpreted_5)
                tryToMoveBurrow = False
                allMoves.append(command_interpreted_5)

        return allMoves

    def getBestMoveOnMoves(self, moves, state, config):

        bestValue    = -99999999
        returnMove   = None

        for move in moves:
            this_state = deepcopy(state)
            this_state.checkPosition(move['short_label'],move['quadrant_to_go'])
            this_state.updateAnimal(config.howPlay()['player'],move['short_label'][0],move['quadrant_to_go'])
            this_state.depth = 0
            this_value = self.getBestValue(this_state,config)
            if this_value > bestValue:
                bestValue = this_value
                returnMove = move

        #print 'getBestMoveOnMoves'
        #print str(returnMove)
        return returnMove


    def getBestValue(self,state,_config):

        value = 0
        config = copy(_config)
        config.nextPlayer()
        moves = self.movesOnScene(state,config)

        if state.depth != 4:
            for move in moves:
                this_state = deepcopy(state)
                this_state.checkPosition(move['short_label'],move['quadrant_to_go'])
                this_state.updateAnimal(config.howPlay()['player'],move['short_label'][0],move['quadrant_to_go'])
                this_state.depth = state.depth+1
                value += self.getBestValue(this_state,config)
        else:
            player = config.howPlay()['player']
            oponent_player = None
            if player == "player_1":
                oponent_player = "player_2"
            else:
                oponent_player = "player_1"
            for animal in state.players.players[player]:
                if state.players.players[player][animal]['live']:
                    value += 1
                else:
                    value -= 1
            for animal in state.players.players[oponent_player]:
                if state.players.players[oponent_player][animal]['live']:
                    value -= 1
                else:
                    value += 1

        return value


    def manhattanDistance(self,animal1,animal2):
        calculate   = abs(animal1[0] - animal2[0]) + abs(animal1[1] - animal2[1])
        #print 'manhattanDistance '+str(calculate)
        return calculate
