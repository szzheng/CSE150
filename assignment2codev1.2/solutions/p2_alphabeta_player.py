# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action

class AlphaBetaPlayer(Player):
	def move(self, state):
		"""Calculates the best move from the given board using the minimax
		algorithm with alpha-beta pruning and transposition table.
		:param state: State, the current state of the board.
		:return: Action, the next move
		"""

		global player
		player = state.player

		global transpositionTableForMax
		transpositionTableForMax = {}

		global transpositionTableForMin
		transpositionTableForMin = {}

		return self.alphabeta(state)

	def alphabeta(self, state):

		''' state key '''
		'''
		stateString = ""
		for i in state.board:
			stateString += str(i)
			stateString += ","
		'''
		stateString = state.ser()

		global transpositionTableForMax
		transpositionTableForMax = {}

		global transpositionTableForMin
		transpositionTableForMin = {}

		self.maxValue(state, -2, 2, 0)

		action = transpositionTableForMax.get(stateString, None)
		if (action is None):
			return None
		else:
			return action[0]

	def maxValue(self, state, alpha, beta, depth):

		global transpositionTableForMax

		''' state key '''
		'''
		stateString = ""
		for i in state.board:
			stateString += str(i)
			stateString += ","
		'''
		stateString = state.ser()


		''' Check to see if we've already encountered this state '''
		'''
		action = transpositionTableForMax.get(stateString, None)
		if not(action is None):
			return action[1]
		'''

		''' 1. Terminal test '''
		if (state.is_terminal()): 
			utility = state.utility(player)
			#transpositionTableForMax[stateString] = (None, utility, depth)
			return utility

		''' 2. Initialize utility to negative infinite (effectively) '''
		utility = -2 


		''' Process actions '''
		actions = state.actions()

		# No actions available
		if not(actions): 
			nextState = State(state.board, state.opponent_row, state.player)
			utility = self.minValue(nextState, alpha, beta, depth + 1)
			#transpositionTableForMax[stateString] = (None, utility, depth)

			# Prune if possible
			'''
			if (utility >= beta):
				print "PRUNING WHEN THERE's NO ACTION"
				return utility
			'''
			'''
			if (utility > alpha):
				alpha = utility
			'''
			return utility

		else:
			bestAction = transpositionTableForMax.get(stateString, None)
			if not(bestAction is None):
				currentAction = bestAction[0]
				nextState = state.result(currentAction)

				utilityTmp = self.minValue(nextState, alpha, beta, depth + 1)


				# Get the max utility
				if (utility < utilityTmp):
					utility = utilityTmp
					transpositionTableForMax[stateString] = (currentAction, utility, depth)


				# Prune if possible
				if (utility >= beta):
					return utility
				if (utility > alpha):
					alpha = utility

				while (actions):

					currentAction = actions.pop(0)
					if not(currentAction == bestAction[0]):
						nextState = state.result(currentAction)

						utilityTmp = self.minValue(nextState, alpha, beta, depth + 1)

						# Get the max utility
						if (utility < utilityTmp):
							utility = utilityTmp
							transpositionTableForMax[stateString] = (currentAction, utility, depth)


						# Prune if possible
						if (utility >= beta):
							return utility
						if (utility > alpha):
							alpha = utility
			else :
				while (actions):

					currentAction = actions.pop(0)
					nextState = state.result(currentAction)

					utilityTmp = self.minValue(nextState, alpha, beta, depth + 1)

					# Get the max utility
					if (utility < utilityTmp):
						utility = utilityTmp
						transpositionTableForMax[stateString] = (currentAction, utility, depth)


					# Prune if possible
					if (utility > beta):
						return utility
					if (utility > alpha):
						alpha = utility

			return utility

	def minValue(self, state, alpha, beta, depth):

		global transpositionTableForMin

		''' state key '''
		'''
		stateString = ""
		for i in state.board:
			stateString += str(i)
			stateString += ","
		'''
		stateString = state.ser()


		''' Check to see if we've already encountered this state '''
		'''
		action = transpositionTableForMin.get(stateString, None)
		if not(action is None):
			return action[1]
		'''

		''' 1. Terminal test '''
		if (state.is_terminal()): 
			utility = state.utility(player)
			#transpositionTableForMin[stateString] = (None, utility, depth)
			return utility

		''' 2. Initialize utility to positive infinite (effectively) '''
		utility = 2

		''' Process actions '''
		actions = state.actions()

		# No actions available
		if not(actions): 
			nextState = State(state.board, state.opponent_row, state.player)
			utility = self.maxValue(nextState, alpha, beta, depth + 1)
			#transpositionTableForMin[stateString] = (None, utility, depth)

			'''
			if (utility <= alpha):
				print "PRUNING WHEN THERE's NO ACTION"
				return utility
			'''
			'''
			if (utility > beta):
				beta = utility
			'''

			return utility

		else:

			bestAction = transpositionTableForMin.get(stateString, None)
			if not(bestAction is None):
				currentAction = bestAction[0]
				nextState = state.result(currentAction)

				utilityTmp = self.maxValue(nextState, alpha, beta, depth + 1)

				# Get the max utility
				if (utility > utilityTmp):
					utility = utilityTmp
					transpositionTableForMin[stateString] = (currentAction, utility, depth)

				if (utility <= alpha):
					return utility

				if (utility > beta):
					beta = utility

				while (actions):

					currentAction = actions.pop(0)
					if not(currentAction == bestAction[0]):
						nextState = state.result(currentAction)

						utilityTmp = self.maxValue(nextState, alpha, beta, depth + 1)

						# Get the max utility
						if (utility > utilityTmp):
							utility = utilityTmp
							transpositionTableForMin[stateString] = (currentAction, utility, depth)

						if (utility < alpha):
							return utility

						if (utility > beta):
							beta = utility

			else:
				while (actions):

					currentAction = actions.pop(0)
					nextState = state.result(currentAction)

					utilityTmp = self.maxValue(nextState, alpha, beta, depth + 1)

					# Get the max utility
					if (utility > utilityTmp):
						utility = utilityTmp
						transpositionTableForMin[stateString] = (currentAction, utility, depth)

					if (utility <= alpha):
						return utility

					if (utility > beta):
						beta = utility

			return utility
