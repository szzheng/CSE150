# -*- coding: utf-8 -*-
__author__ = 'Dan'
__email__ = 'daz040@eng.ucsd.edu'

from assignment2 import Player, State, Action

class AlphaBetaPlayer(Player):

	player = None
	alphabetatranspositionTable = {}


	def alphabeta(self, state, alpha, beta, first):

		global action  

		actionIndex = state.M * 2 + 2

		actions = state.actions()

		# Reached terminal state
		if (state.is_terminal()): 

			# Return the state's utility 
			return state.utility(player)

		# max
		if (state.player_row == player.row):
			#utility = -1

			if not(actions):
				# no actions available
				nextState = State(state.board, state.opponent_row, state.player)
				alphaTmp = self.alphabeta(nextState, alpha, beta, first + 1)
				if (alphaTmp > alpha):
					alpha = alphaTmp
				return alphaTmp

			actualMaxValue = -2
			while (actions):
				currentAction = actions.pop()
				nextState = state.result(currentAction)
 
				alphaTmp = self.alphabeta(nextState, alpha, beta, first + 1)

				if (actualMaxValue < alphaTmp):
					actualMaxValue = alphaTmp
				if (alpha < alphaTmp):
					alpha = alphaTmp

					# first move
					if (first == 1):
						action = currentAction
						actionIndex = currentAction.index
						print "new index with " + str(alpha)
				
				#tie breaker
				# first move
				if (alpha == alphaTmp):
					if (first == 1):
						if (currentAction.index < actionIndex):
							action = currentAction
							actionIndex = currentAction.index
							print "change index with utility is " + str(alpha)
				

				# PRUNE
				#if (alpha >= beta):
				#	break;
			if (first < 5):
				print "max Utility being returned is " + str(alpha)
			return actualMaxValue
		# min
		if (state.player_row != player.row):
			utility = 1

			if not(actions):
				# no actions available
				nextState = State(state.board, state.opponent_row, state.player)
				betaTmp = self.alphabeta(nextState, alpha, beta, first + 1)
				if (betaTmp < beta):
					beta = betaTmp

				return betaTmp

			actualMinValue = 2
			while (actions):
				currentAction = actions.pop()
				nextState = state.result(currentAction)

				betaTmp = self.alphabeta(nextState, alpha, beta, first + 1)

				if (actualMinValue > betaTmp):
					actualMinValue = betaTmp
				if (beta > betaTmp):
					beta = betaTmp

				# PRUNE
				#if (alpha >= beta):
				#	break;
			if (first < 5):
				print "min Utility being returned is " + str(beta)
			return actualMinValue


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

		utility = self.alphabeta(state, -2, 2, 1)

		print "ACTION: " + str(action.row) +  " " + str(action.index)

		
		

		return action

		#raise NotImplementedError("Need to implement this method")