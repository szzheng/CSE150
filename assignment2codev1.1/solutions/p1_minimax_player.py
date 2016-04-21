# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action


class MinimaxPlayer(Player):
    def __init__(self):
        self.cache ={}

    player = None


    def minimax(self, state, first):
        global action  

        actionIndex = state.M * 2 + 2

        actions = state.actions()

        # Reached terminal state
        if (state.is_terminal()): 

            # Return the state's utility 
            return state.utility(player)

        # max
        if (state.player_row == player.row):
            utility = -2

            if not(actions):
                # no actions available
                nextState = State(state.board, state.opponent_row, state.player)
                utility = self.minimax(nextState, first + 1)

            bestAction = None
            while (actions):
                currentAction = actions.pop()
                nextState = state.result(currentAction)
 
                utilityTmp = self.minimax(nextState, first + 1)


                if (first == 1):
                    print str(utilityTmp)

                if (utility <= utilityTmp):
                    utility = utilityTmp

                    # first move
                    if (first == 1):
                        action = currentAction
                        actionIndex = currentAction.index

                # first move
                '''
                if (utility == utilityTmp):
                    if (first == 1):
                        if (currentAction.index < actionIndex):
                            action = currentAction
                            actionIndex = currentAction.index'''
   

        # min
        if (state.player_row != player.row):
            utility = 2

            if not(actions):
                # no actions available
                nextState = State(state.board, state.opponent_row, state.player)
                utility = self.minimax(nextState, first + 1)

            while (actions):
                currentAction = actions.pop(0)
                nextState = state.result(currentAction)

                utilityTmp = self.minimax(nextState, first + 1)



                if (utility > utilityTmp):
                    utility = utilityTmp

                    # first move
                    if (first == 1):
                        action = currentAction
                        actionIndex = currentAction.index



        return utility

    def move(self, state):
        """
        Calculates the best move from the given board using the minimax
        algorithm.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """

        ###### Start searching ######
        global player
        player = state.player

        utility = self.minimax(state, 1)



        print "ACTION: " + str(action.row) +  " " + str(action.index)

        return action

        #raise NotImplementedError("Need to implement this method")


