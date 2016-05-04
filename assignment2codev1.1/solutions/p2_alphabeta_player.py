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
		global maxDepth
		maxDepth = 0

		stateString = ""
		for i in state.board:
			stateString += str(i)
		stateString += str(state.player_row)

		bestAction = alphabetatranspositionTable.get(stateString, None)

		if bestAction is None:
			utility = self.maxValue(state, alpha, beta, 0)

		print str(maxDepth)
		
		bestAction = alphabetatranspositionTable.get(stateString, None)
		action = bestAction[0]
		return bestAction[1]

	def maxValue(self, state, alpha, beta, depth):

		'''
		global maxDepth
		if depth > maxDepth:
			maxDepth = depth
		'''

		stateString = ""
		for i in state.board:
			stateString += str(i)
		stateString += str(state.player_row)

		bestAction = alphabetatranspositionTable.get(stateString, None)
		if bestAction is None:

			# Terminal test
			if (state.is_terminal()): 
				utility = state.utility(player)
				print "TERMINAL " + stateString + " " + str(utility)
				alphabetatranspositionTable[stateString] = (None, utility, depth)
				return utility

			# Past lowest possible utility, effectively negative infinite
			utility = -2

			# Get the actions from this state
			actions = state.actions()

			# No available actions, repeat state but switch players
			if not(actions):
				nextState = State(state.board, state.opponent_row, state.player)
				utility = self.minValue(nextState, alpha, beta, depth + 1)
				alphabetatranspositionTable[stateString] = (None, utility, depth)

				if (utility >= beta):
					return utility

				if (utility > alpha):
					alpha = utility

			# Actions available
			while (actions):

				currentAction = actions.pop(0)
				nextState = state.result(currentAction)

				utilityTmp = self.minValue(nextState, alpha, beta, depth + 1)
				if (depth == 0):
					print str(nextState.board) + " " + str(utilityTmp)

				if (utility < utilityTmp):

					utility = utilityTmp
					bestAction = currentAction
					alphabetatranspositionTable[stateString] = (bestAction, utility, depth)


				if (utility >= beta):
					return utility

				if (utility > alpha):
					alpha = utility

			return utility

		else:
			return bestAction[1]

	def minValue(self, state, alpha, beta, depth):
		'''
		global maxDepth
		if depth > maxDepth:
			maxDepth = depth

		'''

		stateString = ""
		for i in state.board:
			stateString += str(i)
		stateString += str(state.player_row)


		bestAction = alphabetatranspositionTable.get(stateString, None)
		if bestAction is None:

			# Terminal test
			if (state.is_terminal()): 
				utility = state.utility(player)
				print "TERMINAL " + stateString + " " + str(utility)
				alphabetatranspositionTable[stateString] = (None, utility, depth)
				return utility

			# Past lowest possible utility, effectively negative infinite
			utility = 2

			# Get the actions from this state
			actions = state.actions()

			# No available actions, repeat state but switch players
			if not(actions):
				nextState = State(state.board, state.opponent_row, state.player)
				utility = self.maxValue(nextState, alpha, beta, depth + 1)
				alphabetatranspositionTable[stateString] = (None, utility, depth)

				if (utility <= alpha):
					return utility

				if (beta > utility):
					beta = utility

			# Actions available
			while (actions):

				currentAction = actions.pop(0)
				nextState = state.result(currentAction)

				utilityTmp = self.maxValue(nextState, alpha, beta, depth + 1)
				if (utility > utilityTmp):
					utility = utilityTmp
					bestAction = currentAction
					alphabetatranspositionTable[stateString] = (bestAction, utility, depth)


				if (utility <= alpha):
					return utility

				if (utility < beta):
					beta = utility

			return utility
			
		else:

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

		#print "ACTION: " + str(action.row) +  " " + str(action.index)

		
		

		return action

		#raise NotImplementedError("Need to implement this method")