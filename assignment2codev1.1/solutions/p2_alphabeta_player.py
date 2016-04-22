# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action

class AlphaBetaPlayer(Player):

	player = None
	alphabetatranspositionTable = {}
	action = None

	def alphabeta(self, state, alpha, beta):

		global action

		stateString = ""
		for i in state.board:
			stateString += str(i)
		stateString += str(state.player_row)

		bestAction = alphabetatranspositionTable.get(stateString, None)

		if bestAction is None:
			utility = self.maxValue(state, alpha, beta)
		
		bestAction = alphabetatranspositionTable.get(stateString, None)
		action = bestAction[0]
		return bestAction[1]

	def maxValue(self, state, alpha, beta):

		stateString = ""
		for i in state.board:
			stateString += str(i)
		stateString += str(state.player_row)

		bestAction = alphabetatranspositionTable.get(stateString, None)
		if bestAction is None:

			# Terminal test
			if (state.is_terminal()): 
				return state.utility(player)

			# Past lowest possible utility, effectively negative infinite
			utility = -2

			# Get the actions from this state
			actions = state.actions()

			bestAction = None

			# No available actions, repeat state but switch players
			if not(actions):
				nextState = State(state.board, state.opponent_row, state.player)
				utility = self.minValue(nextState, alpha, beta)

				if (utility >= beta):
					return utility

				if (utility > alpha):
					alpha = utility

			# Actions available
			while (actions):
				currentAction = actions.pop(0)
				nextState = state.result(currentAction)

				utilityTmp = self.minValue(nextState, alpha, beta)
				if (utilityTmp > utility):
					utility = utilityTmp
					bestAction = currentAction
					alphabetatranspositionTable[stateString] = (bestAction, utility)

				'''
				# tie break
				if (utility == utilityTmp):
					bestAction = alphabetatranspositionTable.get(stateString, None)
					index = bestAction[0].index
					if (currentAction.index < index):
						print "tiebreaking"
						bestAction = currentAction
						alphabetatranspositionTable[stateString] = (bestAction, utility)'''

				if (utility >= beta):
					return utility

				if (utility > alpha):
					alpha = utility

			return utility
		if not(bestAction is None):
			return bestAction[1]

	def minValue(self, state, alpha, beta):

		stateString = ""
		for i in state.board:
			stateString += str(i)
		stateString += str(state.player_row)

		bestAction = alphabetatranspositionTable.get(stateString, None)
		if bestAction is None:

			# Terminal test
			if (state.is_terminal()): 
				return state.utility(player)

			# Past lowest possible utility, effectively negative infinite
			utility = 2

			# Get the actions from this state
			actions = state.actions()

			# No available actions, repeat state but switch players
			if not(actions):
				nextState = State(state.board, state.opponent_row, state.player)
				utility = self.maxValue(nextState, alpha, beta)

				if (utility <= alpha):
					return utility

				if (beta > utility):
					beta = utility

			# Actions available
			while (actions):
				currentAction = actions.pop(0)
				nextState = state.result(currentAction)

				utilityTmp = self.maxValue(nextState, alpha, beta)
				if (utility > utilityTmp):
					utility = utilityTmp
					bestAction = currentAction
					alphabetatranspositionTable[stateString] = (bestAction, utility)

				# tie break
				'''
				if (utility == utilityTmp):
					bestAction = alphabetatranspositionTable.get(stateString, None)
					index = bestAction[0].index
					if (currentAction.index < index):
						print "tiebreaking"
						bestAction = currentAction
						alphabetatranspositionTable[stateString] = (bestAction, utility)'''


				if (utility <= alpha):
					return utility

				if (utility < beta):
					beta = utility

			return utility
			
		if not(bestAction is None):
			return bestAction[1]

	def move(self, state):
		"""Calculates the best move from the given board using the minimax
		algorithm with alpha-beta pruning and transposition table.
		:param state: State, the current state of the board.
		:return: Action, the next move
		"""
		###### Start searching ######



		global alphabetatranspositionTable
		alphabetatranspositionTable = {}
		
		global player
		player = state.player


	

		#### ALPHA BETA COMPARISON ###

		utility = self.alphabeta(state, -2, 2)

		print "ACTION: " + str(action.row) +  " " + str(action.index)

		
		

		return action

		#raise NotImplementedError("Need to implement this method")