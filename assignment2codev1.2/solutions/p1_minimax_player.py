# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action

class MinimaxPlayer(Player):
	def __init__(self):
		self.cache ={}

	def move(self, state):
		"""
		Calculates the best move from the given board using the minimax
		algorithm.
		:param state: State, the current state of the board.
		:return: Action, the next move
		"""

		global player
		player = state.player

		global transpositionTable
		transpositionTable = {}

		return self.minimax(state)

	def minimax(self, state):

		''' state key '''
		'''
		stateString = ""
		for i in state.board:
			stateString += str(i)
			stateString += ","
		stateString += str(state.player_row)
		'''
		stateString = state.ser()


		global transpositionTable
		transpositionTable = {}

		self.maxValue(state, 0)

		action = transpositionTable.get(stateString, None)
		if (action is None):
			return None
		else:
			return action[0]

	def maxValue(self, state, depth):

		global transpositionTable

		''' state key '''
		'''
		stateString = ""
		for i in state.board:
			stateString += str(i) 
			stateString += ","
		stateString += str(state.player_row)
		'''
		stateString = state.ser()


		''' 1. Terminal test '''
		if (state.is_terminal()): 
			utility = state.utility(player)
			transpositionTable[stateString] = (None, utility)
			return utility

		''' 2. Initialize utility to negative infinite (effectively) '''
		utility = -2 


		''' Process actions '''
		actions = state.actions()

		# No actions available
		if not(actions): 
			nextState = State(state.board, state.opponent_row, state.player)
			utility = self.minValue(nextState, depth + 1)
			transpositionTable[stateString] = (None, utility)
			return utility

		else:
			while (actions):

				currentAction = actions.pop(0)
				nextState = state.result(currentAction)

				utilityTmp = self.minValue(nextState, depth + 1)

				# Get the max utility
				if (utility < utilityTmp):
					utility = utilityTmp
					transpositionTable[stateString] = (currentAction, utility)


			return utility

	def minValue(self, state, depth):

		global transpositionTable

		''' state key '''
		'''
		stateString = ""
		for i in state.board:
			stateString += str(i)
			stateString += ","
		stateString += str(state.player_row)
		'''
		stateString = state.ser()


		''' 1. Terminal test '''
		if (state.is_terminal()): 
			utility = state.utility(player)
			transpositionTable[stateString] = (None, utility)
			return utility

		''' 2. Initialize utility to positive infinite (effectively) '''
		utility = 2

		''' Process actions '''
		actions = state.actions()

		# No actions available
		if not(actions): 
			nextState = State(state.board, state.opponent_row, state.player)
			utility = self.maxValue(nextState, depth + 1)
			transpositionTable[stateString] = (None, utility)
			return utility

		else:
			while (actions):

				currentAction = actions.pop(0)
				nextState = state.result(currentAction)

				utilityTmp = self.maxValue(nextState, depth + 1)

				# Get the max utility
				if (utility > utilityTmp):
					utility = utilityTmp
					transpositionTable[stateString] = (currentAction, utility)


			return utility
