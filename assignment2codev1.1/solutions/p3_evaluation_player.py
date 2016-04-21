# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action


class EvaluationPlayer(Player):
    def move(self, state):
        """Calculates the best move after 1-step look-ahead with a simple
        evaluation function.
        :param state: State, the current state of the board.
        :return: Action, the next move
        """

        # *You do not need to modify this method.*
        best_value = -1.0

        actions = state.actions()
        if not actions:
            actions = [None]

        best_move = actions[0]
        for action in actions:
            result_state = state.result(action)
            value = self.evaluate(result_state, state.player_row)
            if value > best_value:
                best_value = value
                best_move = action

        # Return the move with the highest evaluation value
        print "ACTION: " + str(best_move.row) + " " + str(best_move.index)
        return best_move

    def evaluate(self, state, my_row):
        """
        Evaluates the state for the player with the given row
        """


        m = state.M 
        n = state.N 


        ''' initialize variables '''
        yourGoalIndex = 0
        opponnentGoalIndex = 0
        stonesInYourGoal = 0
        stonesInOpponentGoal = 0
        stonesOnYourSide = 0
        stonesOnOpponentSide = 0
        ''' end  initialize variables '''

        ''' evaluate for TOP plyaer '''
        if (my_row == 1):
            yourGoalIndex = 2 * m + 1
            opponnentGoalIndex = m

            stonesInYourGoal = state.board[yourGoalIndex]
            stonesInOpponentGoal = state.board[opponnentGoalIndex]

            for i in range (opponnentGoalIndex + 1, yourGoalIndex):
                stonesOnYourSide += state.board[i]

            for i in range (0, opponnentGoalIndex):
                stonesOnOpponentSide += state.board[i]
        ''' END - evaluate for TOP player '''

        ''' Evaluate for BOTTOM player '''
        if (my_row == 0):
            print "MY ROW IS 0"
            yourGoalIndex = m
            opponnentGoalIndex = 2 * m + 1

            for i in range (0, yourGoalIndex):
                stonesOnYourSide += state.board[i]

            for i in range (yourGoalIndex + 1, opponnentGoalIndex):
                stonesOnOpponentSide += state.board[i]
        
        ''' End - evaluate for BOTTOM player '''
        #print "stonesInYourGoal: " + str(stonesInYourGoal)
        #print "stonesInOpponentGoal: " + str(stonesInOpponentGoal)
        #print "stonesOnYourSide: " + str(stonesOnYourSide)
        #print "stonesOnOpponentSide: " + str(stonesOnOpponentSide)

        value = (stonesInYourGoal - stonesInOpponentGoal + stonesOnYourSide - stonesOnOpponentSide)
        value = float(value) / (2 * m * n)
        #print "m: " + str(m)  + " n: " + str(n)
        #print "value: " + str(value)
        



        #raise NotImplementedError("Need to implement this method")

        return value
